from enum import Enum


class LendingStatusEnum(Enum):
    ACTIVE = "active"
    RETURNED = "returned"


def validated_lending_status(value) -> str:
    try:
        status = LendingStatusEnum(value)
        return status.value
    except ValueError:
        raise ValueError("Invalid Lending status provided. Allowed values are: 'active', 'returned'.")
