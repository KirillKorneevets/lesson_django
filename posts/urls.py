from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_posts, name='posts'),
    path("get/<int:user_id>/", views.get_posts, name='get_posts'),
]