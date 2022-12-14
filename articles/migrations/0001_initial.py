# Generated by Django 4.0.6 on 2022-07-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, verbose_name='name')),
                ('image', models.ImageField(upload_to='imagesCategories', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='title')),
                ('slug', models.SlugField(max_length=999, verbose_name='slug')),
                ('image', models.ImageField(upload_to='imagesArticles')),
                ('descriptions', models.TextField(verbose_name='descriptions')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('categories', models.ManyToManyField(to='articles.categories', verbose_name='categories')),
            ],
        ),
    ]
