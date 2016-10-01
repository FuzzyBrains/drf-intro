from .views import TalkViewSet

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'talks', TalkViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]