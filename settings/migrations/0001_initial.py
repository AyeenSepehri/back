# Generated by Django 4.0.6 on 2022-07-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=999, verbose_name='title')),
                ('Keywords', models.TextField(verbose_name='Keywords')),
                ('descriptions', models.TextField(verbose_name='descriptions')),
                ('image', models.ImageField(upload_to='imagesSettings', verbose_name='image')),
                ('paymentـpercentage', models.IntegerField(default=0, verbose_name='paymen percentage')),
                ('phone', models.CharField(max_length=999, verbose_name='phone')),
                ('email', models.EmailField(max_length=999, verbose_name='email')),
                ('about_us', models.TextField(verbose_name='about us')),
                ('address', models.TextField(verbose_name='address')),
            ],
        ),
    ]
