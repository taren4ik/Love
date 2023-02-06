from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.index, name='index'),
    path("category/<slug:slug>/", views.category_profiles,
         name="category_profiles"),
    path("city/<slug:slug>/", views.city, name="city_list"),
    path('profiles/<int:profile_id>/', views.profile_detail,
         name='profile_detail'),

    path("profiles/<int:profile_id>/delete/", views.profile_delete,
         name="profile_delete"),
    path(
        "profiles/<int:profile_id>/comment/", views.add_comment,
        name="add_comment"
    ),
    path(
        "profiles/<int:profile_id>/message/", views.send_message,
        name="send_message"
    ),
    path("message/", views.index_message, name="index_message"),
    path("follow/", views.follow_index, name="follow_index"),
    path(
        "profiles/<int:profile_id>/follow/",
        views.profile_follow,
        name="profile_follow"
    ),
    path(
        "profiles/<int:profile_id>/unfollow/",
        views.profile_unfollow,
        name="profile_unfollow"
    ),

]
