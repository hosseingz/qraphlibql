from django.contrib import admin
from .models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'age']
    list_filter = ['date_of_birth', 'date_of_death']
    search_fields = ['first_name', 'last_name']
    ordering = ['date_of_birth']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'page_count']
    list_filter = ['author', 'published_date', 'genre']
    search_fields = ['title', 'author__first_name', 'author__last_name']
    ordering = ['published_date']
    date_hierarchy = 'published_date'
