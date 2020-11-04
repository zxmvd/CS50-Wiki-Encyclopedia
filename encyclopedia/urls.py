from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("random", views.randomPage, name="random"),
    path("<str:title>/edit", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
    
]
