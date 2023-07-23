from audioop import reverse
from gc import get_referents
import math
import re
from webbrowser import get
from BasicRunner import *

class Runner(BasicTxRunner):
    def __init__(self) -> None:
        super().__init__()

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
    
    # amount_in: eth
    def swap_pepe_from_v3_to_v2(self, amount_in):
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
            "from": self.account
        })

    # amount_in: pepe
    def swap_eth_from_v3_to_v2(self, amount_in):
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
            "from": self.account
        })

    def get_uni_v3_sqrt_price_x96(self):
        slot0 = self.uni_v3.functions.slot0().call()
        sqrt_price_x96 = slot0[0]
        return sqrt_price_x96 >> 96

    def test_liquidity(self, amount_in):
        self.save_anvil_snapshot()
        # self.show_uni_v3_liquidity_and_price()
        delta_eth_amount = amount_in
        sqrt_price_before = self.get_uni_v3_sqrt_price_x96()
        self.swap_pepe_from_v3_to_v2(delta_eth_amount)
        sqrt_price_after = self.get_uni_v3_sqrt_price_x96()
        delta_sqrt_price = 1/sqrt_price_after - 1/sqrt_price_before
        liquidity = delta_eth_amount / delta_sqrt_price
        print(int(liquidity))
        # self.show_uni_v3_liquidity_and_price()
        self.revert_evm()

    def show_uni_v3_liquidity(self):
        liquidity = self.uni_v3.functions.liquidity().call()
        # slot0 = self.uni_v3.functions.slot0().call()
        # cur_price = (slot0[0]**2) >> 192
        print(liquidity)

    def run_01(self):
        # self.show_uni_v3_liquidity_and_price()
        self.show_uni_v3_liquidity()

        delta_eth_amount = 1*10**17 # 0.1 eth
        self.test_liquidity(delta_eth_amount)

        delta_eth_amount = 2*10**17 # 0.2 eth
        self.test_liquidity(delta_eth_amount)

    def get_uni_v3_slot0(self):
        return self.uni_v3.functions.slot0().call()

    def get_uni_v3_tick_bit_map_value(self, tick):
        tick_index = (tick//200)>>8
        # ret = []
        # value = self.uni_v3.functions.tickBitmap(tick_index-1).call()
        # ret.append(value)
        value = self.uni_v3.functions.tickBitmap(tick_index).call()
        # ret.append(value)
        # value = self.uni_v3.functions.tickBitmap(tick_index+1).call()
        # ret.append(value)
        # print(value)
        # return ret 
        return value

    def get_uni_v3_liquidity(self):
        r = self.uni_v3.functions.liquidity().call()
        return r

    # tickBitmap test
    def run_02(self):
        slot0 = self.get_uni_v3_slot0()
        cur_tick = slot0[1]
        print(cur_tick, 1.0001**cur_tick)

        # compressed = cur_tick // 200
        # tick_index = compressed >> 8
        # pos = compressed % 256
        # print(tick_index, pos)
        # print(cur_tick)

        value = self.get_uni_v3_tick_bit_map_value(cur_tick) 
        print(f"{value:0256b}")
        cur_pos = (cur_tick//200) % 256
        print(f"{1<<cur_pos:0256b}")

        print(f"{cur_tick//200*200}")
        print(f"{(cur_tick//200-1)*200}")
        # 0000000100001100010000011110101111010000010110101100000010000011001000000001100000000000100001100011111111110000010010010000010100000000000001000000010010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        # for value in ret:
        #     # print(ret)
        #     print(f"0x{value:064x}")
        # print(f"{byte:b}")
        # for i in range(10):
        #     value = self.uni_v3.functions.tickBitmap(i).call()
        #     # value = self.get_uni_v3_tick_bit_map_value(i)
        #     print(f"{value:0256b}", end="")

    # amount_in: eth
    def swap_pepe_from_v3_to_v2_by_tick(self, next_tick):
        self.init_uni_v3_env(10*ETH)

        sqrt_price_x96 = math.floor(math.sqrt(1.0001**next_tick))<<96
        amount_in = 9*ETH

        self.uni_v3_router.functions.exactInputSingle({
            "tokenIn": WETH_ERC20,
            "tokenOut": PEPE_ERC20,
            "fee": FEE_10000,
            "recipient": PEPE_UNI_V2,
            "deadline": int(time.time())+10*60,
            "amountIn": amount_in,
            "amountOutMinimum": 0,
            "sqrtPriceLimitX96": sqrt_price_x96,
        }).transact({
            "from": self.account
        })

    def test_liquidity_2(self, next_tick):
        self.save_anvil_snapshot()
        # delta_eth_amount = amount_in
        # next_tick = 240801
        self.swap_pepe_from_v3_to_v2(next_tick)

        liquidity = self.get_uni_v3_liquidity()
        # print(liquidity)
        tick = self.get_uni_v3_slot0()[1]
        # print(tick)
        print(f"liquidity: {liquidity}, tick: {tick}")

        self.revert_evm()

    
    # cur_tick: 240956
    # 0000000100001100010000011110101111010000010110101100000010000011001000000001100000000000100001100011111111110000010010010000010100000000000001000000010010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    # 0000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    def run_03(self):
        cur_tick = self.get_uni_v3_slot0()[1]
        liquidity = self.get_uni_v3_liquidity()
        print(f"liquidity: {liquidity}, tick: {cur_tick}")

        # for delta_tick in range(240956-240795):
        #     next_tick = cur_tick - delta_tick
        #     self.test_liquidity_2(next_tick)

        for next_tick in [240801, 240800, 240601, 240600]:
            self.test_liquidity_2(next_tick)

    def get_uni_v3_cur_price(self):
        sqrt_price_x96 = self.get_uni_v3_slot0()[0]
        return sqrt_price_x96 >> 96

    def get_uni_v3_reserves(self):
        liquidity = self.get_uni_v3_liquidity()
        sqrt_price_x96 = self.get_uni_v3_slot0()[0]
        v3_r_x = int((liquidity << 96) / sqrt_price_x96)
        v3_r_y = int(liquidity * sqrt_price_x96 >> 96)

        return [v3_r_x, v3_r_y]

    def get_uni_v2_reserves(self):
        reserve = self.uni_v2.functions.getReserves().call()
        r_x = reserve[0]
        r_y = reserve[1]
        return [r_x, r_y]

    def get_real_profit(self, amount_in):
        pepe_out = self.uni_v3_quoter.functions.quoteExactInputSingle(
            WETH_ERC20,
            PEPE_ERC20,
            10000,
            amount_in,
            0,
        ).call()

        result = self.uni_v2_router.functions.getAmountsOut(
            int(pepe_out*0.99),
            [PEPE_ERC20, WETH_ERC20]
        ).call()

        amount_out = result[1]
        return amount_out - amount_in

    def swap_eth_from_v2_to_sender(self):
        pepe_balance = self.pepe_erc20.functions.balanceOf(PEPE_UNI_V2).call()
        pepe_reserved = self.uni_v2.functions.getReserves().call()[1]

        pepe_amount = pepe_balance - pepe_reserved

        [_, expect_v2_eth_amount_out] = self.uni_v2_router.functions.getAmountsOut(
            pepe_amount,
            [PEPE_ERC20, WETH_ERC20]
        ).call()

        expect_v2_pepe_amount_out = 0
        data = "0x"
        self.uni_v2.functions.swap(
            expect_v2_eth_amount_out,
            expect_v2_pepe_amount_out,
            self.account,
            data,
        ).transact()

        return expect_v2_eth_amount_out

    def do_the_arbitarge(self, amount_in):
        self.save_anvil_snapshot()
        # self.init_uni_v3_env(10**ETH)
        self.swap_pepe_from_v3_to_v2(amount_in)
        amount_out = self.swap_eth_from_v2_to_sender()

        # tick = self.get_uni_v3_slot0()[1]
        # print(f"{tick}")

        self.revert_evm()

        return amount_out - amount_in

    def run_04(self):
        f_v3 = 0.99*0.99
        f_v2 = 0.997

        [v3_r_x, v3_r_y] = self.get_uni_v3_reserves()
        [v2_r_x, v2_r_y] = self.get_uni_v2_reserves()

        r_y = (v3_r_y * v2_r_x * f_v2)/(v3_r_y*f_v2 + v2_r_y)

        r_x = (v3_r_x * v2_r_y)/(v3_r_y * f_v2 + v2_r_y)

        # result = []
        for i in range(2000):
            delta_x = int((0.001 * ETH)*(i+1))

            cacl_profit = int((r_y*f_v3 * delta_x)/(r_x + f_v3 * delta_x) - delta_x)

            # real_profit = self.do_the_arbitarge(delta_x) 
            # print(f"{delta_x/ETH:.2f} Eth, real: {real_profit:18}, cacl: {cacl_profit:18}, rate: {cacl_profit/real_profit:.4f}")

            get_profit = self.get_real_profit(delta_x)
            print(f"{delta_x/ETH:.3f} Eth, real: {get_profit:18}, get: {cacl_profit:18}, {get_profit/cacl_profit:.4f}")

            # print(real_profit)
            # print(f"{delta_x/(10**18):.2f} Eth: cacl: {int(cacl_profit):20}, real: {int(real_profit):20}, rate: {cacl_profit/real_profit:.3f}")
            # result.append((delta_x, cacl_profit, real_profit))

if __name__ == "__main__":
    start_anvil()
    Runner().run_04()