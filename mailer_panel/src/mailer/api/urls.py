from django.urls import path, include

urlpatterns = [
    path('v1/', include('mailer.api.v1.urls')),
]
