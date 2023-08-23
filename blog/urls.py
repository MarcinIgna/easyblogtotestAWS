from django.urls import path
from blog.views.main_view import main
from blog.views.post_view import PostView

app_name = "blog"
urlpatterns = [
    path("", main, name="main"),
    path("new_post/", PostView.new_post, name="new_post"),
]
