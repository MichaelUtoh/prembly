from django.db import models
from django.conf import settings

from core.config.choices import PricingPlans


# Create your models here.
class PricingPlan(models.Model):
    duration = models.CharField(
        max_length=9, choices=PricingPlans.choices, default=PricingPlans.MONTHLY
    )
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)