from django.http import HttpResponse


def welcome(request):
    return HttpResponse("comming web project -- :)")
