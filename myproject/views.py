from django.http import HttpResponse

def index(request):
    response = "¡Hola, mundo! Soy Fidel Pineda!"
    return HttpResponse(response)


