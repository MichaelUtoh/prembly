from django.shortcuts import get_object_or_404

from rest_framework import serializers

from core.smartfarm.models import PricingPlan

class PricingPlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = ["id", "duration", "price", "created_at", "updated_at"]


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = ["duration", "price"]

    def save(self):
        pricing_plan = PricingPlan.objects.create(**self.validated_data)
        return pricing_plan

    def update(self):
        pricing_plan = PricingPlan.objects.filter(
            pk=self.context["pk"]
        ).update(**self.validated_data)
        return pricing_plan
