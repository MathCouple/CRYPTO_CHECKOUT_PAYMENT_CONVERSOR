'''
    This class is responsible for calculating the price of a coin
    and converting it to the desired currency.

    USD is the default currency, but it can be changed to BRL.
    USD and BRL avaliable

    Satoshi can be converted either to BRL or USD
    coin = to N satoshis

    remember that SATOSHI is equal to 0.00000001 BTC

    get_brl_coin - takes advantage to convert the price of bitcoin
    to dolar then proportionally to Brazillian Real
    and the relation btc_dolar/real_dolar is used to Brazillian Real
    approximation.

    this is a asyncronous function, so it can be used with await
    or asyncio.run
    I'll incorporate into a class later on to make real time sales
'''


class CoinPriceCalculator:
    '''
        get_btc_price: get the price of BTC to a specif coin and stores
        get_brl_coin_price: get the price of BRL
        get_coin_to_satoshi: get the price of a coin to satoshi
    '''
    def __init__(self, data):
        self.data = data

    def get_btc_price(self, coin: str = 'USD') -> float:
        ''' get the price of BTC to a specif coin and stores '''
        return self.data.get(coin, 0)

    def get_brl_coin_price(self, amount: float = 1) -> float:
        ''' get the price of BRL '''
        real_current_price = (
            self.get_btc_price('BRL') / self.get_btc_price('USD')
        )*amount
        return format(real_current_price, '.2f')

    def get_coin_to_satoshi(
        self,
        coin: str = 'USD',
        amount: float = 1
    ) -> float:
        ''' get the price of a coin to satoshi '''
        satoshi_btc_prop = 100000000
        btc_price = self.get_btc_price(coin)
        coin_to_satoshi = (satoshi_btc_prop / btc_price)*amount
        return format(coin_to_satoshi, '.2f')
