from django.contrib import admin
from django.urls import path, include
import reviews.views

urlpatterns = [
    path('', reviews.views.index),
    path('create/<book_id>', reviews.views.create_review, name="create_review"),
    path('update_review/<reviewid>', reviews.views.update_review, name='update_review'),
    path('delete_review/<reviewid>', reviews.views.delete_review, name='delete_review')
]