from django.conf.urls import url,include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('profiles', views.ProfileView)
router.register('entries', views.EntryView)
router.register('exits', views.ExitView)


urlpatterns = [
    url('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]