from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.db.models import Q


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers
    }

    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')

    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()

    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()

    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember
    }

    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))


def testing(request):
    #mydata = Members.objects.values_list('firstname')
    #mydata = Members.objects.filter(lastname='Doe', id=3).values()
    #mydata = Members.objects.filter(firstname='John').values() | Members.objects.filter(firstname='Tobias').values()
    #mydata = Members.objects.filter(Q(firstname='John') | Q(firstname='Tobias')).values()
    #mydata = Members.objects.filter(firstname__startswith='L').values()
    #mydata = Members.objects.order_by('-firstname').values()
    mydata = Members.objects.all().order_by('lastname', '-id').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
