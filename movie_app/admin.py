from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['-rating', 'name']
    list_per_page = 5

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 61:
            return 'Зачем это смотреть'
        if mov.rating < 70:
            return 'Что интересное'
        if mov.rating <= 85:
            return 'Крутой фильм'
        else:
            return 'Это ТОП!!!'
