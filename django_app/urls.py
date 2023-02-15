from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]


handler404 = views.error404
