from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('actors/', views.show_all_actors),
    path('actors/<int:id_actor>', views.show_one_actor, name='url_actors'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='url_name'),
]
