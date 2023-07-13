from cgitb import reset
import json
import logging
import requests
import time
from decimal import *
from web3 import Web3

WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
PEPE_ERC20 = '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD'

PEPE_UNI_V2 = '0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269'
PEPE_UNI_V3 = '0xD738E6a2EF2846a643dC68092AD0fd7F5a8EB6f8'
FEE_10000 = 10000

UNI_V3_QUOTER = "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6"
UNI_V3_ROUTER = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
UNI_V2_ROUTER = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

ANVIL_USER  = [
    "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"
]

ANVIL_URL="http://127.0.0.1:8545"

logging.basicConfig(level=logging.INFO)

class ArbiTest:
    # V3_FEE = 10000

    def __init__(self):
        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        # self.pepe_erc20_addr = PEPE_ERC20
        # self.weth_erc20_addr = WETH_ERC20

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
            10000,
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

    def show_uniswap_v3_info(self):
        slot0 = self.uni_v3.functions.slot0().call()
        sqrt_price = slot0[0]
        # print(f"slot0: {slot0}")

        liquidity = self.uni_v3.functions.liquidity().call()
        # print(f"liquidity: {liquidity}")

        pepe_amount = liquidity*(sqrt_price>>96)
        eth_amount = int(liquidity/(sqrt_price>>96))

        price = (sqrt_price >> 96)**2
        # print(f"v3_price: {price}")

        print(f"pepe: {pepe_amount}, eth: {eth_amount}, v3_price: {price}")
    
    def show_uniswap_v3_info2(self):
        pepe_amount = self.pepe_erc20.functions.balanceOf(
            Web3.to_checksum_address(PEPE_UNI_V3)
        ).call()
        eth_amount = self.weth_erc20.functions.balanceOf(
            Web3.to_checksum_address(PEPE_UNI_V3)
        ).call()

        print("value from erc20")
        print(f"pepe: {pepe_amount}, eth: {eth_amount}, price: {pepe_amount/eth_amount}")

        liquidity = self.uni_v3.functions.liquidity().call()
        slot0 = self.uni_v3.functions.slot0().call()

        sqrt_price_x96 = slot0[0]
        sqrt_price = sqrt_price_x96>>96
        pepe_amount = liquidity*sqrt_price
        eth_amount = int(liquidity/sqrt_price)
        price = sqrt_price**2
        print(f"value from slot0: {price}")
        # print(f"pepe: {pepe_amount}, eth: {eth_amount}, price: {pepe_amount/eth_amount}")
    
    def show_uniswap_v2_info(self):
        result = self.uni_v2.functions.getReserves().call()
        pepe_amount = result[1]
        eth_amount = result[0]
        price = pepe_amount/eth_amount
        print(f"pepe: {pepe_amount}, eth: {eth_amount}, v2_price: {price}")

    def uni_v3_quote_test(self):
        # reset_anvil()

        amount_in = self.uni_v3_quoter.functions.quoteExactOutputSingle(
            WETH_ERC20,
            PEPE_ERC20,
            FEE_10000,
            1<<250,
            13443882501629929000910181338733598
        ).call()

        print(amount_in)
    
    def get_v2_price(self):
        reserves = self.uni_v2.functions.getReserves().call()
        token1 = reserves[1]
        token0 = reserves[0]
        price = token1/token0
        return price
    
    def get_v3_price(self):
        slot0 = self.uni_v3.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        return (sqrt_price_x96>>96)**2
    
    def arbitarge_test_01(self):
        qty = 0
        delta_qty = int(0.2*10**18)

        while True:
            qty += delta_qty
            profit = self.get_arbitarge_profit(qty)
            v3_price = self.get_v3_price()
            v2_price = self.get_v2_price()
            print(f"profit: {profit}, v3_price: {v3_price}, v2_price: {v2_price}")

            if v3_price < v2_price:
                break
    
    def deposit_test(self, reset: bool):
        if reset:
            reset_anvil()

        from_user = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

        result = self.weth_erc20.functions.deposit().transact({
            "from": from_user,
            "value": 1*10**18
        })
        print(result.hex())

        balance = self.weth_erc20.functions.balanceOf(from_user).call()
        print(f"balance: {balance}")
    
    def uniswap_v3_swap_test(self, reset: bool):
        if reset:
            reset_anvil()

        from_user = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        amount_in = 1057147387365399552
        amount_out_min = 0
        deadline = int(time.time()) + 10*60
        # print(deadline)
        sqrt_price_x96 = 13443882501629929000910181338733598

        v2_pepe_before = self.pepe_erc20.functions.balanceOf(PEPE_UNI_V2).call()

        self.weth_erc20.functions.approve(
            UNI_V3_ROUTER,
            amount_in
        ).transact({
            "from": from_user,
        })

        self.uni_v3_router.functions.exactInputSingle({
            "tokenIn": WETH_ERC20,
            "tokenOut": PEPE_ERC20,
            "fee": FEE_10000,
            "recipient": PEPE_UNI_V2,
            "deadline": deadline,
            "amountIn": amount_in,
            "amountOutMinimum": amount_out_min,
            "sqrtPriceLimitX96": sqrt_price_x96,
        }).transact({
            "from": from_user,
        })

        v2_pepe_after = self.pepe_erc20.functions.balanceOf(PEPE_UNI_V2).call()
        print(f"before: {v2_pepe_before}, after: {v2_pepe_after}")
    
    def arbitarge_test_02(self, reset: bool):
        if reset:
            reset_anvil()

        from_user = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        to_user = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"

        eth_amount_out = 1068308522694445586
        pepe_amount_out = 0
        data = "0x"

        v2_eth_before = self.weth_erc20.functions.balanceOf(PEPE_UNI_V2).call()

        self.uni_v2.functions.swap(
            eth_amount_out,
            pepe_amount_out,
            to_user,
            data,
        ).transact({
            "from": from_user
        })

        v2_eth_after = self.weth_erc20.functions.balanceOf(PEPE_UNI_V2).call()
        print(f"before: {v2_eth_before}, after: {v2_eth_after}")

    def get_uni_v2_and_v3_price(self):
        reserve = self.uni_v2.functions.getReserves().call()
        pepe_amount = reserve[1]
        eth_amount = reserve[0]
        v2_price = pepe_amount/eth_amount

        slot0 = self.uni_v3.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        v3_price = (sqrt_price_x96>>96)**2

        return (int(v2_price), v3_price)

    def get_uni_v2_reserves(self):
        reserves = self.uni_v2.functions.getReserves().call()
        pepe_amount = reserves[1]
        eth_amount = reserves[0]
        return (pepe_amount, eth_amount)

    def do_the_03_tx(self, amount_in):
        v2_pepe_amount_before = self.pepe_erc20.functions.balanceOf(PEPE_UNI_V2).call()
        # print(f"pepe amount before: {v2_pepe_amount_before}")

        self.weth_erc20.functions.deposit().transact({
            "from": ANVIL_USER[0],
            "value": 10*10**18
        })

        # anvil_balance = self.weth_erc20.functions.balanceOf(ANVIL_USER[0]).call()
        # print(f"{anvil_balance}")

        self.weth_erc20.functions.approve(
            UNI_V3_ROUTER,
            amount_in
        ).transact({
            "from": ANVIL_USER[0],
        })
        # print("approve router done")

        self.uni_v3_router.functions.exactInputSingle({
            "tokenIn": WETH_ERC20,
            "tokenOut": PEPE_ERC20,
            "fee": FEE_10000,
            "recipient": PEPE_UNI_V2,
            "deadline": int(time.time())+10*60,
            "amountIn": amount_in,
            "amountOutMinimum": 0,
            "sqrtPriceLimitX96": 0,
            # "sqrtPriceLimitX96": 13443882501629929000910181338733598,
        }).transact({
            "from": ANVIL_USER[0],
        })

        v2_pepe_amount_after = self.pepe_erc20.functions.balanceOf(PEPE_UNI_V2).call()
        # print(f"pepe amount after: {v2_pepe_amount_before}")

        v2_pepe_amount_in = v2_pepe_amount_after - v2_pepe_amount_before
        # print(f"uni_v2 pepe amount recv: {v2_pepe_amount_in}")

        [_, expect_v2_eth_amount_out] = self.uni_v2_router.functions.getAmountsOut(
            v2_pepe_amount_in,
            [PEPE_ERC20, WETH_ERC20]
        ).call()

        # print(f"uni_v2 expect eth amount out: {expect_v2_eth_amount_out}")
        # swap out eth from uni_v2
        expect_v2_pepe_amount_out = 0
        data = "0x"
        self.uni_v2.functions.swap(
            expect_v2_eth_amount_out,
            expect_v2_pepe_amount_out,
            ANVIL_USER[0],
            data,
        ).transact({
            "from": ANVIL_USER[0]
        })
        return expect_v2_eth_amount_out


    def arbitarge_test_03(self):
        reset_anvil()

        amount_in = 1057147387365399552

        (v2_price_before, v3_price_before) = self.get_uni_v2_and_v3_price()
        amount_out = self.do_the_03_tx(amount_in)
        (v2_price_after, v3_price_after) = self.get_uni_v2_and_v3_price()

        profit = amount_out - amount_in
        print(f"profit: {profit}, amount_in: {amount_in}")
        print(f"v3_price: before: {v3_price_before}, after: {v3_price_after}")
        print(f"v2_price: before: {v2_price_before}, after: {v2_price_after}")

    def arbitarge_test_04(self):
        amount_in = int(0.2*10**18)
        delta_amount = int(0.2*10**18)

        while True:
            reset_anvil()
            # (v2_price_before, v3_price_before) = self.get_uni_v2_and_v3_price()
            amount_in += delta_amount
            amount_out = self.do_the_03_tx(amount_in)
            profit = amount_out - amount_in
            print(f"profit: {profit:20}")
            # print(f"profit: {profit:20}, amount_in: {amount_in}, amount_out: {amount_out}")

            (v2_price_after, v3_price_after) = self.get_uni_v2_and_v3_price()
            print(f"v2_price: {v2_price_after}, v3_price: {v3_price_after}")

            if v3_price_after < v2_price_after:
                break

