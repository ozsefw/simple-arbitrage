from_user="0x2d2a7d56773ae7d5c7b9f1b57f7be05039447b4d"
tx="0xf45c6ab2879e9262ec0158f0ac340a43c88c13dd14524f114bf94e2d7f8f1fa7"
pepe_univ2="0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269"
weth_erc20="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
pepe_erc20="0xfb66321D7C674995dFcC2cb67A30bC978dc862AD"

default_account_1="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
default_account_2="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"


# cast send --from $from_user --unlocked \
#     --priority-gas-price \
#     $pepe_univ2 "swap(uint256,uint256,address,bytes)" 0 100000000000 $default_account_1 "[]"

# fun_name="swap(uint256,uint256,address,bytes)"
# echo $fun_name
# cast calldata $fun_name 0 1000000 $default_account_1 "0x"

# echo "getReserves()"
# cast call $pepe_univ2 "getReserves()(uint112, uint112, uint32)"

# echo "getBalance() pepe_univ2"
# eth_amount="$(cast call $weth_erc20 "balanceOf(address)(uint)" $pepe_univ2)";
# pepe_amount="$(cast call $pepe_erc20 "balanceOf(address)(uint)" $pepe_univ2)";
# echo $eth_amount
# echo $pepe_amount

# echo "getBalance() from_user"
# eth_amount="$(cast call $weth_erc20 "balanceOf(address)(uint)" $from_user)";
# pepe_amount="$(cast call $pepe_erc20 "balanceOf(address)(uint)" $from_user)";

# echo $eth_amount
# echo $pepe_amount

# cast calldata "balanceOf(address)(uint)" $from_user
# 0x70a082310000000000000000000000002d2a7d56773ae7d5c7b9f1b57f7be05039447b4d

# swap_data="$(cast calldata "swap(uint,uint,address,bytes)" "0" "0x100000000" $default_account_1 "0x")"
# echo $swap_data

# cast call $pepe_erc20 $swap_data --from $from_user 

# 10.065897298424708376
#  7.632789410651257211

# swap_data="$(cast calldata "swap(uint,uint,address,bytes)" "0" "10000000000" $weth_erc20 "0x")"

# # 向weth里面存入1个eth
# echo "deposit to pepe_uni's weth"
# cast send --from $default_account_1 --unlocked \
#     $weth_erc20 "deposit()" --value 1ether

# # echo "getReserves()"
# # cast call $pepe_univ2 "getReserves()(uint112, uint112, uint32)"

cast send --from $default_account_2 --unlocked \
    $weth_erc20 "transfer(address,uint)" $pepe_univ2 "100"

# echo "getReserves()"
# cast call $pepe_univ2 "getReserves()(uint112, uint112, uint32)"

# echo "getBalance() pepe_univ2"
# eth_amount="$(cast call $weth_erc20 "balanceOf(address)(uint)" $pepe_univ2)";
# pepe_amount="$(cast call $pepe_erc20 "balanceOf(address)(uint)" $pepe_univ2)";
# echo $eth_amount
# echo $pepe_amount

# cast call $weth_erc20 "balanceOf(address)(uint)" $default_account_2

echo "balance before"
cast call $pepe_erc20 "balanceOf(address)(uint)" $default_account_2

cast send --from $default_account_1 --unlocked \
    $pepe_univ2 "swap(uint,uint,address,bytes)" "0" "1000000" $default_account_2 "0x"

echo "balance after"
cast call $pepe_erc20 "balanceOf(address)(uint)" $default_account_2

# cast call $pepe_univ2 "swap(uint,uint,address,bytes)" "10" "0x0" $default_account_1 "0x" 
    
# 08c379a0
# 0000000000000000000000000000000000000000000000000000000000000020
# 0000000000000000000000000000000000000000000000000000000000000024
# 556e697377617056323a20494e53554646494349454e545f494e5055545f414d
# 4f554e5400000000000000000000000000000000000000000000000000000000

# cast send CONTRACT_ADDRESS "updatePrices((address,uint256,uint256)[])" "[(ADDR,100,200),(ADDR,300,400)]" --rpc-url RPC_URL --private-key=P_KEY


# fun_name="swap(uint,uint,address,bytes)"
# echo $fun_name
# cast calldata $fun_name 0 1000000 $default_account_1 "0x"

# pepe_token="0x6982508145454Ce325dDbE47a25d4ec3d2311933"
# pepe_contract="0xa43fe16908251ee70ef74718545e4fe6c5ccec9f"
# pepe_univ3="0xD738E6a2EF2846a643dC68092AD0fd7F5a8EB6f8"

# priv_key="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"


# cast call $pepe_univ2 "getReserves()(uint256,uint256)"
# cast call $pepe_univ3 "getReserves()(uint256,uint256)"
# cast call $weth_erc20 "balanceOf(address)(uint)" $default_account_1
# cast call $weth_erc20 "balanceOf(address)(uint)" $from_user