# Generated by Django 5.1 on 2024-09-01 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='updated_at',
        ),
    ]