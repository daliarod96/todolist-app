from django.contrib import admin
from .models import ToDoList, Item # add our ToDolist, Item models to the admin dashboard
# Register your models here.

admin.site.register(ToDoList) # register our to do list
admin.site.register(Item) # register our to do list