import re
from django.utils.timezone import datetime
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now

    return HttpResponse(content)


print("http://127.0.0.1:8000/hello/VSCode")
