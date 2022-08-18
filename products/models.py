from extensions.optimization import photo_optimization
from usersmodel.models import Userperson
from extensions.date import django_jalali
from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=999,verbose_name='title')
    slug = models.SlugField(max_length=999,verbose_name='slug')
    image = models.ImageField(upload_to='imagesProducts',blank=True,null=True,verbose_name='image')
    image1 = models.ImageField(upload_to='imagesProducts',blank=True,null=True,verbose_name='image1')
    image2 = models.ImageField(upload_to='imagesProducts',blank=True,null=True,verbose_name='image2')
    image3 = models.ImageField(upload_to='imagesProducts',blank=True,null=True,verbose_name='image3')
    price = models.IntegerField(default=0,verbose_name='price')
    quality = models.IntegerField(default=0,verbose_name='quality')
    inventory = models.IntegerField(default=0,verbose_name='inventory')
    category = models.ForeignKey('Categories',on_delete=models.CASCADE,verbose_name='category')
    date = models.DateTimeField(auto_now_add=True,verbose_name='date')
    descriptions = models.TextField(verbose_name='descriptions')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        photo_optimization(self.image1)
        photo_optimization(self.image2)
        photo_optimization(self.image3)
        super(Products, self).save(*args, **kwargs)

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=999,unique=True,verbose_name='name')
    icon_code = models.CharField(max_length=999,verbose_name='icone code')
    image = models.ImageField(upload_to='imagesCategories',verbose_name='image')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,blank=True,null=True,verbose_name='user')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=True,null=True,verbose_name='product')
    comment = models.TextField(verbose_name='comment')
    status = models.BooleanField(default=False,verbose_name='status')
    date = models.DateTimeField(auto_now_add=True,verbose_name='date')

    def jdate(self):
        return django_jalali(self.date)


class Likes(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,blank=True,null=True,verbose_name='user')
    like = models.BooleanField(default=False,verbose_name='like and dis like')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=True,null=True,verbose_name='product')

    def __str__(self):
        return self.like

class Sliders(models.Model):
    image = models.ImageField(upload_to='imagesSliders',verbose_name='image')
    url = models.URLField(verbose_name='url')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Sliders, self).save(*args, **kwargs)

    def __str__(self):
        return self.image.name



class Carts(models.Model):
    customer = models.ForeignKey(Userperson,on_delete=models.CASCADE,verbose_name='user')
    payment_status = models.BooleanField(default=False,verbose_name='payment status')
    payment_date = models.DateTimeField(auto_created=True,verbose_name='payment date')



class Orders(models.Model):
    cart = models.ForeignKey(Carts,on_delete=models.CASCADE,blank=True,null=True,verbose_name='cart')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=True,null=True,verbose_name='product')
    title = models.CharField(max_length=999,verbose_name='title')
    descriptions = models.TextField(verbose_name='descriptions')
    price = models.IntegerField(default=0,verbose_name='price')
    count = models.IntegerField(default=0,verbose_name='count')
    tracking_code = models.CharField(max_length=999, blank=True,null=True,verbose_name='tracking code')
    payment_status = models.BooleanField(default=False,verbose_name='payment status')
    payment_date = models.DateTimeField(auto_created=True,verbose_name='payment date')

    def __str__(self):
        return self.title




class Trackings(models.Model):
    cart = models.ForeignKey(Carts,on_delete=models.CASCADE,verbose_name='cart')
    code = models.CharField(max_length=999,verbose_name='code')
    status = models.CharField(max_length=999,verbose_name='status')

    def orders(self):
        orders = []
        for order in Orders.objects.filter(tracking_code=self.code,payment_status=True).all():
            orders.append({'product_id': order.product.id,'title': order.title,'descriptions': order.descriptions,'count': order.count,'price': order.price})

        return orders

    def __str__(self):
        return self.code