from django.contrib import admin

from posts.models import Post, Category, Comment


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Post)
