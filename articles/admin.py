from django.contrib import admin
from . import models


class CommentInLine(admin.TabularInline):
    model = models.Comment



@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = ('title', 'content', 'date', 'author')
    list_filter = ('date', 'author')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'date'
    ordering = ('date', 'title')


admin.site.register(models.Comment)


