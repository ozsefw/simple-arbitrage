import { Contract, providers, Wallet } from "ethers";
import { UniswappyV2EthPair } from "./UniswappyV2EthPair";
// import { FACTORY_ADDRESSES } from "./addresses";

// const UNISWAP_LOOKUP_CONTRACT_ADDRESS = '0x5EF1009b9FCD4fec3094a5564047e190D72Bd511'
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
    const markets = await UniswappyV2EthPair.getUniswapMarketsByToken(provider, FACTORY_ADDRESSES);
    console.log(markets);
}

main();