from constants import RESOLUTION
from func_utils import get_ISO_time
import pandas as pd 
import numpy as np
import time

from pprint import pprint

# get relevant time periods for ISO from and to
ISO_TIMES = get_ISO_time()

pprint(ISO_TIMES)

# construct market prices
def construct_market_prices(client):
    pass