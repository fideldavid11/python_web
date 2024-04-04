from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera aplicación web con Django.")
