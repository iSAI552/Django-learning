from django import forms
from .models import HeroVariety


class HeroVarietyForm(forms.Form):
    hero_variety = forms.ModelChoiceField(queryset=HeroVariety.objects.all(), label="Select the hero variety")
