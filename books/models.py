from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'category'

class Tags(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'tags'

class Author(models.Model):
    first_name = models.TextField(blank=False, max_length=255)
    last_name = models.TextField(blank=False, max_length=255)
    date_of_birth = models.DateField(blank=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    author = models.ManyToManyField(Author)
    owner = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title