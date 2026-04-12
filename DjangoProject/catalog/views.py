from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наш каталог'
        return context


class ContactTemplateView(TemplateView):
    template_name = 'main/contact.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
