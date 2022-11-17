from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from core.config.services import filter_http_method_names
from core.smartfarm.models import PricingPlan
from core.smartfarm.serializers import PricingPlanSerializer, PricingPlanListSerializer


class PricingPlanViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
    http_method_names = filter_http_method_names(["patch"])

    @swagger_auto_schema(
        request_body=PricingPlanSerializer,
        responses={status.HTTP_201_CREATED: PricingPlanSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=PricingPlanSerializer,
        responses={status.HTTP_200_OK: PricingPlanListSerializer},
    )
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"pk": self.kwargs["pk"]}
        )
        serializer.is_valid(raise_exception=True)
        serializer.update()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=None, responses={status.HTTP_200_OK: PricingPlanListSerializer})
    def list(self, request, *args, **kwargs):
        plans_qs = self.get_queryset()
        serializer = self.get_serializer(plans_qs, many=True)
        data = PricingPlanListSerializer(plans_qs, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)