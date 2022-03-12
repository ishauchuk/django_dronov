from django.http import HttpResponse


def index(request):
    return HttpResponse("The list of announcements will be displayed here.")
