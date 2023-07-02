import * as _ from "lodash";
import { ETHER } from "./utils";
import { UNISWAP_FACTORY_ABI, UNISWAP_PAIR_ABI, UNISWAP_QUERY_ABI } from "./abi";
import { Contract, providers, Wallet } from "ethers";
import { UniswappyV2EthPair } from "./UniswappyV2EthPair";
// import { UNISWAP_LOOKUP_CONTRACT_ADDRESS, WETH_ADDRESS } from "./addresses";
// import { FACTORY_ADDRESSES } from "./addresses";

const UNISWAP_LOOKUP_CONTRACT_ADDRESS = '0x5EF1009b9FCD4fec3094a5564047e190D72Bd511'
const WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2';
const SUSHISWAP_FACTORY_ADDRESS = '0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac';
const UNISWAP_FACTORY_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f';
// const CRO_FACTORY_ADDRESS = "0x9DEB29c9a4c7A88a3C0257393b7f3335338D9A9D";
// const ZEUS_FACTORY_ADDRESS = "0xbdda21dd8da31d5bee0c9bb886c044ebb9b8906a";
// const LUA_FACTORY_ADDRESS = "0x0388c1e0f210abae597b7de712b9510c6c36c857";

const FACTORY_ADDRESSES = [
//   CRO_FACTORY_ADDRESS,
//   ZEUS_FACTORY_ADDRESS,
//   LUA_FACTORY_ADDRESS,
  SUSHISWAP_FACTORY_ADDRESS,
  UNISWAP_FACTORY_ADDRESS,
]


// const ETHEREUM_RPC_URL = process.env.ETHEREUM_RPC_URL || "http://127.0.0.1:8545"
const ETHEREUM_RPC_URL = "https://eth-mainnet.public.blastapi.io"
// const ETHEREUM_RPC_URL = "https://rpc.payload.de"

const provider = new providers.StaticJsonRpcProvider(ETHEREUM_RPC_URL);

async function get_pair_t1() {
  // const markets = await UniswappyV2EthPair.getUniswapMarketsByToken(provider, FACTORY_ADDRESSES);
  // console.log(markets);

  const uniswapQuery = new Contract(UNISWAP_LOOKUP_CONTRACT_ADDRESS, UNISWAP_QUERY_ABI, provider);

  const factoryAddress = UNISWAP_FACTORY_ADDRESS;
  // const factoryAddress = SUSHISWAP_FACTORY_ADDRESS;

  const pairs: Array<Array<string>> = (
    await uniswapQuery.functions.getPairsByIndexRange(
      factoryAddress, 
      0,
      10,
    )
  )[0];

  console.log(pairs);

  // let result = await uniswapQuery.functions.getReservesByPairs(
  //     [factoryAddress],
  //   );
  // console.log(result);
}

async function contract_test() {
  const uniswapFactoryQuery = new Contract(
    UNISWAP_FACTORY_ADDRESS,
    UNISWAP_FACTORY_ABI,
    provider
  );

  const poolAddr :Array<string> = (await uniswapFactoryQuery.functions.allPairs(0));
  console.log(poolAddr);

  const uniswapPairQuery = new Contract(
    poolAddr[0],
    UNISWAP_PAIR_ABI,
    provider
  )

  const token0 = await uniswapPairQuery.functions.token0();
  console.log(token0);
}

async function provider_test() {
  provider.on('block', async (blockNumber) => {
    console.log("new block: ", blockNumber);
  })
}

const BATCH_COUNT_LIMIT = 1;
const UNISWAP_BATCH_SIZE = 5;

async function getpair_t2() {
  const uniswapQuery = new Contract(UNISWAP_LOOKUP_CONTRACT_ADDRESS, UNISWAP_QUERY_ABI, provider);
  const factoryAddress = UNISWAP_FACTORY_ADDRESS;

  let pairs = new Array<Array<string>>();
  for(let i = 0; i< BATCH_COUNT_LIMIT * UNISWAP_BATCH_SIZE; i += UNISWAP_BATCH_SIZE){
    console.log("get pair, %d->%d", i, i+UNISWAP_BATCH_SIZE-1);
    const batch_pairs: Array<Array<string>> = (
      await uniswapQuery.functions.getPairsByIndexRange(
        factoryAddress, i, i+UNISWAP_BATCH_SIZE,
      ))[0];

    // console.log(batch_pairs);
    pairs = pairs.concat(batch_pairs);
  }

  console.log(pairs);
}

