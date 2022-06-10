from dataclasses import dataclass, field
from .exceptions import InvalidDriverException


@dataclass
class Driver:
    _rec: str
    _first_name: str = field(init=False)

    def __post_init__(self):
        self._first_name = self._rec.rstrip('\n')
        self.validate()

    def validate(self):
        if not self._first_name:
            raise InvalidDriverException('first name is invalid')

    def get_first_name(self):
        return self._first_name
