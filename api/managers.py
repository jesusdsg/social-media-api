from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# extends user manaer to customize the model


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        ''' Custom function to create a user with email as main field '''
        if not email:
            raise ValueError('The Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        ''' Custom super user creation '''
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super user needs to have a is_staff = True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Super user needs to have  is_superuser = True.'))

        return self.create_superuser(self, email, password, **extra_fields)
