from func_connections import connect_DYDX
from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED
from func_private import abort_all_positions
from func_public import construct_market_prices

if __name__ == "__main__":

# connect to client
  try:
      print("Connecting to client...")
      client = connect_DYDX()
  except Exception as e:
        print("Error connecting to client", e)
        exit(1)

# abort all open positions
  if ABORT_ALL_POSITIONS:
    try:
      print("Closing all positions...")
      close_orders = abort_all_positions(client)
    except Exception as e:
        print("Error closing all positions", e)
        exit(1) 

# find cointegrated pairs
if FIND_COINTEGRATED:
   
   # construct market prices
    try:
      print("Fetching market prices, please wait...")
      df_market_prices = construct_market_prices(client)
    except Exception as e:
        print("Error constructing market prices", e)
        exit(1) 