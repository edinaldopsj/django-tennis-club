from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('heroes/', views.heroes, name='heroes'),
    path('new_hero/', views.new_hero, name='new_hero'),
    path('add_hero/', views.add_hero, name='add_hero'),
    path('delete_hero/<int:id>', views.delete_hero, name='delete_hero'),
    path('hero_detail/<int:id>', views.hero_detail, name='hero_detail'),
    path('update_hero/<int:id>', views.update_hero, name='update_hero'),
    path('update_hero_data/<int:id>', views.update_hero_data, name='update_hero_data'),
]