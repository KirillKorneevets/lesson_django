from django.urls import path
from posts.views import user, comments, wallet



urlpatterns = [
    path("create_user/", user.UserViews.as_view()),
    path("get/<int:user_id>/", user.UserViews.as_view()),
    path("update/<int:user_id>/", user.UserViews.as_view()),
    path("delete/<int:user_id>/", user.UserViews.as_view()),
    path("create_posts/", comments.create_posts),
    path("create_comments/", comments.create_comments),
    path("get_comment/<int:post_id>/", comments.get_comment),
    path("transaction/", wallet.post),
    ]