from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__ (self):
        return self.name


class Price(models.Model):
    price = models.BigIntegerField(max_length=None)

    def __str__ (self):
        return self.price


class Book(models.Model):
    class Category(models.TextChoices):
        Biography = 'B', 'Biography'
        Childrens_fiction = 'C', 'Childrens fiction'
        Fantasy  = 'F', 'Fantasy'
        Horror = 'H', 'Horror'
        Inspirational  = 'I', 'Inspirational'
        Mystery = 'M', 'Mystery'
        Romance = 'R', 'Romance'
        Young_adult = 'V', 'Young adult'


    #Data field
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    #Relation field
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, 
        null=True,
        related_name='author_books',
    )
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE, 
        null=True,
        related_name='book_price',
    )

    #Date field
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Choice field
    category = models.CharField(
        max_length=2, 
        choices=Category.choices, 
        default=Category.Biography
    )

    class  Meta:
        ordering = [
            '-published_at',
        ]
        indexes = [
            models.Index(fields=['-published_at',]),
        ]


    def __str__ (self):
        return self.name