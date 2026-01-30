import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_core.settings')
django.setup()


from owners.models import CarOwner, Car, DriverLicense, Ownership
from typing import Dict, List
from django.db.models import Min, Max, Count, Q

def get_oldest_license() -> DriverLicense:
    return DriverLicense.objects.aggregate(Min('issue_date'))


def get_latest_ownership() -> Ownership:
    return Ownership.objects.aggregate(Max('start_date'))


def get_cars_count_by_owner() -> Dict[CarOwner: int]:
    owners = CarOwner.objects.annotate(
        cars_count=Count('ownerships'),
        filter=Q(ownerships__end_date__isnull=True)
        )
    return {owner: owner.cars_count for owner in owners}


def count_cars_by_brand() -> List[dict]:
    cars = Car.objects.values('brand').annotate(Count('id'))
    return cars


def get_drivers_by_licenses_date():
    drivers = CarOwner.objects.order_by('licenses__issue_date').distinct()
    return drivers


def main():
    print()
    # print(get_oldest_license())
    # print(get_latest_ownership())
    # print(get_cars_count_by_owner())
    # print(count_cars_by_brand())
    print(get_drivers_by_licenses_date())


if __name__ == "__main__":
    main()