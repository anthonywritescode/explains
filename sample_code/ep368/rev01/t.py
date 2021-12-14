from typing import NewType


BusinessID = NewType("BusinessID", int)

# class BusinessID(int): ...


def business_name(business_id: int) -> str:
    # TODO: some database lookup ...
    ...


business_name(5)
