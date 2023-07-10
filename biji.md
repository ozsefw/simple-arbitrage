## 启动anvil

```sh
anvil --fork-url="https://eth-mainnet.nodereal.io/v1/5e75d4566e0048b3b195abbf1de9f366" --fork-block-number=17600000 --compute-units-per-second=300 --no-mining

anvil --fork-url="https://eth-mainnet.nodereal.io/v1/5e75d4566e0048b3b195abbf1de9f366" --fork-block-number=17589010 --compute-units-per-second=300 --chain-id=1
```

## 运行总体流程
 - 初始化crossMarket的信息
 - 每次出现新的区块的时候
  - 马上筛选出可以套利的market_pair
  - 计算每个market_pair的最大利润
  - 生成对应的交易数据
  - 模拟交易执行，模拟gas费的情况
  - bundleExecutor执行交易

## 初始化market的数据
  - 最基本的方法: 通过uniswapFactory.allPairs(number), 获取到某个位置的market的地址
    - [uniswapFactory](https://etherscan.io/address/0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f)
    - [uniswap](https://etherscan.io/address/0x3139Ffc91B99aa94DA8A2dc13f1fC36F9BDc98eE)
  - 通过UniswapFlashQuery合约的方式查询，效率更高

## 套利的计算方式
 - [uniswap搬砖套利的公式](https://medium.com/@pwl94/%E5%A6%82%E4%BD%95%E8%A8%88%E7%AE%97-uniswap-v2-%E6%9C%80%E5%A4%A7%E5%A5%97%E5%88%A9%E6%95%B8%E9%87%8F-9f3cb9e4feb1)

## UniswappyV2EthPairs.ts 
line 215: sellTokensToNextMarket() 的代码的判断有什么作用

## Arbitarge
line 172: 
    - 为什么要设置gasLimit, 如果有利润，gasLimit是多少都无所谓
    - 估算gas的时候，为什么限定100w，运行的时候还会出现大于140w的情况

line 187: 为什么最后要设置为2倍,
line 208: 为什么发送raw_bundle的时候，要在+1，+2两个高度发送