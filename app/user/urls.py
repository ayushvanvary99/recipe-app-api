"""
Url mappings for the user API
"""
from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserview.as_view(), name='create'),
    path('token/', views.CreateTokenview.as_view(), name='token'),

]
