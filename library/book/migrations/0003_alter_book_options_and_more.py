# Generated by Django 5.1 on 2024-08-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_author_price_book_author_book_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-published_at']},
        ),
        migrations.RemoveIndex(
            model_name='book',
            name='book_book_publish_314e8c_idx',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='created',
            new_name='published_at',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publish',
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['-published_at'], name='book_book_publish_731b0b_idx'),
        ),
    ]
