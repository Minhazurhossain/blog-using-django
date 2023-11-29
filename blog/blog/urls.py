
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('account/',include('login.urls')),
    path('blog/',include('ablog.urls')),
    path('', views.Index , name ='index'),
]
