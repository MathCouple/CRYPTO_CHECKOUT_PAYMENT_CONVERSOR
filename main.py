'''
    This is the main file of the project.

    It's responsible for running the application and
    consolidating all APPs into one.
'''

import asyncio
from src.application import MainGetCoinPrices


async def main():
    '''
        run the application

        :return: dict with the data
        :parameter: coin: coin to be calculated (USD, BRL)
        :parameter: amount: amount of coin to be calculated(float)
    '''

    coin = 'BRL'
    amount = 2

    app = MainGetCoinPrices()
    data = await app.run(
        coin=coin,
        amount=amount
    )

    print(data)


if __name__ == "__main__":
    asyncio.run(main())
