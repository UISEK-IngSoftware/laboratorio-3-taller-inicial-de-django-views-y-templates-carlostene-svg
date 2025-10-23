from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('pokemon/<str:pokemon>',views.pokemon_detail, name='pokemon_details'),
]
