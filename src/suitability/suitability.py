from dataclasses import dataclass, field
from src.utils.utils import count_vowels, count_consonents, has_common_factor


class SuitabilityScore:
    pass


@dataclass
class AddressDriverSuitabilityScore(SuitabilityScore):
    _addr: str
    _driver: str
    _ss: float = field(init=False)

    def __post_init__(self):
        self.calculate_suitability()

    def calculate_suitability(self):
        addr_len = len(self._addr)
        drv_len = len(self._driver)

        self._ss = self.calculate_base_ss(addr_len)

        if has_common_factor(addr_len, drv_len):
            self._ss = self._ss * 1.5

    def calculate_base_ss(self, addr_len):
        if addr_len % 2 == 0:
            return count_vowels(self._addr) * 1
        else:
            return count_consonents(self._addr) * 1.5

    def get_ss(self):
        return self._ss
