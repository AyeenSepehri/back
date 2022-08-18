from django.contrib.auth.base_user import BaseUserManager
from extensions.optimization import photo_optimization
from django.contrib.auth.models import AbstractUser
from django.db import models


class manager(BaseUserManager):
    def _create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(phone, password, **extra_fields)
        return user


#  user model with 'phone' as username
class Userperson(AbstractUser):
    username = None
    fullname = models.CharField(blank=True, null=True, max_length=100, verbose_name="Full Name")
    phone = models.CharField(blank=True, null=True, max_length=20, verbose_name="Phone", unique=True)
    image = models.ImageField(blank=True, null=True, upload_to="userphoto/", verbose_name="User Photo")
    address = models.TextField(null=True, blank=True, verbose_name='Address')
    status = models.BooleanField(default=False, blank=True, null=True, verbose_name='Status')
    is_superuser = models.BooleanField(default=False, blank=True, null=True, verbose_name='Is Super User')
    wallet = models.IntegerField(default=0)
    objects = manager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['fullname']

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Userperson, self).save(*args, **kwargs)

    def __call__(self):
        return f'{self.fullname}'

    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return f'{self.fullname}'



class Codes(models.Model):
    user = models.ForeignKey(Userperson,on_delete=models.CASCADE,blank=True,null=True,verbose_name='user')
    code = models.CharField(max_length=999,verbose_name='code')

    def __str__(self):
        return self.code