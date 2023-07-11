import math
import json
import logging
# import numpy as np
from decimal import *
from web3 import Web3

WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
PEPE_ERC20 = '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD'

PEPE_UNI_V2 = '0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269'
PEPE_UNI_V3 = '0xd738e6a2ef2846a643dc68092ad0fd7f5a8eb6f8'

UNI_V3_QUOTER = "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6"
UNI_V2_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

logging.basicConfig(level=logging.INFO)

class ArbiTest:
    V3_FEE = 10000

    def __init__(self):
        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        # self.pepe_erc20_addr = PEPE_ERC20
        # self.weth_erc20_addr = WETH_ERC20

        with open("abi/uniswap_v3_quoter.json") as f:
            uni_v3_quoter_abi = json.load(f)
        
        with open("abi/uniswap_v2_router.json") as f:
            uni_v2_router_abi = json.load(f)

        with open("abi/uniswap_v3.json") as f:
            uniswap_v3_abi = json.load(f)

        self.uni_v3_quoter = web3.eth.contract(
            web3.to_checksum_address(UNI_V3_QUOTER),
            abi = uni_v3_quoter_abi,
        )

        self.uni_v2_router = web3.eth.contract(
            web3.to_checksum_address(UNI_V2_ROUTER),
            abi = uni_v2_router_abi,
        )

        self.uni_v3 = web3.eth.contract(
            web3.to_checksum_address(PEPE_UNI_V3),
            abi = uniswap_v3_abi,
        )

    def get_arbitarge_profit(self, qty):
        pepe_out_from_v3 = self.get_pepe_out_from_v3(qty)
        # logging.info(f"pepe amount out from v3: {pepe_out_from_v3}")

        pepe_in_to_v2 = pepe_out_from_v3 - (pepe_out_from_v3//100)
        # logging.info(f"pepe amount in to v2: {pepe_in_to_v2}")

        eth_out_from_v2 = self.get_eth_out_from_v2(pepe_in_to_v2)
        # logging.info(f"eth amount out from v2: {eth_out_from_v2}")

        profit = eth_out_from_v2 - qty
        return profit

    # "function quoteExactInputSingle(address,address,uint24,uint256,uint160) view returns (uint256)"
    def get_pepe_out_from_v3(self, eth_amount_in):
        amount_out = self.uni_v3_quoter.functions.quoteExactInputSingle(
            WETH_ERC20,
            PEPE_ERC20,
            self.V3_FEE,
            eth_amount_in,
            0,
        ).call()
        return amount_out

    # "function getAmountsOut(uint256, address[]) view returns (uint256[])",
    def get_eth_out_from_v2(self, pepe_amount_in):
        result = self.uni_v2_router.functions.getAmountsOut(
            pepe_amount_in,
            [PEPE_ERC20, WETH_ERC20]
        ).call()
        eth_amount_out = result[1]
        return eth_amount_out
    
    def uniswap_v3_amount_test(self):
        (liquidity, sqrt_price) = self.get_uniswap_v3_liqudity_and_sqrt_price()

        before_eth = liquidity / sqrt_price
        before_pepe = liquidity * sqrt_price

        before_value = Decimal(before_eth * before_pepe)

        eth_amount_in = 10**18
        pepe_amount_out = self.uni_v3_quoter.functions.quoteExactInputSingle(
            WETH_ERC20,
            PEPE_ERC20,
            10000,
            eth_amount_in,
            0
        ).call()

        after_eth = before_eth + eth_amount_in
        after_pepe = before_pepe - pepe_amount_out

        after_value = Decimal(after_eth * after_pepe)
        print(f"after: {after_value}, before: {before_value}, rate: {after_value/before_value}")

    def get_uniswap_v3_liqudity_and_sqrt_price(self):
        liquidity = self.uni_v3.functions.liquidity().call()
        slot0 = self.uni_v3.functions.slot0().call()
        sqrt_price = slot0[0]>>96

        return (liquidity, sqrt_price)

def test02():
    abr_test = ArbiTest()
    abr_test.uniswap_v3_amount_test()

def test01():
    abr_test = ArbiTest()

    amount_in = int(Decimal("0.7")*(10**18))
    delta_amount = int(Decimal("0.05")*(10**18))
    max_qty = int(Decimal("1.5")*10**18)

    while amount_in < max_qty:
        amount_in += delta_amount
        profit = abr_test.get_arbitarge_profit(amount_in)
        print(f"profit: {profit:18d}, amount_in: {Decimal(amount_in)/10**18:.3f}")
    # print(profit, amount_in)

test02()
# def amount_test():
#     (liqudity, sqrt_price) = get_liqudity_and_sqrt_price()

#     return