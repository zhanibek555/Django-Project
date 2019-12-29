from django.http import HttpResponse

def func(request):
    return HttpResponse('<h1>Test Test!</h>')