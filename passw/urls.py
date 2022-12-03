from django.urls import path 
from .views import password_list_view, password_form_view


urlpatterns = [
    path("list", password_list_view, name="passwordslist"),
    path("form", password_form_view , name = 'passwordsform' )
]