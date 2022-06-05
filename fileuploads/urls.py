from django.contrib import admin
from django.urls import path

from document import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('admin/', admin.site.urls),
]
