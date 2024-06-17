from django.shortcuts import render

# Create your views here.
def all_hereos(request):
    return render(request, 'myApp/all_heroes.html')