from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
	products = Product.objects.all()
	return render(request, 'index.html', 
			{'products': products })

# /products -> index function
# Url:Uniform Resourse Locator
#def index(request):
# find all the products 
#	products = Product.objects.all()
# find the products price above 2.00 or no stock
#	Product.object.filter()
# find just one product
#	Product.object.get()
# save the producdt
#	Product.object.save()
	return HttpResponse('HelloWorld')


def new(request):
	return HttpResponse('New Product')
