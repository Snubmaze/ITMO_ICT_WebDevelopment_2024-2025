import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_core.settings')
django.setup()


from owners.models import CarOwner, Car, DriverLicense, Ownership
from datetime import datetime
from typing import Optional


def get_cars_by_brand(brand: str) -> Optional[Car]:
    cars = Car.objects.filter(brand=brand)
    return cars


def get_owner_by_name(name: str) -> Optional[CarOwner]:
    owners = CarOwner.objects.filter(first_name__contains=name)
    return owners


def get_owner_and_license():
    owner = CarOwner.objects.order_by('?').first()
    license = DriverLicense.objects.filter(owner=owner.id)
    return license


def get_owners_by_car_color(color: str) -> Optional[CarOwner]:
    cars = Car.objects.filter(color=color)
    owners = []
    for car in cars:
        ownerships = Ownership.objects.filter(car=car.id, end_date=None)
        for ownership in ownerships:
            owner = ownership.owner
            owners.append(owner)
    return owners


def get_owners_by_ownership_start_year(year: int) -> Optional[CarOwner]:
    ownerships = Ownership.objects.filter(start_date__gte=datetime(year, 1, 1))
    return set([ownshp.owner for ownshp in ownerships])


def main():
    print(get_cars_by_brand("Toyota"))
    print(get_owner_by_name("Maria"))
    print(get_owner_and_license())
    print(get_owners_by_car_color("Red"))
    print(get_owners_by_ownership_start_year(2010))


if __name__ == "__main__":
    main()