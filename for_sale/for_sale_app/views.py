from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.


def index(request):
    queryset = Product.objects.all()
    context = {
        'product_list': queryset
    }
    return render(request, 'for_sale_app/index.html', context)


def product_detail(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, 'for_sale_app/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "for_sale_app/product_create.html", context)

