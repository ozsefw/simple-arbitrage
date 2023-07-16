import subprocess
import os
import signal
import json
import math
from typing import List
import requests
import time
from decimal import *
from web3 import Web3
from web3.contract import (
    Contract,
    ContractCaller,
)

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

def restart_anvil():
    try:
        pid_map = map(int, subprocess.check_output(["pidof", "anvil"]).split())
        pid_list = [i for i in pid_map]
        if len(pid_list) > 0:
            print("kill: ", pid_list[0])
            os.kill(pid_list[0], signal.SIGKILL)
    except:
        print("no anvil running")
    
    rpc_url = "https://eth-mainnet.nodereal.io/v1/5e75d4566e0048b3b195abbf1de9f366"
    block_number = 17589010

    subprocess.Popen(
        [
            "anvil",
            "--fork-chain-id=1",
            f"--fork-url={rpc_url}",
            f"--fork-block-number={block_number}",
            "--compute-units-per-second=300"
        ],
        stdout = subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    time.sleep(1)

def start_anvil():
    try:
        pid_map = map(int, subprocess.check_output(["pidof", "anvil"]).split())
        pid_list = [i for i in pid_map]
        if len(pid_list) > 0:
            return
    except:
        pass

    rpc_url = "https://eth-mainnet.nodereal.io/v1/5e75d4566e0048b3b195abbf1de9f366"
    block_number = 17589010

    subprocess.Popen(
        [
            "anvil",
            "--fork-chain-id=1",
            f"--fork-url={rpc_url}",
            f"--fork-block-number={block_number}",
            "--compute-units-per-second=300"
        ],
        stdout = subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    time.sleep(1)

class ArbiTest:
    def __init__(self):
        web3 = Web3(Web3.HTTPProvider(ANVIL_URL))

        with open("abi/uniswap_v3_quoter.json") as f:
            uni_v3_quoter_abi = json.load(f)

        self.uni_v3_quoter = web3.eth.contract(
            web3.to_checksum_address(UNI_V3_QUOTER),
            abi = uni_v3_quoter_abi,
        )
        
        with open("abi/uniswap_v2_router.json") as f:
            uni_v2_router_abi = json.load(f)

        self.uni_v2_router = web3.eth.contract(
            web3.to_checksum_address(UNI_V2_ROUTER),
            abi = uni_v2_router_abi,
        )

        with open("abi/uniswap_v3.json") as f:
            uniswap_v3_abi = json.load(f)

        self.uni_v3 = web3.eth.contract(
            web3.to_checksum_address(PEPE_UNI_V3),
            abi = uniswap_v3_abi,
        )

        with open("abi/uniswap_v2.json") as f:
            uniswap_v2_abi = json.load(f)

        self.uni_v2 = web3.eth.contract(
            web3.to_checksum_address(PEPE_UNI_V2),
            abi = uniswap_v2_abi,
        )

        with open("abi/erc20.json") as f:
            erc_20_abi = json.load(f)
        
        self.pepe_erc20 = web3.eth.contract(
            web3.to_checksum_address(PEPE_ERC20),
            abi = erc_20_abi
        )

        self.weth_erc20 = web3.eth.contract(
            web3.to_checksum_address(WETH_ERC20),
            abi = erc_20_abi
        )

        with open("abi/uniswap_v3_router.json") as f:
            uni_v3_router_abi = json.load(f)

        self.uni_v3_router = web3.eth.contract(
            web3.to_checksum_address(UNI_V3_ROUTER),
            abi = uni_v3_router_abi
        )

class UniswapV2:
    def __init__(self, address) -> None:
        web3 = Web3(Web3.HTTPProvider(ANVIL_URL))

        with open("abi/uniswap_v2.json") as f:
            abi = json.load(f)

        self.functions = web3.eth.contract(
            web3.to_checksum_address(address),
            abi=abi,
        ).functions

    def get_reserves(self)->List[int]:
        reserves = self.functions.getReserves().call()
        [pepe_amount, eth_amount] = [reserves[1], reserves[0]]
        return [pepe_amount, eth_amount]

    def get_price(self)->int:
        [pepe_amount, eth_amount] = self.get_reserves()
        return int(pepe_amount/eth_amount)

class UniswapV3:
    def __init__(self, address) -> None:
        web3 = Web3(Web3.HTTPProvider(ANVIL_URL))

        with open("abi/uniswap_v3.json") as f:
            abi = json.load(f)

        self.functions = web3.eth.contract(
            web3.to_checksum_address(address),
            abi=abi,
        ).functions

    def slot0(self)->List[int]:
        slot0 = self.functions.slot0().call()
        return slot0

    def get_price(self)->int:
        slot0 = self.slot0()
        sqrt_price_x96 = slot0[0]
        sqrt_price = sqrt_price_x96>>96
        price = sqrt_price**2
        return price

class UniswapV3Router:
    def __init__(self) -> None:
        pass

class UnswapV3Quoter:
    def __init__(self) -> None:
        pass

# class ERC20(Contract):
#     def __init__(self, address) -> None:
#         web3 = Web3(Web3.HTTPProvider(ANVIL_URL))

#         with open("abi/erc20.json") as f:
#             erc_20_abi = json.load(f)

#         self = web3.eth.contract(
#             web3.to_checksum_address(address),
#             abi = erc_20_abi
#         ).functions

#     # def balanceOf(self, address)->int:
#     #     return self.functions.balanceOf(address).call()

#     # def deposit(self, account, amount):
#     #     self.functions.deposit().transact({
#     #         "from": account,
#     #         "value": amount
#     #     })

def init_contract(address, abi):
    web3 = Web3(Web3.HTTPProvider(ANVIL_URL))

    with open(f"abi/{abi}.json") as f:
        erc_20_abi = json.load(f)

    return web3.eth.contract(
        web3.to_checksum_address(address),
        abi = erc_20_abi
    )


class BasixTxRunner:
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

class TxRunner(BasixTxRunner):
    def __init__(self) -> None:
        super().__init__()
        self.weth_erc20 = init_contract(WETH_ERC20, "erc20")
        self.pepe_erc20 = init_contract(PEPE_ERC20, "erc20")
        self.uni_v3_router = init_contract(UNI_V3_ROUTER, "uniswap_v3_router")
        self.uni_v2_router = init_contract(UNI_V2_ROUTER, "uniswap_v2_router")
        self.uni_v2 = init_contract(PEPE_UNI_V2, "uniswap_v2")
        self.uni_v3 = init_contract(PEPE_UNI_V3, "uniswap_v3")
        self.account = ANVIL_USER[0]

    def init_uni_v3_env(self, amount_in):
        self.weth_erc20.functions.deposit(
        ).transact({
            "value": amount_in,
            "from": self.account
        })

        self.weth_erc20.functions.approve(
            UNI_V3_ROUTER,
            amount_in
        ).transact({
            "from": self.account
        })

    def swap_from_v3_to_v2(self, amount_in):
        self.init_uni_v3_env(10*ETH)

        self.uni_v3_router.functions.exactInputSingle({
            "tokenIn": WETH_ERC20,
            "tokenOut": PEPE_ERC20,
            "fee": FEE_10000,
            "recipient": PEPE_UNI_V2,
            "deadline": int(time.time())+10*60,
            "amountIn": amount_in,
            "amountOutMinimum": 0,
            "sqrtPriceLimitX96": 0,
        }).transact({
            "from": ANVIL_USER[0],
        })

    def withdraw_from_uni_v2(self)->int:
        pepe_erc20_amount = self.pepe_erc20.functions.balanceOf(PEPE_UNI_V2).call()
        [_, pepe_uni_v2_reserve_amount, _] = self.uni_v2.functions.getReserves().call()

        v2_token_amount_in = pepe_erc20_amount - pepe_uni_v2_reserve_amount

        # get eth amount out
        [_, expect_v2_eth_amount_out] = self.uni_v2_router.functions.getAmountsOut(
            v2_token_amount_in,
            [PEPE_ERC20, WETH_ERC20]
        ).call()

        before_amount = self.weth_erc20.functions.balanceOf(self.account).call()

        self.uni_v2.functions.swap(
            expect_v2_eth_amount_out,
            0,
            self.account,
            "0x",
        ).transact({
            "from": self.account
        })

        after_amount = self.weth_erc20.functions.balanceOf(self.account).call()

        return after_amount - before_amount

    def get_v2_v3_price(self)->List[int]:
        v2_price = self.get_v2_price()
        v3_price = self.get_v3_price()

        return [v2_price, v3_price]

    def get_v2_price(self)->int:
        reserves = self.uni_v2.functions.getReserves().call()
        [pepe_amount, eth_amount] = [reserves[1], reserves[0]]
        return int(pepe_amount/eth_amount)

    def get_v3_price(self)->int:
        slot0 = self.uni_v3.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        sqrt_price = sqrt_price_x96>>96
        return sqrt_price**2

    def do_arbitarge(self, amount_by_eth):
        print()
        amount_in = int(amount_by_eth * ETH)
        [v2_price, v3_price] = self.get_v2_v3_price()
        price_rate = v2_price/v3_price
        print(f"before: {price_rate}, {v2_price}, {v3_price}")

        self.swap_from_v3_to_v2(amount_in)
        amount_out = self.withdraw_from_uni_v2()

        [v2_price, v3_price] = self.get_v2_v3_price()
        price_rate = v2_price/v3_price
        print(f"after : {price_rate}, {v2_price}, {v3_price}")
        profit = amount_out - amount_in
        print(f"profit: {profit:18}, amount_in: {amount_in:18}, amount_out: {amount_out:18}")

    def run_t01(self):
        amount = 0
        delta_amount = Decimal("0.05")
        # amount_in = int(amount_by_eth * ETH)
        while True:
            amount += delta_amount
            self.run_in_state(
                self.do_arbitarge,
                amount 
            )
            if amount > 1.5:
                break

def cur_test():
    start_anvil()
    # restart_anvil()

    tx_runner = TxRunner()
    tx_runner.run_t01()
    # pepe_uni_v2 = UniswapV2(PEPE_UNI_V2) 
    # print(pepe_uni_v2.get_price())

    # pepe_uni_v3 = UniswapV3(PEPE_UNI_V3)
    # print(pepe_uni_v3.get_price())
    # reserves = pepe_uni_v2.get_reserves()
    # print(reserves)

cur_test()