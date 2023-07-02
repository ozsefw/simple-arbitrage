from_user="0x2d2a7d56773ae7d5c7b9f1b57f7be05039447b4d"
tx="0xf45c6ab2879e9262ec0158f0ac340a43c88c13dd14524f114bf94e2d7f8f1fa7"
pepe_univ2="0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269"
weth_erc20="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
pepe_erc20="0xfb66321D7C674995dFcC2cb67A30bC978dc862AD"

default_account_1="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
default_account_2="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

# echo "deposit to pepe_uni's weth"
# cast send --from $default_account_1 --unlocked \
#     $weth_erc20 "deposit()" --value 1ether

echo "getReserves()"
cast call $pepe_univ2 "getReserves()(uint112, uint112, uint32)"

# echo "deposit weth"
# cast send --from $default_account_1 --unlocked \
#     $weth_erc20 "deposit()" --value 1ether

echo "transfer eth to pepe_univ2"
cast send --from $default_account_1 --unlocked \
    $weth_erc20 "transfer(address,uint)" $pepe_univ2 "0x100"

echo "getReserves()"
cast call $pepe_univ2 "getReserves()(uint112, uint112, uint32)"