from django.urls import path
from .views import CreateBook, DetailBook, DeleteBook, UpdateBook


urlpatterns = [
    path("create", CreateBook.as_view(), name="create_book"),
    path("details/<pk>", DetailBook.as_view(), name="detail_book"),
    path("delete/<pk>", DeleteBook.as_view(), name="delete_book"),
    path("update/<pk>", UpdateBook.as_view(), name="update_book"),

]