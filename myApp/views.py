from django.shortcuts import render, get_object_or_404
from .models import HeroVariety


# Create your views here.

def all_heroes(request):
    heroes = HeroVariety.objects.all()
    return render(request, 'myApp/all_heroes.html', {"heroes": heroes})


def hero_detail(request, hero_id):
    hero = get_object_or_404(HeroVariety, pk=hero_id)
    return render(request, 'myApp/hero_details.html', {'hero': hero})
