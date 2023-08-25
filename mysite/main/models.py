from django.db import models # a model is like a table
from django.contrib.auth.models import User
# Create your models here.

# ToDoList
class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

# Item for items that go in the ToDoList
class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()


	def __str__(self):
		return self.text 