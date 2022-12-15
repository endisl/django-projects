from django.contrib import admin

from .models import Blog, Blogger, Comment

admin.site.register(Blogger)
admin.site.register(Comment)


class BlogCommentsInline(admin.TabularInline):
    model = Comment
    max_num = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    inlines = [BlogCommentsInline]
