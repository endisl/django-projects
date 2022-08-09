from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    product = Product.objects.filter(pk=0).first()  # return None

    return render(request, 'hello.html', {'name': 'John'})
