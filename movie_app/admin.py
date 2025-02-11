from django.contrib import admin, messages
from .models import Movie, Director, Actor
from django.db.models import QuerySet


admin.site.register(Director)
admin.site.register(Actor)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('<40 до 59', 'Средний'),
            ('<60 до 79', 'Высокий'),
            ('>=80', 'Топовый'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == '<40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == '<60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # readonly_fields = ['budget']
    # exclude = ['slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status']
    list_editable = ['rating', 'director', 'budget']
    ordering = ['-rating', 'name']
    list_per_page = 6
    actions = ['set_dollars', 'set_euro', 'set_rub']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    filter_horizontal = ['actors']

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

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей',
        )

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EURO)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей',
            messages.ERROR,
        )

    @admin.action(description='Установить валюту в рубли')
    def set_rub(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.RUB)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей',
        )