async function getUniswappyMarkets(provider: providers.JsonRpcProvider, factoryAddress: string): Promise<Array<UniswappyV2EthPair>> {
  const uniswapQuery = new Contract(UNISWAP_LOOKUP_CONTRACT_ADDRESS, UNISWAP_QUERY_ABI, provider);

  const marketPairs = new Array<UniswappyV2EthPair>()
  for (let i = 0; i < BATCH_COUNT_LIMIT * UNISWAP_BATCH_SIZE; i += UNISWAP_BATCH_SIZE) {
    const pairs: Array<Array<string>> = (await uniswapQuery.functions.getPairsByIndexRange(factoryAddress, i, i + UNISWAP_BATCH_SIZE))[0];
    for (let i = 0; i < pairs.length; i++) {
      const pair = pairs[i];
      const marketAddress = pair[2];
      // let tokenAddress: string;

      if (pair[0]!=WETH_ADDRESS && pair[1] != WETH_ADDRESS){
        continue;
      }
      // if (pair[0] === WETH_ADDRESS) {
      //   tokenAddress = pair[1]
      // } else if (pair[1] === WETH_ADDRESS) {
      //   tokenAddress = pair[0]
      // } else {
      //   continue;
      // }
      // if (!blacklistTokens.includes(tokenAddress)) {
        const uniswappyV2EthPair = new UniswappyV2EthPair(marketAddress, [pair[0], pair[1]], "");
        marketPairs.push(uniswappyV2EthPair);
      // }
    }
    if (pairs.length < UNISWAP_BATCH_SIZE) {
      break
    }
  }

  console.log("pairs in one market: %s, %d", factoryAddress, marketPairs.length);

  return marketPairs
}

async function getpair_t3() {
  const factory_list = FACTORY_ADDRESSES;
  const allPairs = await Promise.all(
    _.map(factory_list, factory_address=>
        getUniswappyMarkets(provider, factory_address))
  )

  console.log("allPairs: %d", allPairs.length);

  const marketsByTokenAll = _.chain(allPairs)
      .flatten()
      .groupBy(pair => pair.tokens[0] == WETH_ADDRESS ? pair.tokens[1]: pair.tokens[0])
      .value();

  console.log(marketsByTokenAll);

  const allMarketPairs = _.chain(
    _.pickBy(marketsByTokenAll, a => a.length > 1) // weird TS bug, chain'd pickBy is Partial<>
  )
    .values()
    .flatten()
    .value()

  console.log(allMarketPairs);
}

async function t1_test_reserves() {
  const factory_list = FACTORY_ADDRESSES;

  const allPairs = await Promise.all(
    _.map(factory_list, factory__address=>
        getUniswappyMarkets(provider, factory__address))
  )

  const allMarketPairs = _.chain(allPairs).flatten().value();

  await UniswappyV2EthPair.updateReserves(provider, allMarketPairs);


  const marketsByToken = _.chain(allMarketPairs)
    .filter(pair => (pair.getBalance(WETH_ADDRESS).gt(ETHER)))
    .groupBy(pair => pair.tokens[0] === WETH_ADDRESS ? pair.tokens[1] : pair.tokens[0])
    .value()
  
  console.log("allMarketPairs: %d", allMarketPairs.length);
  console.log(JSON.stringify(allMarketPairs, null, 2));

  console.log("marketsByToken: %d", Object.keys(marketsByToken).length);
  console.log(JSON.stringify(marketsByToken,null, 2));
}

async function t2_reserves() {
  // const uniswap_contracts = new Array<Contract>();

  const factory_addr = UNISWAP_FACTORY_ADDRESS;
  const uni_factory_contract = new Contract(factory_addr, UNISWAP_FACTORY_ABI, provider);
  const contract_addrs = new Array<string>();
  for(let i =0; i<5; i++){
    // console.log(i);
    const contract_addr = await uni_factory_contract.functions.allPairs(i);
    contract_addrs.push(contract_addr[0]);
  }
  // console.log(contract_addrs);

  // const contract_addrs = [
  //   '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc',
  //   '0x3139Ffc91B99aa94DA8A2dc13f1fC36F9BDc98eE',
  //   '0x12EDE161c702D1494612d19f05992f43aa6A26FB',
  //   '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11',
  //   '0x07F068ca326a469Fc1d87d85d448990C8cBa7dF9'
  // ];
  
  // const contract_addrs = [
  //   new Contract(addr, )
  // ];

  const uniswap_contracts = contract_addrs.map(addr => new Contract(addr, UNISWAP_PAIR_ABI, provider));
  for(let i=0; i< uniswap_contracts.length; i++){
    const reserve_result = await uniswap_contracts[i].getReserves();
    console.log(JSON.stringify(reserve_result, null, 2));
  }
}

// provider_test();
// contract_test();
// getpair_t3();
// t1_test_reserves();
t2_reserves();