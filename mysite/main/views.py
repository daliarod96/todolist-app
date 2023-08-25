from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib.auth import logout
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
	ls = ToDoList.objects.get(id=id)
	if response.method== "POST":
		#print(response.POST)
		# save changes to your list (checked items, added items)
		if response.POST.get("save"):
			for item in ls.item_set.all(): 
				if response.POST.get("c" + str(item.id)) == "clicked":
					item.complete = True
				else:
					item.complete = False
				item.save()
		elif response.POST.get("newItem"):
			txt = response.POST.get("new")
			if len(txt) > 2:
				ls.item_set.create(text=txt, complete=False)
			else:
				print("invalid")

	return render(response, "main/list.html", {"ls": ls}) # show template

def delete_list(response,id):
	ls = ToDoList.objects.get(id=id)
	if response.method=="POST":
		if response.POST.get("delete"):
			ls.delete()
	return render(request, 'main/view.html', {})


# Create your homepage here.
def home(request):
	template_name = 'main/home.html'
	extended_template = 'main/base.html'

	if request.user.is_authenticated:
		extended_template = 'main/base_login.html'
	return render(request, template_name, {'extended_template': extended_template})


def logout_view(request):
    logout(request)
    # Redirect to a success page.

    return render(request, 'main/logout.html', {})


def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t= ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()

	return render(response, "main/create.html", {"form": form}) # show template


def view(response):
	return render(response, "main/view.html", {})
