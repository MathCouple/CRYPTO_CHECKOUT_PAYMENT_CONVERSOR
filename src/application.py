'''
    APP consolidation

    conversor.coin_price_fetcher.CoinPriceFetcher
    conversor.coin_price_calculator.CoinPriceCalculator

    application.MainGetCoinPrices

    run:
        - fetch data: connect to api and fetch data
        - calculate data: calculate the data, parameters are passed:
            - coin: coin to be calculated
            - amount: amount of coin to be calculated

'''
# pylint: disable=import-error
from src.conversor.coin_price_fetcher import (
    CoinPriceFetcher
)
# pylint: disable=import-error
from src.conversor.coin_price_calculator import (
    CoinPriceCalculator
)


class MainGetCoinPrices:
    ''' Main class to run the application '''
    def __init__(self):
        self.fetcher = CoinPriceFetcher()
        self.data = None
        self.calculator = None

    async def run(
        self,
        coin: str = 'USD',
        amount: float = 1
    ) -> dict:
        ''' run the application '''
        try:
            self.data = await self.fetcher.fetch_data()

            if "error" in self.data:
                print(self.data["error"])
                return {
                    "status": "error",
                    "message": self.data["error"]
                }

            self.calculator = CoinPriceCalculator(self.data)

            btc_price = self.calculator.get_btc_price(coin)
            # print(f"Current BTC Price({coin}): {btc_price}")

            if coin == 'BRL':
                amount_1 = amount
            else:
                amount_1 = 1

            brl_price = self.calculator.get_brl_coin_price(amount_1)
            # print(f"Current Real Price (USD>BRL): {brl_price}")

            coin_to_satoshi = self.calculator.get_coin_to_satoshi(coin, amount)
            # print(f"{amount} {coin} in Satoshi: {coin_to_satoshi}")

            coin_data = {
                "status": "success",
                "btc_price": btc_price,
                "real_price": brl_price,
                "coin_to_satoshi": coin_to_satoshi
            }

            return coin_data

        finally:

            await self.fetcher.close()
