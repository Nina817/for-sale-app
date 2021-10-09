from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    queryset = Product.objects.all()
    context = {
        'product_list': queryset
    }
    return render(request, 'for_sale_app/index.html', context)
