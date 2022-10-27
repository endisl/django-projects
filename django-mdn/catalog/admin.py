from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language

admin.site.register(Genre)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
