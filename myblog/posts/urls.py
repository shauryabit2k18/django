from django.urls import path
from posts.views import posts_list , posts_detail , posts_create , posts_update

urlpatterns = [
    path('' , posts_list),
    path('create/' , posts_create),
    path('<slug>/update/' , posts_update),
    path('<slug>/' , posts_detail),
]