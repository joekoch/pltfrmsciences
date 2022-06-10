from src.utils.loader import FileLoader
from .address import Address
from dataclasses import dataclass, field
from .exceptions import InvalidAddressException
import logging

logger = logging.getLogger(__name__)


@dataclass
class Addresses:
    _addresses: list[Address] = field(default_factory=list, init=False)

    @classmethod
    def from_file(cls, file_path):

        try:
            addrs = cls()
            for rec in FileLoader.load_from_file(file_path):
                addrs.append(Address(rec))
            return addrs
        except InvalidAddressException as iae:
            logger.error(f'skipping {rec} since invalid.{iae.msg}')

    def append(self, addr: Address):
        self._addresses.append(addr)

    def get_addresses(self):
        return self._addresses
