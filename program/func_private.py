from datetime import datetime, timedelta
from func_utils import format_number
import time
from pprint import pprint

# check order status
def check_order_status(client, order_id):
    order = client.private.get_order_by_id(order_id)

# place market order
def place_market_order(client, market, side, size, price, reduce_only):

    # Get Position ID
    account_response = client.private.get_account()
    position_id = account_response.data["account"]["positionId"]

    position_id

    # get expiration time
    server_time = client.public.get_time()
    expiration = datetime.fromisoformat(server_time.data["iso"].replace("Z", "")) + timedelta(seconds=70)

    # place an order
    placed_order = client.private.create_order(
    position_id=position_id, # required for creating the order signature
    market=market,
    side=side,
    order_type="MARKET",
    post_only=False,
    size=size,
    price=price,
    limit_fee='0.015',
    expiration_epoch_seconds=expiration.timestamp(),
    time_in_force="FOK",
    reduce_only=reduce_only    
    )

    # return results
    return placed_order.data

# abort all open positions
def abort_all_positions(client):
    
    # cancel all orders
    client.private.cancel_all_orders()

    # protect API
    time.sleep(0.5)

    # get markets for reference of tick size
    markets = client.public.get_markets().data
    #pprint (markets)

    # protect API
    time.sleep(0.5)

    # get all open positions
    positions = client.private.get_positions(status="OPEN")
    all_positions = positions.data["positions"]

    # handle open positions
    close_orders = []
    if len(all_positions) > 0:

        # loop through each position
        for position in all_positions:

            # determine market
            market = position["market"]

            # determine side
            side = "BUY"
            if position["side"] == "LONG":
                side = "SELL"

            # get price
            price = float(position["entryPrice"])
            accept_price = price * 1.7 if side == "BUY" else price * 0.3
            tick_size = markets["markets"][market]["tickSize"]
            accept_price = format_number(accept_price, tick_size)

            # place order to close
            order = place_market_order(
                client,
                market,
                side, 
                position["sumOpen"],
                accept_price,
                True
            )

            #r append the result
            close_orders.append(order)

            # protect api
            time.sleep(0.2)

        # return closed orders
        return close_orders