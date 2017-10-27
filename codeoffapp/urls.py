from django.conf.urls import include,url
#from django.contrib.auth.views import login,logout, password_reset, password_reset_done, password_reset_confirm,password_reset_complete
from . import views



urlpatterns = [
   	url(r'^register',views.register,name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^view_profile/$', views.view_profile, name='view_profile'),
    ]