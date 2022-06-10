from src.utils.loader import FileLoader
from src.driver.driver import Driver
from dataclasses import dataclass, field
from .exceptions import InvalidDriverException
import logging

logger = logging.getLogger(__name__)


@dataclass
class Drivers:
    _drivers: list[Driver] = field(default_factory=list, init=False)

    @classmethod
    def from_file(cls, file_path):

        try:
            drvrs = cls()
            for rec in FileLoader.load_from_file(file_path):
                drvrs.append(Driver(rec))
            return drvrs
        except InvalidDriverException as iae:
            logger.error(f'skipping {rec} since invalid.{iae.msg}')

    def append(self, addr: Driver):
        self._drivers.append(addr)


    def get_drivers(self):
        return self._drivers
