import time

import requests

from .utils import hash_by_sha256, hash_by_md5


class FreekassaApi:
    API_BASE_URL = 'https://api.freekassa.ru/v1/{method}'
    INVOICE_BASE_URL = 'https://pay.freekassa.ru/?{query}'

    def __init__(self, shop_id: int, secret1: str, secret2: str, api_key: str):
        self.session = requests.Session()

        self.shop_id = shop_id
        self.secret1 = secret1
        self.secret2 = secret2
        self.api_key = api_key

    def _generate_api_signature(self, json: dict) -> str:
        sorted_values = []

        for key in sorted(json.keys()):
            sorted_values.append(str(json[key]))

        return hash_by_sha256(self.api_key, '|'.join(sorted_values))

    def _generate_payment_form_signature(self, amount: int, order_id: str, currency='RUB') -> str:
        return hash_by_md5(f'{self.shop_id}:{amount}:{self.secret1}:{currency}:{order_id}')

    def _remove_none(self, params: dict, key: str = '') -> dict:
        return {key + k: v for k, v in params.items() if v is not None}

    def _create_json(self, json: dict) -> dict:
        json = json or {}
        json = {k: v for k, v in json.items() if v is not None}
        json = {**json, 'shopId': self.shop_id,
                'nonce': time.time_ns()}
        return {**json, 'signature': self._generate_api_signature(json)}

    def _request(self, method: str, json: dict = None) -> dict:
        resp = self.session.post(self.API_BASE_URL.format(method=method), json=self._create_json(json=json))
        return resp.json()
