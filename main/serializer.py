from .models import Compliant
from rest_framework.serializers import ModelSerializer


class CompliantSerializer(ModelSerializer):
    class Meta:
        model = Compliant
        fields = "__all__"
