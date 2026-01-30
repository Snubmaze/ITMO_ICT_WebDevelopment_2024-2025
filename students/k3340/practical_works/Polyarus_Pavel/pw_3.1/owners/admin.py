from django.contrib import admin
from .models import CarOwner, Car, DriverLicense, Ownership


@admin.register
class CarOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    search_fields = ('last_name', 'first_name')


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'license_number', 'license_type', 'issue_date')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_number', 'brand', 'model', 'color')
    search_fields = ('brand', 'model', 'state_number')


@admin.register(Ownership)
class OwnershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'car', 'start_date', 'end_date')