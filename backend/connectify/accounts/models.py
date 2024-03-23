from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, username, password=None, password2=None):
      """
      Creates and saves a User with the given email, username, and password.
      """
      if not email:
          raise ValueError('User must have an email address')
      if not username:
          raise ValueError('User must have an username')

      user = self.model(
          email=self.normalize_email(email),
          username=username,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, username, password=None):
      """
      Creates and saves a superuser with the given email, username, and password.
      """
      user = self.create_user(
          email,
          password=password,
          username=username,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  username = models.CharField(max_length=200,unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
      return self.username

  def has_perm(self, perm, obj=None):
      return self.is_admin

  def has_module_perms(self, app_label):
      return True

  @property
  def is_staff(self):
      return self.is_admin
  
#User profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    profile_img = models.ImageField(upload_to='profile_img',blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=50,blank=True,null=True)
    bio = models.CharField(max_length=500,blank=True,null=True)