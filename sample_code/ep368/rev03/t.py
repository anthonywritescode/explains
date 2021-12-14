from typing import NewType
from typing import NamedTuple


class Business(NamedTuple):
    id: int
    name: str


BusinessID = NewType("BusinessID", int)

# class BusinessID(int): ...


def lookup_business_by_name(name: str) -> BusinessID:
    # pretend that this came from the database
    business = Business(id=4, name='my business')
    return business.id


def business_name(business_id: BusinessID) -> str:
    # TODO: some database lookup ...
    ...


business_name(5)
