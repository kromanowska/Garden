from __future__ import unicode_literals

import enum

from django.db import migrations


class VehicleTypeEnum(enum.IntEnum):
    MOPED = 1
    MOTORCYCLE = 2
    MOTOR_VEHICLE = 3
    LARGE_GOODS_VEHICLE = 4
    BUS = 5


def migrate_driving_licences(apps, schema_editor):
    """
    Source: https://en.wikipedia.org/wiki/European_driving_licence#Categories_valid_in_all_EEA_member_states
    """
    DrivingLicence = apps.get_model('users', 'DrivingLicence')
    DrivingLicence.objects.create(
        class_name='AM',
        vehicle_type=VehicleTypeEnum.MOPED,
        description='Two-wheel vehicles or three-wheel vehicles with a maximum design speed '
                    'of not more than 45 km/h and with a cylinder capacity not exceeding 50 cubic centimetres.'
    )
    DrivingLicence.objects.create(
        class_name='A1',
        vehicle_type=VehicleTypeEnum.MOTORCYCLE,
        description='Motorcycles with a cylinder capacity not exceeding 125 cubic centimetres and a power '
                    'not exceeding 11 kW; and motor tricycles with a power not exceeding 15 kW.'
    )
    DrivingLicence.objects.create(
        class_name='A2',
        vehicle_type=VehicleTypeEnum.MOTORCYCLE,
        description='Motorcycles of a power not exceeding 35 kW and with a power/weight ratio not '
                    'exceeding 0,2 kW/kg (Switzerland: 0,16 kW/kg) and not derived from a vehicle of more '
                    'than double its power.'
    )
    DrivingLicence.objects.create(
        class_name='A',
        vehicle_type=VehicleTypeEnum.MOTORCYCLE,
        description='Any motorcycle or motor tricycle not in category A1/A2'
    )
    DrivingLicence.objects.create(
        class_name='B',
        vehicle_type=VehicleTypeEnum.MOTOR_VEHICLE,
        description='Motor vehicles with a maximum authorised mass (MAM) not exceeding 3500 kg and designed '
                    'and constructed for the carriage of no more than eight passengers in addition to the driver; '
                    'motor vehicles in this category may be combined with a trailer having a maximum authorised '
                    'mass which does not exceed 750 kg. You can also tow heavier trailers if the total MAM of '
                    'the vehicle and trailer isn’t more than 3,500 kg.'
    )
    DrivingLicence.objects.create(
        class_name='BE',
        vehicle_type=VehicleTypeEnum.MOTOR_VEHICLE,
        description='Without prejudice to the provisions of type-approval rules for the vehicles concerned, '
                    'a combination of vehicles consisting of a tractor vehicle in category B and a trailer or '
                    'semi-trailer where the maximum authorised mass of the trailer or semi-trailer does '
                    'not exceed 3500 kg.'
    )
    DrivingLicence.objects.create(
        class_name='B1',
        vehicle_type=VehicleTypeEnum.MOTOR_VEHICLE,
        description='Heavy quadricycles'
    )
    DrivingLicence.objects.create(
        class_name='C1',
        vehicle_type=VehicleTypeEnum.LARGE_GOODS_VEHICLE,
        description='Large goods vehicle with a maximum authorised mass of not more than 7.5 t; with or without '
                    'a trailer with a maximum mass of less than 750 kg.	'
    )
    DrivingLicence.objects.create(
        class_name='C1E',
        vehicle_type=VehicleTypeEnum.LARGE_GOODS_VEHICLE,
        description='Combinations of vehicles where the tractor vehicle is in category C and its trailer '
                    'or semi-trailer has a maximum authorised mass of over 750 kg.	'
    )
    DrivingLicence.objects.create(
        class_name='C',
        vehicle_type=VehicleTypeEnum.LARGE_GOODS_VEHICLE,
        description='Large goods vehicle with a maximum authorised mass of more than 3.5 t mass and not '
                    'more than 8 + 1 seats (lorry); with a trailer with a maximum mass of 750 kg.	'
    )
    DrivingLicence.objects.create(
        class_name='CE',
        vehicle_type=VehicleTypeEnum.LARGE_GOODS_VEHICLE,
        description='Other combinations of vehicles and trailers which with combined maximum authorised mass '
                    'of more than 750 kg.	'
    )
    DrivingLicence.objects.create(
        class_name='D1',
        vehicle_type=VehicleTypeEnum.BUS,
        description='Light buses with a maximum of 16 + 1 seats, maximum length of 8 metres.	'
    )
    DrivingLicence.objects.create(
        class_name='D1E',
        vehicle_type=VehicleTypeEnum.BUS,
        description='Combinations of vehicles where the tractor vehicle is in category D1 and its trailer has '
                    'a maximum authorised mass of over 750 kg.	'
    )
    DrivingLicence.objects.create(
        class_name='D',
        vehicle_type=VehicleTypeEnum.BUS,
        description='Vehicles with more than 8 + 1 seats (buses).	'
    )
    DrivingLicence.objects.create(
        class_name='DE',
        vehicle_type=VehicleTypeEnum.BUS,
        description='Combinations of vehicles where the tractor vehicle is in category D and its trailer has '
                    'a maximum authorised mass of over 750 kg.	'
    )


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20170709_1316'),
    ]

    operations = [
        migrations.RunPython(migrate_driving_licences),
    ]
