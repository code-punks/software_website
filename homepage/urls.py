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
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^edit_profile/(?P<pk>[\-\w]+)/$',views.edit_user,name='edit_profile'),
	url(r'^assign_rfid/$', views.assign_rfid, name='assign_rfid'),
	url(r'^make_payment/$',views.make_payment, name='make_payment')
	#url(r'^api/newentry$', views.new_entry, name = 'new_entry'),
	]
