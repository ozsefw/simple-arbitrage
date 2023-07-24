import json
import requests
from decimal import *
from web3 import Web3
from web3.contract import (Contract)
from Anvil import *

WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
PEPE_ERC20 = '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD'

PEPE_UNI_V2 = '0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269'
PEPE_UNI_V3 = '0xD738E6a2EF2846a643dC68092AD0fd7F5a8EB6f8'

UNI_V3_QUOTER = "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6"
UNI_V3_ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
UNI_V2_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

ANVIL_USER  = [
    "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"
]

ANVIL_URL="http://127.0.0.1:8545"
FEE_10000 = 10000
ETH = 10**18

def init_contract(address, abi):
    web3 = Web3(Web3.HTTPProvider(ANVIL_URL))

    with open(f"abi/{abi}.json") as f:
        erc_20_abi = json.load(f)

    return web3.eth.contract(
        web3.to_checksum_address(address),
        abi = erc_20_abi
    )


class BasicTxRunner:
    def __init__(self) -> None:
        self.weth_erc20 = init_contract(WETH_ERC20, "erc20")
        self.pepe_erc20 = init_contract(PEPE_ERC20, "erc20")
        self.uni_v2_router = init_contract(UNI_V2_ROUTER, "uniswap_v2_router")
        self.uni_v2 = init_contract(PEPE_UNI_V2, "uniswap_v2")
        self.uni_v3_router = init_contract(UNI_V3_ROUTER, "uniswap_v3_router")
        self.uni_v3_quoter = init_contract(UNI_V3_QUOTER, "uniswap_v3_quoter")
        self.uni_v3 = init_contract(PEPE_UNI_V3, "uniswap_v3")
        self.account = ANVIL_USER[0]

    def save_anvil_snapshot(self):
        data = {
            "jsonrpc": "2.0",
            "method": "anvil_snapshot",
            "params": [],
            "id": 0
        }
        response = requests.post(url=ANVIL_URL, json=data)
        if response.status_code != 200:
            raise Exception(response.content)
        msg = json.loads(response.content)
        self.snap_shot = msg["result"]

    def revert_evm(self):
        data = {
            "jsonrpc": "2.0",
            "method": "anvil_revert",
            "params":[ self.snap_shot ],
            "id": 0
        }
        response = requests.post(url=ANVIL_URL, json=data)
        if response.status_code != 200:
            raise Exception(response.content)
    
    def run_in_state(self, fun, params):
        self.save_anvil_snapshot()

        try:
            fun(params)
        except:
            print("fun run failed")

        self.revert_evm()

    def get_uni_v3_slot0(self):
        return self.uni_v3.functions.slot0().call()

    def get_uni_v3_liquidity(self):
        return self.uni_v3.functions.liquidity().call()

    def get_uni_v2_reserves(self):
        reserve = self.uni_v2.functions.getReserves().call()
        r_x = reserve[0]
        r_y = reserve[1]
        return [r_x, r_y]

    def get_uni_v3_tick_bitmap_value(self, index):
        return self.uni_v3.functions.tickBitmap(index).call()

    def get_uni_v3_tick_info(self, index):
        return self.uni_v3.functions.ticks(index).call()

class BasicTxRunnerV2:
    def __init__(self) -> None:
        self.uni_v3 = UniswapV3()
    
    # def get_uni_v3_slot0(self):
    #     return self.uni_v3.slot0()

class UniswapV3:
    def __init__(self) -> None:
        contract = init_contract(PEPE_UNI_V3, "uniswap_v3")
        # init_contract(PEPE_UNI_V3, "uniswap_v3")
        self.functions = contract.functions

    def tick_bitmap(self, index):
        return self.functions.tickBitmap(index).call()
    
    def ticks(self, tick):
        return self.functions.ticks(tick).call()

    def slot0(self):
        return self.functions.slot0().call()

    def liquidity(self):
        return self.functions.liquidity().call()
    