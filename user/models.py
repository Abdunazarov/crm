from email.policy import default
from enum import unique
from ftplib import MAXLINE
from multiprocessing.managers import BaseManager
from operator import mod
from pyexpat import model
import re
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import PasswordInput



class UserManager(BaseUserManager):

    def create_user(self, email, first_name, second_name, password, **others):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            second_name=second_name
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, first_name, second_name, password, **others):
        user = self.create_user(
            email=email,
            first_name=first_name,
            second_name=second_name,
            password=password,
            **others
        )
        user.is_staff = user.is_active = user.is_superuser = True
        user.role = 'Суперадмин'
        user.save()
        return user



class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    second_name = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=150, null=True, blank=True, default='Риелтор')
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True) # saves every time
    date_joined = models.DateTimeField(auto_now_add=True) # saves once

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff
    
    def has_module_perms(self, app_label):
        return True



