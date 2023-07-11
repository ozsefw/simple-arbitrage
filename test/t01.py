import math
import json
from web3 import Web3

def t01():
    # price = math.log(240956, 1.0001)
    # print(price)
    v3_price = math.pow(1.0001, 240956)
    print(v3_price)
    # v3_price = math.pow(1.0001, 240955)
    # print(v3_price)

    # v2_price = math.pow()
    uni_v2_token0 = 246700985253907116129
    uni_v2_token1 = 6876672226455661486587566009790

    v2_price = float(uni_v2_token1/uni_v2_token0)
    print(v2_price)

    print(v2_price/v3_price)

    # tick = 
    # math.240956

WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
PEPE_UNI_V2 = '0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269'
PEPE_UNI_V3 = '0xd738e6a2ef2846a643dc68092ad0fd7f5a8eb6f8'

def t02():
    # const ETHEREUM_RPC_URL="http://127.0.0.1:8545"
    # with open("abi/erc20.json") as f:
    #     erc20_abi = json.load(f)

    with open("abi/uniswap_v2.json") as f:
        uni_v2_abi = json.load(f)

    with open("abi/uniswap_v3.json") as f:
        uni_v3_abi = json.load(f)

    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

    pepe_uni_v2 = web3.eth.contract(
        address=PEPE_UNI_V2,
        abi=uni_v2_abi,
    )

    reserves = pepe_uni_v2.functions.getReserves().call()
    token0 = reserves[0]
    token1 = reserves[1]

    v2_price = token1/token0
    print(v2_price)

    pepe_uni_v3 = web3.eth.contract(
        address=web3.to_checksum_address(PEPE_UNI_V3),
        abi=uni_v3_abi,
    )
    slot0 = pepe_uni_v3.functions.slot0().call()

    cur_tick = slot0[1]

    v3_price = math.pow(1.0001, cur_tick)
    print(v3_price)

    # symbol = web3.eth.contract(
    #     address=WETH_ERC20,
    #     abi=abi,
    # ).functions.symbol().call()

    # print(symbol)

    # balance = weth_erc20.functions.balanceOf(PEPE_UNI_V2).call()
    # print(balance)

def build_contract(address, abi_path):
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

    with open(abi_path) as f:
        abi = json.load(f)

    return web3.eth.contract(
        web3.to_checksum_address(address),
        abi=abi
    )

def t03():

    # print(reserves)
    pepe_uni_v3 = build_contract(PEPE_UNI_V3, "abi/uniswap_v3.json")
    slot0 = pepe_uni_v3.functions.slot0().call()
    print(slot0)

    pepe_uni_v2 = build_contract(PEPE_UNI_V2, "abi/uniswap_v2.json")
    reserves = pepe_uni_v2.functions.getReserves().call()
    v2_price = reserves[1]/reserves[0]
    print(f"v2_price:   {v2_price}")

    cur_price = (slot0[0]>>96)**2
    print(f"slot price: {cur_price}")

    tick_price = math.pow(1.0001, slot0[1])
    print(f"tick price: {slot0[1]}: {tick_price}")

    tick_price = math.pow(1.0001, slot0[1]+1)
    print(f"tick price: {slot0[1]+1}: {tick_price}")

# def t03():
#     univ2_price = univ2_token1/univ2_token0
#     tick = slot0
#     univ3_price = math.log(tick, 1.0001)

t03()