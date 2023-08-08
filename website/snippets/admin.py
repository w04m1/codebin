from django.contrib import admin

from .models import Snippet, Comment, Reaction

# Register your models here.


class SnippetAdmin(admin.ModelAdmin):
    list_display = ("title", "language", "published", "public", "owner")
    list_filter = ("language", "published", "public")
    search_fields = ("title", "description", "code")
    ordering = ("-published",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("snippet", "owner", "published")
    list_filter = ("published",)
    search_fields = ("text",)
    ordering = ("-published",)


class ReactionAdmin(admin.ModelAdmin):
    list_display = ("snippet", "owner", "reaction")
    list_filter = ("reaction",)
    ordering = ("reaction",)


admin.site.register(Reaction, ReactionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Snippet, SnippetAdmin)
