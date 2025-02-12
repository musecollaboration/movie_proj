from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('actors/', views.show_all_actors, name='actors'),
    path('actors/<int:id_actor>', views.show_one_actor, name='url_actors'),
    path('directors/', views.show_all_directors, name='directors'),
    path('directors/<int:id_director>', views.show_one_director, name='url_directors'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='url_name'),
]
