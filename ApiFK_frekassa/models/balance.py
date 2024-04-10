from pydantic import BaseModel


class Balance(BaseModel):
    RUB: float
    USD: float
    EUR: float
    KZT: float
    UAH: float
