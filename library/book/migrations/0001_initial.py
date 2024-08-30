# Generated by Django 5.1 on 2024-08-30 21:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('B', 'Biography'), ('C', 'Childrens fiction'), ('F', 'Fantasy'), ('H', 'Horror'), ('I', 'Inspirational'), ('M', 'Mystery'), ('R', 'Romance'), ('V', 'Young adult')], default='B', max_length=2)),
            ],
            options={
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='book_book_publish_314e8c_idx')],
            },
        ),
    ]