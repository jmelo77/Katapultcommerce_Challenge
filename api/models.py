import re
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


# creating a validator function
def validate_nit(value):
    pattern = r'^[0-9]{9}\-[0-9]{1}'
    if(re.search(pattern, value)):
        return value
    else:
        raise ValidationError("Invalid NIT")

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


# Create your models here.
# User model.
class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email 


class Provider(models.Model):
    provider_name = models.CharField(max_length=128)
    nit_provider = models.CharField(max_length=64, validators =[validate_nit])
    contact_name = models.CharField(max_length=128)
    cell_phone_contact = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.provider_name

class Bank(models.Model):
    bank_name = models.CharField(max_length=128)
    provider = models.ManyToManyField(Provider, through='BankAccount', related_name='bank')

    def __str__(self):
        return self.bank_name

class BankAccount(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank_account_number = models.CharField(max_length=15, blank=True, null=True)
