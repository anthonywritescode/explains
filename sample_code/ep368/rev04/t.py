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
    return BusinessID(business.id)


def get_business_name(business_id: BusinessID) -> str:
    ...


business1 = lookup_business_by_name('foo')
business2 = lookup_business_by_name('bar')

print(business1 + business2)
print(get_business_name(business1 + business2))
