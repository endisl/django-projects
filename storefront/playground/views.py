from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Collection, Customer, Order, OrderItem, Product


def say_hello(request):
    queryset = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    #queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    #queryset = Product.objects.select_related('collection').all()

    #queryset = Product.objects.defer('description', 'slug')

    #arg = OrderItem.objects.values('product_id').distinct()
    #queryset = Product.objects.filter(id__in=arg).order_by('title')

    #queryset = Product.objects.values_list('id', 'title', 'collection__title')

    #queryset = Product.objects.all()[5:10]

    #product = Product.objects.order_by('unit_price')[0]
    #product = Product.objects.earliest('unit_price')
    #product = Product.objects.latest('unit_price')

    #query_set = Product.objects.filter(collection__id=1).order_by('unit_price', '-title').reverse()

    #query_set = Product.objects.filter(inventory=F('collection__id'))

    #query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # Customers with .com accounts
    # query_set = Customer.objects.filter(email__icontains='.com')

    # Collections that don't have a featured product
    # query_set = Collection.objects.filter(featured_product__isnull=True)

    # Products with low inventory (less than 10)
    # query_set = Product.objects.filter(inventory__lt=10)

    # Orders placed by customer with id = 1
    # query_set = Order.objects.filter(customer__id=1)

    # Order items for products in collection 3
    # query_set = OrderItem.objects.filter(product__collection__id=3)

    return render(request, 'hello.html', {'name': 'John', 'results': list(queryset)})
