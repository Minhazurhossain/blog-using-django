from django.urls import path
from login import views
app_name = 'login'

urlpatterns = [
   path('signup/',views.sign_up,name ='signup'), 
   path('login/',views.login_page,name='login'),
   path('logout/',views.logout_user,name='logout'),
]