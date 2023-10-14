from django.urls import path
from ablog import views
app_name = 'ablog'

urlpatterns = [
    path('',views.blog_list,name='blog_list')
]