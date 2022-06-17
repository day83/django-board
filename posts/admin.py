from django.contrib import admin

from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'to_post', 'user_name', 'date_time')
    list_filter = ('to_post', 'user_name')

    def content(self, object):
        return object.content

    content.short_description = 'PROPERTY X'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
