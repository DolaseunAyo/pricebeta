from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects: CustomUserManager()

	class Meta:
		ordering = ["email"]
		verbose_name = 'User'

	def __str__(self):
		return self.email

