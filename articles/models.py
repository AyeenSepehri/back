from extensions.optimization import photo_optimization
from extensions.date import django_jalali
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=999,verbose_name='title')
    slug = models.SlugField(max_length=999,verbose_name='slug')
    image = models.ImageField(upload_to='imagesArticles')
    descriptions = models.TextField(verbose_name='descriptions')
    categories = models.ManyToManyField('Categories',verbose_name='categories')
    date = models.DateTimeField(auto_now_add=True,verbose_name='date')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Articles, self).save(*args, **kwargs)


    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return self.title


class Categories(models.Model):
    name = models.CharField(max_length=999,verbose_name='name')
    image = models.ImageField(upload_to='imagesCategories',verbose_name='image')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Categories, self).save(*args, **kwargs)



    def __str__(self):
        return self.name