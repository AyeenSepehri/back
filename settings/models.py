from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=999,verbose_name='title')
    Keywords = models.TextField(verbose_name='Keywords')
    descriptions = models.TextField(verbose_name='descriptions')
    image = models.ImageField(upload_to='imagesSettings',verbose_name='image')
    paymentـpercentage = models.IntegerField(default=0,verbose_name='paymen percentage')
    phone = models.CharField(max_length=999,verbose_name='phone')
    email = models.EmailField(max_length=999,verbose_name='email')
    about_us = models.TextField(verbose_name='about us')
    sms_username = models.CharField(max_length=999,blank=True,null=True,verbose_name='sms username')
    sms_phone = models.CharField(max_length=999,blank=True,null=True,verbose_name='sms phone')
    sms_password = models.CharField(max_length=999,blank=True,null=True,verbose_name='sms password')
    address = models.TextField(verbose_name='address')

    def __str__(self):
        return self.title