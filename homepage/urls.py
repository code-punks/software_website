from django.conf.urls import url,include
from . import views
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', auth_views.login,{'template_name': 'homepage/login2.html'}),
	url(r'^logout/$', auth_views.logout,{'template_name': 'homepage/logged_out.html'}),
	url(r'^register/', views.register),
	]
