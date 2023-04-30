from django.urls import path, include
from rest_framework import routers

from mailer.api.v1.views import GroupUserViewSet, EmailTemplateReadOnly

router = routers.DefaultRouter()

router.register('groups-users', GroupUserViewSet, basename='groups-users')
router.register('email-template', EmailTemplateReadOnly, basename='email-template')

urlpatterns = [
    path('', include(router.urls)),
]
