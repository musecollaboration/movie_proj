from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('actors/', views.ShowAllActors.as_view(), name='actors'),
    path('actors/<int:pk>', views.ShowOneActor.as_view(), name='url_actors'),
    path('directors/', views.ShowAllDirectors.as_view(), name='directors'),
    path('directors/<int:pk>', views.ShowOneDirector.as_view(), name='url_directors'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='url_name'),
]
