from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
    path('', books.views.index, name='home'),
    path('create/', books.views.create_book, name='create_book'),
    path('create_author', books.views.create_author, name='create_author'),
    path('update_book/<dataid>', books.views.update_book, name='update_book_route'),
    path('update_author/<dataid>', books.views.update_author, name='update_author_route'),
    path('delete_book/<dataid>', books.views.delete_book, name='delete_book_route'),
    path('delete_author/<dataid>', books.views.delete_author, name='delete_author_route')
]