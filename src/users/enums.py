import enum


class EducationEnum(enum.IntEnum):
    NONE = 1
    ELEMENTARY_SCHOOL = 2
    MIDDLE_SCHOOL = 3
    HIGH_SCHOOL = 4


class VehicleTypeEnum(enum.IntEnum):
    MOPED = 1
    MOTORCYCLE = 2
    MOTOR_VEHICLE = 3
    LARGE_GOODS_VEHICLE = 4
    BUS = 5
