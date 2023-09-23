'''
    fetcher for coin price
    fetching response data from api
'''
import aiohttp  # pylint: disable=import-error
from src.core.src import SourcesAPI  # pylint: disable=import-error


class CoinPriceFetcher:
    '''
        Connection manager to fetch data from api

        1 - open connection - required to pass
        2 - fetch data
        3 - acessing data
        4 - close connection  - required to pass
    '''

    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.url = SourcesAPI().url_get_btc_price

    async def fetch_data(self) -> dict:
        ''' fetch data from api '''
        try:
            async with self.session.get(self.url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    status = response.status
                    return {
                        "error": f"Failed to fetch data, HTTP status: {status}"
                    }
        except aiohttp.ClientError as client_error:
            return {"error": f"Error fetching data: {client_error}"}

    async def close(self):
        '''
            manual close connection
        '''
        if not self.session.closed:
            await self.session.close()
