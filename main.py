import argparse

import requests
from requests.models import PreparedRequest

from config import config


def main() -> str:
    """
    A command line utility for fetching vendor name based on mac-address
    :accepts a mac-address parameter. Run `python main.py -h` for help
    :return: name of the vendor for mac address, or error message
    """
    parser = argparse.ArgumentParser(description='Fetch vendor name of a mac address.')
    parser.add_argument('-m', '--mac_address', required=True)
    args = parser.parse_args()
    mac_address = args.mac_address

    req = PreparedRequest()
    params = {
        'apiKey': config.get('api_key'),
        'search': mac_address,
    }
    req.prepare_url(config.get('url'), params)

    resp = requests.get(req.url)
    if not resp.ok:
        result = f'Error while fetching vendor name for the mac address {mac_address}\n=>' \
                 f' HTTP Status Code: ''{resp.status_code}, {resp.text}'
    else:
        result = f'Vendor Name for the mac address {mac_address} is {resp.text}'

    return result


if __name__ == '__main__':
    print(main())
