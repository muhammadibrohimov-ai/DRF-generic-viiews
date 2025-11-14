from django.contrib import admin
from .models import Book, Author

# Register your models here.


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'year', 'country']
    search_fields = ['fullname', 'year', 'country']
    list_display_links = ['fullname', 'year', 'country']
    list_filter = ['year', 'country']
    

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'year', 'price']
    list_display_links = ['name', 'author', 'year', 'price']
    search_fields = ['name', 'author', 'year', 'price']
    list_filter = ['author', 'year', 'price']