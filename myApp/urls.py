from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_heroes, name='all_heroes'),
    path('<int:hero_id>/', views.hero_detail, name='hero_detail')
]