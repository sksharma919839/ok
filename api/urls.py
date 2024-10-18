from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"hservice", hserviceView, basename="hservier")

orouter = DefaultRouter()
orouter.register(r"ourservice", ourserviceView, basename="ourservice")

rrouter = DefaultRouter()
rrouter.register(r"review", review, basename="review")

vehicleall = DefaultRouter()
vehicleall.register(r"vehicleall", vehicleAllView, basename="vehicleAll")

vehiclefirst = DefaultRouter()
vehiclefirst.register(r"vehiclefirst", vehicleFirstView, basename="vehicleFirst")

vehicelsecond = DefaultRouter()
vehicelsecond.register(r"vehiclesecond", vehicleSecondView, basename="vehicleSecond")

vehiclethird = DefaultRouter()
vehiclethird.register(r"vehiclethird", vehicleThirdView, basename="vehicleThird")

vehiclefourth = DefaultRouter()
vehiclefourth.register(r"vehiclefourth", vehicleFourthView, basename="vehicleFourth")

service = DefaultRouter()
service.register(r"service", serviceView, basename="service")

teamrouter = DefaultRouter()
teamrouter.register(r"team", teamView, basename="team")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(orouter.urls)),
    path("", include(rrouter.urls)),
    path("", include(vehicleall.urls)),
    path("", include(vehiclefirst.urls)),
    path("", include(vehicelsecond.urls)),
    path("", include(vehiclethird.urls)),
    path("", include(vehiclefourth.urls)),
    path("", include(service.urls)),
    path("", include(teamrouter.urls)),
    path("contact/", contact_view, name="contact"),
]
