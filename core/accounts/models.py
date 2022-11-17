from uuid import uuid4

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models, transaction

from core.config.choices import Gender, PricingPlans, Title, UserType

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def external_users(self):
        return self.filter(is_staff=False)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(unique=True, default=uuid4)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    full_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=Gender.MALE)
    title = models.CharField(max_length=4, choices=Title.choices, default=Title.MR)
    designation = models.CharField(max_length=255, blank=True, default="")
    address = models.CharField(max_length=255, blank=True)
    account_type = models.CharField(
        max_length=30, choices=UserType.choices, default=UserType.FARMER
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

