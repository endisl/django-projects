from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection, Customer, Order, OrderItem, Product


def say_hello(request):
    # Customers with .com accounts
    query_set = Customer.objects.filter(email__contains='.com')

    # Collections that don't have a featured product
    #query_set = Collection.objects.filter(featured_product__isnull=True)

    # Products with low inventory (less than 10)
    #query_set = Product.objects.filter(inventory__lt=10)

    # Orders placed by customer with id = 1
    #query_set = Order.objects.filter(customer__id=1)

    # Order items for products in collection 3
    #query_set = OrderItem.objects.filter(Product.objects.filter(collection__id=3))

    return render(request, 'hello.html', {'name': 'John', 'results': list(query_set)})
