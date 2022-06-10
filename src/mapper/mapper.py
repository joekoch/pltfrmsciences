from dataclasses import dataclass, field
from src.address.addresses import Addresses
from src.driver.drivers import Drivers
from itertools import permutations, product
from src.suitability.suitability import AddressDriverSuitabilityScore


class Mapper:
    pass


@dataclass
class AddressDriverMapper(Mapper):
    _addresses: Addresses
    _drivers: Drivers
    _optset: dict = field(init=False, default_factory=dict)

    def __post_init__(self):
        self.map()

    def get_possible_matchsets(self):
        for p in product(permutations(self._addresses.get_addresses()), [self._drivers.get_drivers()]):
            yield [(addr, drvr) for addr, drvr in zip(*p)]

    def map(self):

        for mset in self.get_possible_matchsets():
            total_ss = 0
            for addr_drvr_match in mset:
                addr, drvr = addr_drvr_match
                ad_ss = AddressDriverSuitabilityScore(addr.get_street(), drvr.get_first_name())
                total_ss = total_ss + ad_ss.get_ss()

            if self._optset:
                if total_ss > self._optset.get("ss"):
                    self._optset["mapping"] = mset
                    self._optset["ss"] = total_ss
            else:
                self._optset["mapping"] = mset
                self._optset["ss"] = total_ss

    def get_opt_set(self):
        return self._optset
