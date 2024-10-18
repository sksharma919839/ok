from django.contrib import admin
from .models import *


class hserviceAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "heading", "deatail", "link")


class ourserviceAdmin(admin.ModelAdmin):
    list_display = ("id", "b", "h4", "p")


class reviewAdmin(admin.ModelAdmin):
    list_display = ("id", "h4", "h5", "p", "h5b")


class vehicleAllAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "p", "link")


class vehicleFirstAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "p", "link")


class vehicleSecondAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "p", "link")


class vehicleThirdAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "p", "link")


class vehicleFourthAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "p", "link")


class serviceAdmin(admin.ModelAdmin):
    list_display = ("id", "img", "h5", "p", "link")


class teamAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "h2", "p")


class contactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject", "email", "message")


admin.site.register(hservice, hserviceAdmin)
admin.site.register(ourservice, ourserviceAdmin)
admin.site.register(review, reviewAdmin)
admin.site.register(vehicleAll, vehicleAllAdmin)
admin.site.register(vehicleFirst, vehicleFirstAdmin)
admin.site.register(vehicleSecond, vehicleSecondAdmin)
admin.site.register(vehicleThird, vehicleThirdAdmin)
admin.site.register(vehicleFourth, vehicleFourthAdmin)
admin.site.register(service, serviceAdmin)
admin.site.register(team, teamAdmin)
admin.site.register(contact, contactAdmin)
