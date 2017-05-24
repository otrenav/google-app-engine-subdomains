
from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body><h1>Version 2</h1></body></html>')
