from django.urls import path
from . import views, comments

urlpatterns = [
    path("get/<int:user_id>/", views.get_user, name='get_posts'),
    path("get/", views.get_user, name='all_posts'),
    path("update/<int:user_id>/", views.update_user),
    path("delete/<int:user_id>/", views.delete_user),
    path("create_comm/", comments.create_comments),
    path("create/", comments.create_posts, name='create_posts'),
    path("get_comment/<int:post_id>/", comments.get_comment),
    ]