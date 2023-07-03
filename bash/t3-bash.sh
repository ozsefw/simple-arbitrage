from_user="0x2d2a7d56773ae7d5c7b9f1b57f7be05039447b4d"
tx="0xf45c6ab2879e9262ec0158f0ac340a43c88c13dd14524f114bf94e2d7f8f1fa7"
pepe_univ2="0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269"
weth_erc20="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
pepe_erc20="0xfb66321D7C674995dFcC2cb67A30bC978dc862AD"

default_account_1="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
default_account_2="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

univ2_router="0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
uni_v2_facotry='0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'

# reset_anvil(){
#     curl -X POST \
#         -H "Content-Type: application/json" \
#         --data '{"jsonrpc": "2.0", "id": 1, "method": "anvil_reset", "params": [{"forking": {"jsonRpcUrl": "http://127.0.0.1:<PORT>", "blockNumber": 176000000}}]}' 127.0.0.1:<PORT>
# }

start_anvil(){
    anvil \
        --fork-url "https://eth-mainnet.nodereal.io/v1/5e75d4566e0048b3b195abbf1de9f366" \
        --fork-block-number 17600000 \
        --fork-chain-id 1 \
        --no-mining
}

deposit_weth(){
    # cast call will fail, return 0x
    # cast call --value 1ether --from $default_account_1 $weth_erc20 "deposit()" 

    cast send --from $default_account_1 --unlocked \
        $weth_erc20 "deposit()" --value 1ether

    cast call $weth_erc20 "balanceOf(address)(uint)" $default_account_1
}

swap_test(){
    deposit_weth $default_account_1
    amout_out=5562375595765
    cast call $pepe_univ2 "swap(uint,uint,address,bytes)" 0 $amout_out $default_account_2 "0x" 
}

# swap_test

get_uni_v2_amout_out(){
    amount_out=`cast call $univ2_router "getAmountOut(uint,uint,uint)(uint)" $1 $2 $3`
    echo $amount_out
}

get_uni_v2_amout_in(){
    amount_out=`cast call $univ2_router "getAmountIn(uint,uint,uint)(uint)" $1 $2 $3`
    echo $amount_out
}

router_test(){
    # IFS=' '
    result=(`cast call $pepe_univ2 "getReserves()(uint,uint,uint)"`)
    # echo "-" $result "-"
    reserve_in=${result[0]}
    echo $reserve_in

    reserve_out=${result[1]}
    echo $reserve_out

    amount_out=`cast call $univ2_router "getAmountOut(uint,uint,uint)(uint)" 100 $reserve_in $reserve_out`
    echo $amount_out
    # return $amount_out
    # return $amount_out
}

router_test2(){
    reserve_in=1000000
    reserve_out=1000000
    amount_in=10000

    amount_out=`cast call $univ2_router "getAmountOut(uint,uint,uint)(uint)" $amount_in $reserve_in $reserve_out`
    echo $amount_out
}

router_test3(){
    cast call $univ2_router "getAmountsOut(uint,address[])(uint[])" 10000 [$weth_erc20,$pepe_erc20]
}
