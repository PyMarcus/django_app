from django.urls import path
from .views import index, another_route
from .views import product


urlpatterns = [
    path('', index, name='index'),
    path('another', another_route, name='another'),
    path('product/<int:id>', product, name='product')
]
