from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('heroes/', views.heroes, name='heroes'),
    path('new_hero/', views.new_hero, name='new_hero'),
    # path('members/details/<int:id>', views.details, name='details'),
]