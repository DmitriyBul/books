from django.contrib import admin


# Register your models here.
from store.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_editable = list_display
    list_display_links = None
