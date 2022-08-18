from extensions.date import django_jalali
from usersmodel.models import Userperson
from django.db import models

class Tikets(models.Model):
    customer = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='customer',related_name='customer_db')
    support = models.ForeignKey(Userperson,default=1,on_delete=models.CASCADE,verbose_name='support')
    status = models.BooleanField(default=False,verbose_name='status')
    date = models.DateTimeField(auto_now_add=True,verbose_name='date')

    def jdate(self):
        return django_jalali(self.date)

class Messages(models.Model):
    roles = (
        ('support','support'),
        ('customer','customer'),
    )
    tiket = models.ForeignKey(Tikets,on_delete=models.CASCADE,verbose_name='tiket')
    text = models.TextField(blank=True,null=True,verbose_name='text')
    file = models.FileField(blank=True,null=True,upload_to='filesMessages',verbose_name='file')
    role = models.CharField(choices=roles,max_length=60,blank=True,null=True,verbose_name='role')
    date = models.DateTimeField(auto_now_add=True,verbose_name='date')

    def jdate(self):
        return django_jalali(self.date)