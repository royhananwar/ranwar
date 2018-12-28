from django.urls import path, include

from .views import router_blog


urlpatterns = [
    path('', include(router_blog.urls))
]