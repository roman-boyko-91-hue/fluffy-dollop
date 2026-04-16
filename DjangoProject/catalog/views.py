from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наш каталог'
        return context


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


def form_valid(self, form):
    product = form.save()
    product.owner = self.request.user
    product.save()
    return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_product'

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductForm
        return ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # Если юзер не владелец И не модератор — доступ запрещен
        if self.object.owner != self.request.user and not self.request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied
        return self.object


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # Удалять может владелец ИЛИ модератор
        if self.object.owner != self.request.user and not self.request.user.has_perm('catalog.delete_product'):
            raise PermissionDenied
        return self.object
