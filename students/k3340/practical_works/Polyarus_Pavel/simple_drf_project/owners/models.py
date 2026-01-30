from django.db import models


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 'car_owner'
        verbose_name = 'Car Owner'
        verbose_name_plural = "Car Owners"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class DriverLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name="licenses", null=False)
    license_number = models.CharField(max_length=10, null=False)
    license_type = models.CharField(max_length=10, null=False)
    issue_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'driver_license'
        verbose_name = 'Driver License'
        verbose_name_plural = 'Driver Licenses'

    def __str__(self):
        return f"License {self.license_number}"


class Car(models.Model):
    state_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = 'car'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.color} {self.brand} {self.model} ({self.state_number})"


class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name='ownerships')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='ownerships')
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True)
    
    class Meta:
        db_table = 'ownership'
        verbose_name = 'Ownership'
        verbose_name_plural = 'Ownerships'

    def __str__(self):
        return f"{self.owner} owns {self.car}"
    

