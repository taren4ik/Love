from django.contrib import admin

from .models import Follow, Category, User


admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Category)
