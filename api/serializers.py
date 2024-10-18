from rest_framework import serializers
from .models import *


class hserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = hservice
        fields = "__all__"


class ourserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ourservice
        fields = "__all__"


class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = "__all__"


class vehicleAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleAll
        fields = "__all__"


class vehicleFirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleFirst
        fields = "__all__"


class vehicleSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleSecond
        fields = "__all__"


class vehicleThirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleThird
        fields = "__all__"


class vehicleFourthSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicleFourth
        fields = "__all__"


class serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = service
        fields = "__all__"


class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = "__all__"


class contactSerializer(serializers.Serializer):
    name = serializers.CharField()
    subject = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()
