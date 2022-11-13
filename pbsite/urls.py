from django.urls import path, include
from django.contrib import admin
# from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [

    path('admin/', admin.site.urls),  # FIRST LINE !!!

    path('', include('blog.urls')),

    # path('blog/', include('blog.urls', namespace='blog')),
    # path('blog/', include('blog.urls')),

    path('sitemap.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
