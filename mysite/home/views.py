from django.shortcuts import render

# Create your views here.
from product.models import Category, Product


def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context={'page':'home',
             'category': category,
             'products':products}
    return render(request,'index.html',context)