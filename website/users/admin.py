from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email", "username")


# admin.site.register(User, UserAdmin)
