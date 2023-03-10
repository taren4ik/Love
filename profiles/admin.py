from django.contrib import admin

from .models import Category, Comment, Follow, Message, Photo, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'phone', 'city', 'year', 'sex',
                    'category')
    search_fields = ('phone',)
    list_filter = ('city', 'year', 'sex', 'category')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ('author', 'user')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Photo)
