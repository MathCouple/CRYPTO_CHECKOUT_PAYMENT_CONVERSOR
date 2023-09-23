'''
    utils api endpoints
'''


class SourcesAPI:
    ''' api endpoints '''
    def __init__(self, coins: str = 'USD,BRL'):
        self.coins = coins

    @property
    def url_get_btc_price(self):
        ''' url to get btc price in different coins '''
        return (
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&"
            f"tsyms={self.coins}"
        )
