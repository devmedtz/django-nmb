from django.urls import path

from .import views

app_name = 'example'

urlpatterns = [
    path('test-api/', views.get_sessionID, name='test_api'),
]