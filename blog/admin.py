from django.contrib import admin
from .models import BlgPost, BlgCategory

# Register your models here.

@admin.register(BlgPost)
class BlgPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_tag', 'category')
    list_filter = ('post_date', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'post_date'
    ordering = ('post_date',)


@admin.register(BlgCategory)
class BlgCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
