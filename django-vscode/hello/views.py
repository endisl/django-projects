import imp
from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.http import HttpResponse
from hello.forms import LogMessageForm
from hello.models import LogMessage


def home(request):
    return render(request, "hello/home.html")


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
