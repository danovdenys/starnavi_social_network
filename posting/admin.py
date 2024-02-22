from django.contrib import admin
from posting.models import Like, Post


class LikeAdmin(admin.ModelAdmin):
    pass

class LikeInline(admin.TabularInline):
    model = Like
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [LikeInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)