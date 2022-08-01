from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
  def create_user(self, username, email, github, password=None):
    if not username:
      raise ValueError("Username is required!")
    if not email:
      raise ValueError("Email address is required!")
    if not github:
      raise ValueError("GitHub account is required!")

    user = self.model(
      username = username,
      email = self.normalize_email(email),
      github = github,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email, github, password):
    user = self.create_user(
      username, 
      email, 
      github,
      password = password, 
    )

    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.is_admin = True

    user.save(using=self._db)
    return user

# Create your models here.
class Account(AbstractBaseUser):
  username = models.CharField(max_length=30, unique=True)
  email = models.EmailField(max_length=60, unique=True)
  github = models.CharField(max_length=30)
  profile_picture = models.FileField(upload_to='account_images/', null=True, blank=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'github']

  objects = AccountManager()

  def __str__(self):
    return self.username

  def get_username(self):
    return self.username

  def get_github(self):
    return self.github

  def get_email(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return True
