from django.contrib import admin
# from .models import TodoList
from todo.models import TodoList

# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title','preview','created_at', 'updated_at')
    list_display_links = ('preview',)
    list_filter = ['complete','created_at', 'updated_at']
    date_hierarchy = "created_at"
    search_fields = ['title', 'description']

admin.site.register(TodoList, TodoListAdmin)
# admin.site.register(TodoList)
