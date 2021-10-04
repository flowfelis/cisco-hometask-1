import argparse

import requests
from requests.models import PreparedRequest

from config import config


def main():
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
        print(f'Error while fetching vendor name for the mac address {mac_address}\n'
              f'=> HTTP Status Code: {resp.status_code}, {resp.text}')
    else:
        print(f'Vendor Name for the mac address {mac_address} is {resp.text}')


if __name__ == '__main__':
    main()
