from enum import Enum


class SaleStatusEnum(Enum):
    CASH_IN_HAND = "cash_in_hand"
    PROCESSED = "processed"
    RETURNED = "returned"


def validated_sale_status(value) -> str:
    allowed_statuses = {SaleStatusEnum.CASH_IN_HAND, SaleStatusEnum.PROCESSED}
    try:
        status = SaleStatusEnum(value)
        if status not in allowed_statuses:
            raise ValueError(
                f"Invalid Sale status provided. Allowed values are: {', '.join(status.value for status in allowed_statuses)}.")

        return status.value
    except ValueError:
        raise ValueError(
            f"Invalid Sale status provided. Allowed values are: {', '.join(status.value for status in allowed_statuses)}.")
