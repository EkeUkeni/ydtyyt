"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    # path("", views.current_datetime, name="index"),
    # path("all-list/", views.get_todo, name="todo-list"),
    path("", views.get_todos, name="todo-list"),
    path("todo/<str:pk>/", views.get_todo, name="todo-detail"),
    path("create-todo/", views.create_todo, name="todo-create"),
    path("update-todo/<int:pk>/", views.update_todo, name="todo-update"),
    path("delete-todo/<int:pk>/", views.delete_todo, name="todo-delete"),
    path("admin/", admin.site.urls),
]
