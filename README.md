
# Project idea
This is a part of a bigger application. And this one will be responsible for converting the payment from the user to the currency that the user wants to receive the payment.

It will also be responsible for the checkout of the payment, and the payment itself.
I'm using aiohttp due to the freedom of the configuration.

## This project is divided into 2 parts:
- Checkout:
    - Crypto Checkout (LIGHTNING NETWORK, TRON)
    - Fiat Checkout (PIX | MercadoPago | Brazil Only)
- Coin Conversor (BRL, SATOSHI | REAL/USD)
## Checklist
- [] Completed
    - [] Crypto Checkout
        - [] Lightning Network
        - [] Tron
    - [] Fiat Checkout
        - [] PIX
    - [x] Coin Conversor
        - [x] BRL
        - [x] SATOSHI
        - [x] BTC
## Code Style
- Modular
- PEP8
- Conversor: Monolithic Structure
- Checkout: Microservices Structure
- POO
- ⚠️conversorpricefetcher have a direct dependence (SOLI[D] violation): 
    - 1 its intentional
    - 2 a layer of abstraction would be overkill for this project
    - 3 python does not have native interfaces, so it would be verboselly unnecessary to create one for this project
## 0. Create a virtual environment
```
- python -m venv 00_venv_brain (python3 -m venv 00_venv_brain)
- 00_venv_brain\Scripts\activate (00_venv_brain/bin/activate)
```

## 1. Install dependencies if necessary
pip install -r requirements.txt

## 2. Run the project
python main.py


Directory Structure:
```
- checkout
    - crypto_checkout
        - lightning_network
        - tron
    - pix
- coin_conversor
- core
    - src.py(API base url)
    - .env (api keys)
    - connections
        - lightning_network (nodeless.io: https://nodeless.io/api-docs)
        - tron (tron: https://developers.tron.network/reference/select-network)
        - pix (mercado pago: https://www.mercadopago.com.br/developers/en/reference)
```