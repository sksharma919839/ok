from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


class hserviceView(viewsets.ModelViewSet):
    queryset = hservice.objects.all()
    serializer_class = hserviceSerializer
    parser_classes = (MultiPartParser, FormParser)


class ourserviceView(viewsets.ModelViewSet):
    queryset = ourservice.objects.all()
    serializer_class = ourserviceSerializer
    parser_classes = (MultiPartParser, FormParser)


class review(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = reviewSerializer
    parser_classes = (MultiPartParser, FormParser)


class vehicleAllView(viewsets.ModelViewSet):
    queryset = vehicleAll.objects.all()
    serializer_class = vehicleAllSerializer
    parser_classes = (MultiPartParser, FormParser)


class vehicleFirstView(viewsets.ModelViewSet):
    queryset = vehicleFirst.objects.all()
    serializer_class = vehicleFirstSerializer
    parser_classes = (MultiPartParser, FormParser)


class vehicleSecondView(viewsets.ModelViewSet):
    queryset = vehicleSecond.objects.all()
    serializer_class = vehicleSecondSerializer
    parser_classes = (MultiPartParser, FormParser)


class vehicleThirdView(viewsets.ModelViewSet):
    queryset = vehicleThird.objects.all()
    serializer_class = vehicleThirdSerializer
    parser_classes = (MultiPartParser, FormParser)


class vehicleFourthView(viewsets.ModelViewSet):
    queryset = vehicleFourth.objects.all()
    serializer_class = vehicleFourthSerializer
    parser_classes = (MultiPartParser, FormParser)


class serviceView(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = serviceSerializer
    parser_classes = (MultiPartParser, FormParser)


class teamView(viewsets.ModelViewSet):
    queryset = team.objects.all()
    serializer_class = teamSerializer
    parser_classes = (MultiPartParser, FormParser)


@api_view(["POST"])
def contact_view(request):
    serializer = contactSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        name = validated_data.get("name")
        subject = validated_data.get("subject")
        email = validated_data.get("email")
        message = validated_data.get("message")

        contact.objects.create(name=name, subject=subject, email=email, message=message)
        return Response({"message": "Form data reccived succesfully"})

    else:
        return Response(serializer.errors, status=400)
