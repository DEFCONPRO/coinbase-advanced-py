from typing import Optional

from coinbase.constants import API_PREFIX


def get_candles(
    self, product_id: str, start: str, end: str, granularity: str, **kwargs
):
    """
    Get rates for a single product by product ID, grouped in buckets.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getcandles
    """
    endpoint = f"{API_PREFIX}/products/{product_id}/candles"

    params = {
        "start": start,
        "end": end,
        "granularity": granularity,
    }

    if kwargs:
        params.update(kwargs)

    return self.get(endpoint, params=params)


def get_market_trades(
    self,
    product_id: str,
    limit: int,
    start: Optional[str] = None,
    end: Optional[str] = None,
    **kwargs,
):
    """
    Get snapshot information, by product ID, about the last trades (ticks), best bid/ask, and 24h volume.

    https://docs.cloud.coinbase.com/advanced-trade-api/reference/retailbrokerageapi_getmarkettrades
    """
    endpoint = f"{API_PREFIX}/products/{product_id}/ticker"

    params = {"limit": limit, "start": start, "end": end}

    # Filter out None values from the params dictionary
    if kwargs:
        params.update(kwargs)
    params = {key: value for key, value in params.items() if value is not None}

    return self.get(endpoint, params=params)
