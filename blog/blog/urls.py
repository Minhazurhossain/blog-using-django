
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('account/',include('login.urls')),
    path('blog/',include('ablog.urls')),
    path('', views.Index , name ='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)