def reset_anvil():
    data = {
        "jsonrpc":"2.0",
        "method":"anvil_reset",
        "params":[{
            "forking": {
                "jsonRpcUrl": "https://eth-mainnet.alchemyapi.io/v2/Lc7oIGYeL_QvInzI0Wiu_pOZZDEKBrdf",
                "blockNumber": 17589010,
            }
        }],
        "id":1
    }
    r = requests.post(url=ANVIL_URL, json=data)
    if r.status_code != 200:
        raise Exception(r.content)

def do_the_tx(display: bool):
    # url = 'http://127.0.0.1:8545'
    data =  {
        "jsonrpc":"2.0",
        "method":"eth_sendUnsignedTransaction",
        "params":[{
            "from": "0x76F36d497b51e48A288f03b4C1d7461e92247d5e",
            "to": "0x2d2A7d56773ae7d5c7b9f1B57f7Be05039447B4D",
            "data": "0x000eabbdf2a3259c00d738e6a2ef2846a643dc68092ad0fd7f5a8eb6f8000061e87d6a5807f00000000000076a3e1500f3110d8f4445d396a3d7ca6d0ca269000ed364d8161c1980010c631300"
        }],
        "id":1
    }
    r = requests.post(url=ANVIL_URL, json=data)
    if r.status_code != 200:
        raise Exception(r.content)
    if display:
        print("execute tx: {}", r.content)

def cur_test():

    # reset_anvil()
    abr_test = ArbiTest()
    # abr_test.deposit_test(False)
    # abr_test.uniswap_v3_swap_test(False)
    abr_test.arbitarge_test_04()
    # abr_test.arbitarget_test_01()
    # abr_test.uni_v3_quote_test()

def test02():
    reset_anvil()
    abr_test = ArbiTest()
    print("before tx")
    abr_test.show_uniswap_v3_info2()
    # abr_test.show_uniswap_v3_basic()
    # abr_test.show_uniswap_v2_info()
    do_the_tx(False)

    print("after tx")
    abr_test.show_uniswap_v3_info2()
    # abr_test.show_uniswap_v3_basic()
    # abr_test.show_uniswap_v2_info()
    return

def test01():
    abr_test = ArbiTest()

    amount_in = int(Decimal("0.7")*(10**18))
    delta_amount = int(Decimal("0.05")*(10**18))
    max_qty = int(Decimal("1.5")*10**18)

    while amount_in < max_qty:
        amount_in += delta_amount
        profit = abr_test.get_arbitarge_profit(amount_in)
        print(f"profit: {profit:18d}, amount_in: {Decimal(amount_in)/10**18:.3f}")

# reset_anvil()
cur_test()