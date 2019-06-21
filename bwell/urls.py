from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from mortality import views


router = routers.DefaultRouter()
router.register(r'cause', views.CauseViewSet)
# these urls are a little confusing because I couldn't exactly decide on the name of the app and the name of the view.
# I settled on this structure because I figured if this were a real application, we would want an entire app
# dedicated to mortality data, doing whatever we needed with said data, and a viewset dedicated to just these
# leading causes of death.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
