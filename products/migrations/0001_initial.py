# Generated by Django 4.0.6 on 2022-07-27 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.BooleanField(default=False, verbose_name='payment status')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='payment date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=999, unique=True, verbose_name='name')),
                ('icon_code', models.CharField(max_length=999, verbose_name='icone code')),
                ('image', models.ImageField(upload_to='imagesCategories', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imagesSliders', verbose_name='image')),
                ('url', models.URLField(verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='title')),
                ('slug', models.SlugField(max_length=999, verbose_name='slug')),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagesProducts', verbose_name='image')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='imagesProducts', verbose_name='image1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='imagesProducts', verbose_name='image2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='imagesProducts', verbose_name='image3')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('quality', models.IntegerField(default=0, verbose_name='quality')),
                ('inventory', models.IntegerField(default=0, verbose_name='inventory')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('descriptions', models.TextField(verbose_name='descriptions')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories', verbose_name='category')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='title')),
                ('descriptions', models.TextField(verbose_name='descriptions')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('payment_status', models.BooleanField(default=False, verbose_name='payment status')),
                ('payment_date', models.DateTimeField(auto_now=True, verbose_name='payment date')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.carts', verbose_name='cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='product')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False, verbose_name='like and dis like')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]