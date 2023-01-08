from django.urls import path
from . import views
app_name = 'profiles'
urlpatterns = [
    path('profile/<int:profile_id>/', views.profile_detail, name='profiles'),
    path('profile/', views.profile),
    path('city/', views.city),
]
