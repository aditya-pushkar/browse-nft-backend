from django.urls import path

from .views import (
    users
)

app_name = 'user'

urlpatterns = [
    path('all/', users, name='users'),
]
