from dataclasses import dataclass, field
from .exceptions import InvalidAddressException


@dataclass
class Address:
    _rec: str
    _street: str = field(init=False)

    def __post_init__(self):
        self._street = self._rec.rstrip('\n')
        self.validate()

    def validate(self):
        if not self._street:
            raise InvalidAddressException('first name is invalid')

    def get_street(self):
        return self._street
