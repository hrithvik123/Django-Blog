from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views



urlpatterns = [
    path('test/', views.PostView.as_view(), name='api-test'),
    path('test/token', obtain_auth_token, name='obtain-token'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
