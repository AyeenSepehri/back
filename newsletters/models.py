from extensions.date import django_jalali
from django.db import models


class Newsletters(models.Model):
    email = models.EmailField(max_length=999,verbose_name='email')
    date = models.DateTimeField(auto_now_add=True,verbose_name='date')

    def jdate(self):
        return django_jalali(self.date)

    def __str__(self):
        return self.email