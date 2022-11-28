from django.urls import path 
from .views import accounts_views
urlpatterns = [
    path("",accounts_views ),
]