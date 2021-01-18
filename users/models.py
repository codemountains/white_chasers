import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
	BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
	"""
	ユーザマネージャー
	"""

	def create_user(self, email, password=None):
		if not email:
			raise ValueError('メールアドレスは必須です')

		user = self.model(email=self.normalize_email(email))
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, password):
		user = self.create_user(email, password)
		user.is_active = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user


class User(AbstractBaseUser, PermissionsMixin):
	"""
	ユーザモデル
	"""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'

	def __str__(self):
		return self.email
