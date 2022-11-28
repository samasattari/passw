from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import user 

# admin.site.register(user)
class UserAd (UserAdmin):
    model=user
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('buy',)}),
    )

admin.site.register(user, UserAd)