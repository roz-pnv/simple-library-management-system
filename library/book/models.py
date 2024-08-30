from django.db import models
from django.utils import timezone


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


    #Date field
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Choice field
    category = models.CharField(
        max_length=2, 
        choices=Category.choices, 
        default=Category.Biography
    )

    class  Meta:
        ordering = [
            '-publish',
        ]
        indexes = [
            models.Index(fields=['-publish',]),
        ]


    def __str__ (self):
        return self.name