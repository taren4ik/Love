from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:profile_id>/', views.profile_detail,
         name='profile_detail'),
    path('city/', views.city),
]
