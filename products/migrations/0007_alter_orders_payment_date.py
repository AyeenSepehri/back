# Generated by Django 4.0.6 on 2022-07-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_orders_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payment_date',
            field=models.DateTimeField(auto_created=True, verbose_name='payment date'),
        ),
    ]
