from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:profole_id>/', views.profile_detail, name='profile'),
    path('profile/', views.profile),
    path('city/', views.city),
]
