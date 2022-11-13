from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'
urlpatterns = [
    # post views

    path('', views.post_list, name='post_list'),

    # path('feed/', LatestPostsFeed(), name='post_feed'),  # Must be before 'post_detail' !!!

    path('<slug:xslug>/', views.post_detail, name='post_detail'),

    path('<int:post_id>/share/', views.post_share, name='post_share'),

    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # ------------------------------------------------------

    path('feed/page/', LatestPostsFeed(), name='post_feed'),  # Now can be in any order !!!

    # path('yl', LatestPostsFeed(), name='pyl'),
    # ------------------------------------------------------f
    path('search/x/', views.post_search, name='post_search'),

]
