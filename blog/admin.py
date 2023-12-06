from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'id', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'id')
    # ordering = ('created_date',)
    search_fields = ('title', 'content')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
