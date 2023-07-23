import subprocess
import os
import signal
import json
import math
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

class TxBasic:
    def __init__(self) -> None:
        pass
