import datetime
from urllib.parse import urlencode

from .models import Balance
from .api_base import FreekassaApi
from .type import Currencies


class Merchant(FreekassaApi):
    def get_payment_form_url(self, amount: int, order_id: str, currency=Currencies.RUB, payment_method: int = None,
                             phone: str = None, email: str = None, lang: str = None, us_: dict = None) -> str:
        if us_ is None:
            us_ = {}
            
        params = {
            'm': self.shop_id,
            'oa': amount,
            'currency': currency,
            'o': order_id,
            's': self._generate_payment_form_signature(amount, order_id, currency),
            'i': payment_method,
            'phone': phone,
            'em': email,
            'lang': lang,
        }
        params.update(self._remove_none(us_, key='us_'))
        urls = urlencode(self._remove_none(params))

        return self.INVOICE_BASE_URL.format(query=urls)

    def get_balance(self) -> Balance:
        resp = self._request('balance')
        if resp['type'] != 'success':
            raise Exception(resp['message'])

        currencies_values = {i['currency']: i.get('value') for i in resp['balance']}
        return Balance(**currencies_values)

    def status_order(self, orderId):
        params = {
            'merchant_order_id': orderId
        }
        resp = self._request('orders', params)
        if resp['type'] != 'success':
            raise Exception(resp['message'])

        return resp['orders'][0]['status']
