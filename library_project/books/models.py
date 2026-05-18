from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio  = models.TextField(blank=True)  # blank=True means optional

    def __str__(self):
        return self.name  # shows in Django admin nicely


class Book(models.Model):
    title       = models.CharField(max_length=300)
    author      = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # ForeignKey = one Author can have MANY books (one-to-many relationship)
    published   = models.DateField()
    isbn        = models.CharField(max_length=13, unique=True)
    available   = models.BooleanField(default=True)

    def __str__(self):
        return self.title