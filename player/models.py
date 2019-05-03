from django.db import models
from django.conf import settings

class Player(models.Model):
    Player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)