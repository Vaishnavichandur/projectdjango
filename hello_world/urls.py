from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('api/hello/', HelloWorldView.as_view(), name='hello-world'),  # REST API endpoint
]
