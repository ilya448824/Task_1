from django.contrib import admin
from  .models import OnlineShop
# Register your models here.

# класс для отображения панели администрирования
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'creation_time','auction']
    list_filter = ['auction', 'creation_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможнось торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Добавить возможнось торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
# отображение нашу модель в панель администрирования
admin.site.register(OnlineShop, OnlineShopAdmin)
