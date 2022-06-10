import argparse
from src.address.addresses import Addresses
from src.driver.drivers import Drivers
from src.mapper.mapper import AddressDriverMapper

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Main:
    @classmethod
    def run(cls):
        args = cls.parse().parse_args()

        # load address file
        addrs = Addresses.from_file(args.addr_file)

        # load driver file
        drvs = Drivers.from_file(args.drv_file)

        # call mapper to map address to driver based on max SS across all drivers
        logger.info(AddressDriverMapper(addrs, drvs).get_opt_set())

    @classmethod
    def parse(cls):
        '''
        parse command input
        :return: argparser
        '''
        parser = argparse.ArgumentParser(description='Perform address->driver mapping')
        parser.add_argument('--address-file', type=str, required=True, dest='addr_file', help='path to address file')
        parser.add_argument('--driver-file', type=str, required=True, dest='drv_file', help='path to driver file')
        return parser


if __name__ == '__main__':
    Main.run()
