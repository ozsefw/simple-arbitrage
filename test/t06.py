import math
from BasicRunner import *

class Runner(BasicTxRunner):
    def __init__(self) -> None:
        super().__init__()
        self.f0 = 0.99
        self.f1 = 0.997

        # liquidity = self.get_uni_v3_liquidity()
        # sqrt_price_x96 = self.get_uni_v3_slot0()[0]

        # self.v3_r_x = int((liquidity << 96) / sqrt_price_x96)
        # self.v3_r_y = int(liquidity * sqrt_price_x96 >> 96)
        [self.v3_r_x, self.v3_r_y] = self.get_uni_v3_reserves()
        [self.v2_r_x, self.v2_r_y] = self.get_uni_v2_reserves()

        print(f"({self.v3_r_x}, {self.v3_r_y})")
        print(f"({self.v2_r_x}, {self.v2_r_y})")

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

    def get_v3_amount_out(self, eth_amount_in):
        amount_out = self.uni_v3_quoter.functions.quoteExactInputSingle(
            WETH_ERC20,
            PEPE_ERC20,
            FEE_10000,
            eth_amount_in,
            0,
        ).call()

        return amount_out


    def get_v2_amount_out(self, amount_in):
        [_, amount_out] = self.uni_v2_router.functions.getAmountsOut(
            amount_in,
            [PEPE_ERC20, WETH_ERC20]
        ).call()

        return amount_out

    def get_uni_v3_reserves(self):
        liquidity = self.get_uni_v3_liquidity()
        sqrt_price_x96 = self.get_uni_v3_slot0()[0]
        v3_r_x = int((liquidity << 96) / sqrt_price_x96)
        v3_r_y = int(liquidity * sqrt_price_x96 >> 96)

        return [v3_r_x, v3_r_y]

    def get_profit_from_formula(self, amount_in):
            # xy_amount_out = int(f * amount_in * r_y/(r_x + f*amount_in))
        amount_out_from_v3 = (
            self.f0 * amount_in * self.v3_r_y
                    /
            (self.v3_r_x + self.f0 * amount_in)
        )

        amount_in_to_v2 = int(amount_out_from_v3 * 0.99)
        # print(f"f: to_v2: {amount_in_to_v2}")

        amount_out_from_v2 = (
            self.f1 * amount_in_to_v2 * self.v2_r_x
                    /
            (self.v2_r_y + self.f1 * amount_in_to_v2)
        )

        return int(amount_out_from_v2)

    def get_profit_from_quoter(self, amount_in):
        amount_out_from_v3 = self.get_v3_amount_out(amount_in)
        amount_in_to_v2 = int(amount_out_from_v3*0.99)
        # print(f"q: to_v2: {amount_in_to_v2}")

        amount_out_from_v2 = self.get_v2_amount_out(amount_in_to_v2)
        return amount_out_from_v2
        # return amount_out_from_v2 - amount_in

    def run_01(self):
        f = 0.99
        [r_x, r_y] = self.get_uni_v3_reserves()
        L = self.get_uni_v3_liquidity()

        for i in range(20):
            amount_in = int(0.1*(i+1)*ETH)

            xy_amount_out = int(f * amount_in * r_y/(r_x + f*amount_in))
            quote_amout_out = self.get_v3_amount_out(amount_in)
            print(f"{xy_amount_out}, {quote_amout_out}, {xy_amount_out/quote_amout_out:.3f}")
    
    def run_02(self):
        for i in range(2000):
            amount_in = int(0.001*(i+1)*ETH)

            quoter_amount = self.get_profit_from_quoter(amount_in)
            quoter_profit = quoter_amount - amount_in
            formula_amount = self.get_profit_from_formula(amount_in)
            formula_profit = formula_amount - amount_in

            print(f"{amount_in/ETH:.3f} ETH, quoter: {quoter_profit:20}, formula: {formula_profit:20}, {quoter_profit/formula_profit}")

if __name__ == "__main__":
    start_anvil()
    Runner().run_02()