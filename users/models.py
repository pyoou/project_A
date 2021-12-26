from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, phone_number, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, phone_number, password, **other_fields)

    def create_user(self, email, user_name, phone_number, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        if not phone_number:
            raise ValueError(_("You must provide a phone number"))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(_('user name'), max_length=150, unique=True)
    phone_number = models.CharField(_('phone number'), max_length=30, unique=True)

    profile_image = models.ImageField(_('profile image'), width_field=200, height_field=200,
                                      upload_to='images/', blank=True, null=True)

    joined_date = models.DateTimeField(_('joined date'), default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone_number']

    def __str__(self):
        return self.user_name
