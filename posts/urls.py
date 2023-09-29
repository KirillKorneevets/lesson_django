from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_user, name='create_posts'),
    path("get/<int:user_id>/", views.get_user, name='get_posts'),
    path("get/", views.get_user, name='all_posts'),
    path("update/<int:user_id>/", views.update_user),
    path("delete/<int:user_id>/", views.delete_user)
]