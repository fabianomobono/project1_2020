from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:query>", views.page, name="page"),
    path("results", views.search, name="results"),
    path("create_page", views.create, name="create_page"),
    path("edit_page", views.edit, name="edit"),
    path("random", views.random, name='random')
]
