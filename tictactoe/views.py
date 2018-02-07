from django.http import HttpResponse


def welcome(request):
    return HttpResponse("today is Rose day..!!")
