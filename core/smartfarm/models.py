from django.db import models
from django.conf import settings

# Create your models here.
class Farmer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorite_shops",
    )
    user_image = models.ImageField(upload_to="")
    nin_number = models.CharField(max_length=15)
    nin_slip = models.ImageField(upload_to="")
    