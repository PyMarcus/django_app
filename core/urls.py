from django.urls import path
from .views import index, another_route


urlpatterns = [
    path('', index),
    path('another', another_route)
]
