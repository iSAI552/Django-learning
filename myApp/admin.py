from django.contrib import admin
from .models import HeroVariety, HeroReview, SpecialPower, CountryPopularIn


# Register your models here.
class HeroReviewInline(admin.TabularInline):
    model = HeroReview
    extra = 2


class HeroVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
    inlines = [HeroReviewInline]


class CountryPopularAdmin(admin.ModelAdmin):
    list_display = ("name", "continent")
    filter_horizontal = ("heroes_popular",)


class SpecialPowerAdmin(admin.ModelAdmin):
    list_display = ("hero",)


admin.site.register(HeroVariety, HeroVarietyAdmin)
admin.site.register(SpecialPower, SpecialPowerAdmin)
admin.site.register(CountryPopularIn, CountryPopularAdmin)
