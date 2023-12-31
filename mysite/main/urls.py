from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name = "home"),
path("<int:id>", views.index, name="index"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
path("logout/", views.logout_view, name="view"),
path("view/", views.delete_list, name="delete_list"),
]