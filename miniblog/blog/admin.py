from django.contrib import admin

from .models import Blog, Blogger, Comment

admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Comment)


class BlogCommentsInline(admin.TabularInline):
    model = Comment
    max_num = 0


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentsInline]
