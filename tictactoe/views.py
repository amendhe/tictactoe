from django.http import HttpResponse


def welcome(request):
    return HttpResponse("This is my comming web project -- :)")
