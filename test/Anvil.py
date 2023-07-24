import subprocess
import os
import signal
import time

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
    time.sleep(5)


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
    time.sleep(5)