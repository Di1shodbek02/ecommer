from django.contrib import admin

from accounts.views import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
