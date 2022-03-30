from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, email, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_courier(self, username, email, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.is_active = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self.db)
        return user