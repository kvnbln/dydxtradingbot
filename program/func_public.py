from constants import RESOLUTION
from func_utils import get_ISO_time
import pandas as pd 
import numpy as np
import time

from pprint import pprint

# get relevant time periods for ISO from and to
ISO_TIMES = get_ISO_time()

# get candles historical
def get_candles_historical(client,market):

    # define output
    close_prices = []

    # extract historical price data for each time frame
    for timeframe in ISO_TIMES.keys():

      # confirm times needed
      tf_obj = ISO_TIMES[timeframe]
      from_iso = tf_obj["from_iso"]
      to_iso = tf_obj["to_iso"]

      # protect api
      time.sleep(0.2)

      # get data
      candles = client.public.get_candles(
         market=market,
         resolution=RESOLUTION,
         from_iso=from_iso,
         to_iso=to_iso,
         limit=100
      )

      # structure data
      for candle in candles.data["candles"]:
         close_prices.append({"datetime": candle["startedAt"], market: candle["close"]})

    # construct and return DataFrame
    close_prices.reverse()
    return close_prices


# construct market prices
def construct_market_prices(client):



  # declare variables
  tradeable_markets = []
  markets = client.public.get_markets()

  # find tradeable pairs
  for market in markets.data["markets"].keys():
    market_info = markets.data["markets"][market]
    if market_info["status"] == "ONLINE" and market_info["type"] == "PERPETUAL":
       tradeable_markets.append(market)

  # set initial datafram
  close_prices = get_candles_historical(client, tradeable_markets[0])

  df = pd.DataFrame(close_prices)
  df.set_index("datetime", inplace=True)

  print(df.tail(10))