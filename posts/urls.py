from django.urls import path
from posts.views import user, comments, wallet, detail_user



urlpatterns = [
    path("create_user/", user.UserViews.as_view()),
    path("get/<int:user_id>/", user.UserViews.as_view()),
    path("get/", user.UserViews.as_view()),
    path("update/<int:user_id>/", user.UserViews.as_view()),
    path("delete/<int:user_id>/", user.UserViews.as_view()),

    path("create_posts/", comments.create_posts),
    path("create_comments/", comments.create_comments),
    path("get_comment/<int:post_id>/", comments.get_comment),

    path("transaction/", wallet.post),

    path("registration-users/", detail_user.RegistrationView.as_view(), name='registration-users'),
    path("get_users/", detail_user.DetailUser.as_view(), name='get_users'),
    path("edit_user/", detail_user.СhangeUser.as_view(), name='edit_user'),


    ]

