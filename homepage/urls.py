from django.conf.urls import url,include
from . import views
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	]