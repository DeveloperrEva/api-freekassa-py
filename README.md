# FreeKassa - Api

## Установка

```sh
pip install api-freekassa-py
```

## Использование

### Создать ссылку платежа

```python
merchant = Merchant(shop_id=123456789,
                    secret1="secret1",
                    secret2="secret2",
                    api_key="api_key")
payment_link = merchant.get_payment_form_url(amount=100, order_id="Product 1", us_={'token':'token1',"token2":"token2"})
token1, token2 = Это при создании магазина мы получаем следующие данные: secret 1, secret 2, shop_id, api_key. Эти данные нужны для работы
```

### Проверить баланс

```python
balance = merchant.get_balance()
```

### Проверить статус платежа

```python
status = merchant.status_order(orderid)
if status == 1 - Payed
```
