from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

# !!!SELECT MODE !!!!
MODE="DEVELOPMENT"

# Close all open positions
ABORT_ALL_POSITIONS = False

# find co-integrated pairs
FIND_COINTEGRATED = True

# place trades
PLACE_TRADES = True

# resolution
RESOLUTION = "1HOUR"

# stats window
WINDOW = 21

# thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 18000

# thresholds - closing
CLOSE_AT_ZSCORE_CROSS = True

# ethereum address
ETHEREUM_ADDRESS = "0xAdf67C1381840d1d2F961cc3F1D0036714Ca6c52"
#wallet private key
ETH_PRIVATE_KEY = "0x94203c74f31ac22076d6a7ab2c8a340c092471aa6e6ee085d0cfb1fa099eb4b6"

# keys - production - mainnet DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# keys - DEVELOPMENT - GOERLI DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# keys - export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == 'PRODUCTION' else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == 'PRODUCTION' else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == 'PRODUCTION' else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == 'PRODUCTION' else DYDX_API_PASSPHRASE_TESTNET

# host export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_GOERLI

# http provider
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/yHwQokXpGdpmn-J_0iB8mgrX6vDqxuE3"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/drBi1vwcfx4vTAXGGnDqaH3HJcfxcyr1"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == 'PRODUCTION' else HTTP_PROVIDER_TESTNET