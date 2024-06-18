from django.shortcuts import render, get_object_or_404
from .models import HeroVariety, CountryPopularIn
from .forms import HeroVarietyForm


# Create your views here.

def all_heroes(request):
    heroes = HeroVariety.objects.all()
    return render(request, 'myApp/all_heroes.html', {"heroes": heroes})


def hero_detail(request, hero_id):
    hero = get_object_or_404(HeroVariety, pk=hero_id)
    return render(request, 'myApp/hero_details.html', {'hero': hero})


def hero_countries_view(request):
    countries = None
    if request.method == "POST":
        form = HeroVarietyForm(request.POST)
        if form.is_valid():
            hero_variety = form.cleaned_data["hero_variety"]
            countries = CountryPopularIn.objects.filter(heroes_popular=hero_variety)
    else:
        form = HeroVarietyForm()

    return render(request, "myApp/hero_countries.html", {'countries': countries, 'form': form})
