from django.urls import path
from . import views

app_name = "blogApp"

urlpatterns = [
    path("post/add/", views.add_post, name="add_post"),
    path("post/list/", views.list_posts, name="list_posts"),
    path("post/detail/<post_id>/", views.post_detail, name="post_detail"),
    path("post/update/<post_id>/", views.update_post, name="update_post"),
    path("post/delete/<post_id>/", views.delete_post, name="delete_post"),
    path("post/search/<post_id>/", views.search_post, name="search_post"),

]