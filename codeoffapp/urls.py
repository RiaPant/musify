from django.conf.urls import include,url
from django.contrib.auth.views import logout
from . import views




urlpatterns = [
   	url(r'^register',views.register,name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^view_profile/$', views.view_profile, name='view_profile'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/',logout,{'template_name': 'codeoffapp/login.html'}, name='logout'),
    ]