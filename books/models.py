from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.TextField(blank=False, max_length=255)
    last_name = models.TextField(blank=False, max_length=255)
    date_of_birth = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + "Hey"


