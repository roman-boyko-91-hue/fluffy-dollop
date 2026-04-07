from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Наш каталог'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
