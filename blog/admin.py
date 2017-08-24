from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
	fields = ['author','image', 'title', 'text', 'created_date', 'published_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

		