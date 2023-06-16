import { UNISWAP_FACTORY_ABI, UNISWAP_PAIR_ABI, UNISWAP_QUERY_ABI } from "./abi";
import { Contract, providers, Wallet } from "ethers";
import { UniswappyV2EthPair } from "./UniswappyV2EthPair";
// import { UNISWAP_LOOKUP_CONTRACT_ADDRESS, WETH_ADDRESS } from "./addresses";
// import { FACTORY_ADDRESSES } from "./addresses";

const UNISWAP_LOOKUP_CONTRACT_ADDRESS = '0x5EF1009b9FCD4fec3094a5564047e190D72Bd511'
// const WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2';
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

async function main() {
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
}

contract_test();

// main();