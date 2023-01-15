from django.contrib import admin

from .models import Follow, Category, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'city', 'year', 'sex', 'category')
    search_fields = ('phone',)
    list_filter = ('city', 'year', 'sex', 'category')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ('author', 'user')
    empty_value_display = '-пусто-'


admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Category)
