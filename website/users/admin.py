from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)


# admin.site.register(User, UserAdmin)
