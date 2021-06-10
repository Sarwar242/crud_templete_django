from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    @property
    def is_student(self):
        if hasattr(self, 'student'):
            return True
        return False