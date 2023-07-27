from BasicRunner import *

def do_the_tx_01(display=True):
    # # url = 'http://127.0.0.1:8545'
    # data = {
    #     "jsonrpc":"2.0",
    #     "method":"anvil_impersonateAccount",
    #     "params":[
    #         "0x76F36d497b51e48A288f03b4C1d7461e92247d5e"
    #     ],
    #     "id":1
    # }
    # r = requests.post(url=ANVIL_URL, json=data)
    # if r.status_code != 200:
    #     raise Exception(r.content)
    # if display:
    #     print("execute tx: {}", r.content)

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

    tx_hash = json.loads(r.content)["result"]
    print(tx_hash)

    data =  {
        "jsonrpc":"2.0",
        "method":"eth_getTransactionReceipt",
        "params":[
            tx_hash
        ],
        "id":1
    }

    # r = requests.post(url=ANVIL_URL, json=data)
    # if r.status_code != 200:
    #     raise Exception(r.content)
    # if display:
    #     print("execute tx: {}", r.content)

def do_tx_02(display=False):
    tx_params_list = [
        {
            "from": "0x37f3D6eAB4D82909536D3DABe7D31b1E04c3602a",
            "to": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
            "data": "0x791ac94700000000000000000000000000000000000000000001c63b595dc8bfd75b20e800000000000000000000000000000000000000000000000004cfbd5d2b89800000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000037f3d6eab4d82909536d3dabe7d31b1e04c3602a000000000000000000000000000000000000000000000000000000011f018be60000000000000000000000000000000000000000000000000000000000000002000000000000000000000000bf6693cdc1ba57d2e9a2d0c4bc1fb27c927bb9ba000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
        },
        {
            "from": "0xf53A4856db59B289DeBA05A44Ca83E94Ac3Cc90A",
            "to": "0x1111111254fb6c44bAC0beD2854e76F90643097d",
            "data": "0x7c0252000000000000000000000000002b6e7fbdf8739ad39f73909fa4af7dd7abde076e000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000001800000000000000000000000003b803cd0515dcff3ac958f2f11af168b85147136000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000a193fbd522b698ce8ce3afee6b1c51ac5f1f7f08000000000000000000000000f53a4856db59b289deba05a44ca83e94ac3cc90a0000000000000000000000000000000000000000000000000004818e541a8f650000000000000000000000000000000000000000000000000dd9795bbce9e36f00000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e30000000000000000000000000000000000000000000000a500008f00005300206ae4071198002dc6c0a193fbd522b698ce8ce3afee6b1c51ac5f1f7f0800000000000000000000000000000000000000000000000000000000000000013b803cd0515dcff3ac958f2f11af168b851471364101c02aaa39b223fe8d0a0e5c4f27ead9083c756cc200042e1a7d4d0000000000000000000000000000000000000000000000000000000000000000c0611111111254fb6c44bac0bed2854e76f90643097d0000000000000000000000000000000000000000000000000004818e541a8f650000000000000000000000000000000000000000000000000000000000e26b9977"
        },
        {
            "from": "0x76F36d497b51e48A288f03b4C1d7461e92247d5e",
            "to": "0x2d2A7d56773ae7d5c7b9f1B57f7Be05039447B4D",
            "data": "0x000eabbdf2a3259c00d738e6a2ef2846a643dc68092ad0fd7f5a8eb6f8000061e87d6a5807f00000000000076a3e1500f3110d8f4445d396a3d7ca6d0ca269000ed364d8161c1980010c631300"
        }
    ]

    for tx_param in tx_params_list:
        data =  {
            "jsonrpc":"2.0",
            "method":"eth_sendUnsignedTransaction",
            "params":[tx_param],
            "id":1
        }
        r = requests.post(url=ANVIL_URL, json=data)
        if r.status_code != 200:
            raise Exception(r.content)

        tx_hash = json.loads(r.content)["result"]
        print(tx_hash)

class Runner(BasicTxRunner):
    def __init__(self) -> None:
        super().__init__()

    def run_01(self):
        # self.save_anvil_snapshot()
        do_tx_02()
        # self.revert_evm()

if __name__ == "__main__":
    start_anvil(17589010)
    Runner().run_01()