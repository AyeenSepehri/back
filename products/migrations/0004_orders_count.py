# Generated by Django 4.0.6 on 2022-07-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_orders_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='count',
            field=models.IntegerField(default=0, verbose_name='count'),
        ),
    ]
