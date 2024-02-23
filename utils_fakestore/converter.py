# api utilisé : 
# https://github.com/fawazahmed0/currency-api#readme

import requests as rq

base_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/cad"

def _get_rate_cad_to_X (currency):
    res = rq.get(f"{base_url}/{currency}.json")
    rate = res.json()[currency]
    return rate

def convert_cad_to_X(amount, currency):
    rate = _get_rate_cad_to_X(currency)
    return amount * rate

def convert_cad_to_us(amount):      return convert_cad_to_X(amount,"usd")
def convert_cad_to_eur(amount):     return convert_cad_to_X(amount,"eur")
def convert_cad_to_btn(amount):     return convert_cad_to_X(amount,"btn")

