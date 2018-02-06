from django.http import HttpResponse


def welcome(request):
    return HttpResponse(".. Implemented Django and GitHub Repro")
