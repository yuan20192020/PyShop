from django.urls import path
from . import views


# Import other modules in the same package above.
# Why do not use 'import views' ,as views are used everywhere

# This is the root url path below
# /products
# /products/1/detail
# /products/new

# view.index is not calling the function

urlpatterns = [
        path('', views.index),
	path('new', views.new)
]
