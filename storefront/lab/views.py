from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
import requests

#from .tasks import notify_customers
#from templated_mail.mail import BaseEmailMessage
#from django.core.mail import EmailMessage, BadHeaderError
#from django.db.models import Value, F, Q, Func, ExpressionWrapper, DecimalField, Count
#from django.db.models.functions import Concat
#from django.db.models.aggregates import Count, Max, Min, Avg, Sum
#from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.contenttypes.models import ContentType
#from django.db import transaction
#from django.db import connection
#from store.models import Collection, Customer, Order, OrderItem, Product
#from tags.models import TaggedItem

logger = logging.getLogger(__name__)


class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'John'})

# @transaction.atomic()
# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()

#     return render(request, 'hello.html', {'name': data})

    # notify_customers.delay('Owner')

    """ try:
            message = BaseEmailMessage(
                template_name='emails/hello.html',
                context={'name': 'Ndion'}
            )
            message.send(['sicocar@ndionbuy.com']) """

    # message = EmailMessage('subject', 'message',
    #                       'info@ndionbuy.com', ['vandeste@ndionbuy.com'])
    # message.attach_file('/static/images/hacking.jpg')
    # message.send()

    #mail_admins('subject', 'message', html_message='message')

    #send_mail('subject', 'message', 'info@ndionbuy.com', ['john@ndionbuy.com'])
    """ except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Ndion'}) """

    # with connection.cursor() as cursor:
    #    cursor.execute('')
    #    cursor.callproc('get_customers', [10, 20, 'abc'])

    #queryset = Product.objects.raw('SELECT id, title FROM store_product')

    """ with transaction.atomic():
        order = Order()
        order.customer_id = -1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save() """

    #collection = Collection(pk=12)
    # collection.delete()
    #collection.featured_product = None
    #collection.featured_product_id = 1
    # collection.save()

    # Collection.objects.filter(id__gt=5).delete()

    # Collection.objects.filter(pk=11).update(featured_product=None)

    #collection = Collection.objects.create(title='a', featured_product_id=1)
    # collection.id

    #queryset = TaggedItem.objects.get_tags_for(Product, 1)

    # discounted_price = ExpressionWrapper(
    #    F('unit_price') * 0.8, output_field=DecimalField())
    #queryset = Product.objects.annotate(discounted_price=discounted_price)

    #queryset = Customer.objects.annotate(orders_count=Count('order'))

    # queryset = Customer.objects.annotate(
    # concat
    #    full_name=Func(F('first_name'), Value(
    #        ' '), F('last_name'), function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    # concat
    #    full_name=Concat('first_name', Value(' '), 'last_name')
    # )

    #queryset = Customer.objects.annotate(new_id=F('id')+1)
    #queryset = Customer.objects.annotate(is_new=Value(True))

    # What is the min, max and average price of the products in collection 3?
    # result = Product.objects.filter(collection__id=3).aggregate(
    #    min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))

    # How many orders has customer 1 placed? -> 5
    #result = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))

    # How many units of product 1 have we sold? -> 4
    # result = OrderItem.objects.filter(
    #    product__id=1).aggregate(sold_units=Sum('quantity'))

    # How many orders do we have? -> 1000
    #result = Order.objects.aggregate(count=Count('id'))

    # result = Product.objects.filter(collection__id=3).aggregate(
    #    count=Count('id'), min_price=Min('unit_price'))

    # queryset = Order.objects.select_related(
    #    'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

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

    # return render(request, 'hello.html', {'name': 'John', 'result': list(queryset)})
