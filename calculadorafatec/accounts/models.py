from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Modelo customizado de usuário.
    Herdamos de AbstractUser porque mantém:
      - username
      - first_name
      - last_name
      - email
      - password
      - is_staff, is_active...
      - groups/perms
    Mas permite adicionar novos campos.
    """
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username or self.email
