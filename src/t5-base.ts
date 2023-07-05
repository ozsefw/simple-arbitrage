import { Contract, providers, } from "ethers";
// import { UNISWAP_FACTORY_ADDRESS } from "./addresses";

const ETHEREUM_RPC_URL="http://127.0.0.1:8545"
const provider = new providers.StaticJsonRpcProvider(ETHEREUM_RPC_URL)

// const UNISWAP_V3_FACTORY_ABI = [
//     { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" },
//     { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "uint24", "name": "fee", "type": "uint24" }, { "indexed": true, "internalType": "int24", "name": "tickSpacing", "type": "int24" }], "name": "FeeAmountEnabled", "type": "event" },
//     { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "address", "name": "oldOwner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "newOwner", "type": "address" }], "name": "OwnerChanged", "type": "event" },
//     { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "address", "name": "token0", "type": "address" }, { "indexed": true, "internalType": "address", "name": "token1", "type": "address" }, { "indexed": true, "internalType": "uint24", "name": "fee", "type": "uint24" }, { "indexed": false, "internalType": "int24", "name": "tickSpacing", "type": "int24" }, { "indexed": false, "internalType": "address", "name": "pool", "type": "address" }], "name": "PoolCreated", "type": "event" },
//     { "inputs": [{ "internalType": "address", "name": "tokenA", "type": "address" }, { "internalType": "address", "name": "tokenB", "type": "address" }, { "internalType": "uint24", "name": "fee", "type": "uint24" }], "name": "createPool", "outputs": [{ "internalType": "address", "name": "pool", "type": "address" }], "stateMutability": "nonpayable", "type": "function" },
//     { "inputs": [{ "internalType": "uint24", "name": "fee", "type": "uint24" }, { "internalType": "int24", "name": "tickSpacing", "type": "int24" }], "name": "enableFeeAmount", "outputs": [], "stateMutability": "nonpayable", "type": "function" },
//     { "inputs": [{ "internalType": "uint24", "name": "", "type": "uint24" }], "name": "feeAmountTickSpacing", "outputs": [{ "internalType": "int24", "name": "", "type": "int24" }], "stateMutability": "view", "type": "function" },
//     { "inputs": [{ "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint24", "name": "", "type": "uint24" }], "name": "getPool", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" },
//     { "inputs": [], "name": "owner", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" },
//     { "inputs": [], "name": "parameters", "outputs": [{ "internalType": "address", "name": "factory", "type": "address" }, { "internalType": "address", "name": "token0", "type": "address" }, { "internalType": "address", "name": "token1", "type": "address" }, { "internalType": "uint24", "name": "fee", "type": "uint24" }, { "internalType": "int24", "name": "tickSpacing", "type": "int24" }], "stateMutability": "view", "type": "function" },
//     { "inputs": [{ "internalType": "address", "name": "_owner", "type": "address" }], "name": "setOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function" }
// ];

const UNISWAP_V3_FACTORY_ADDRESS = "0x1F98431c8aD98523631AE4a59f267346ea31F984"
const UNISWAP_V3_QUOTER_ADDRESS = "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6"
const WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2';
const PEPE_ERC20 = '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD';
const PEPE_UNI_V3_POOL = '0xd738e6a2ef2846a643dc68092ad0fd7f5a8eb6f8';

export async function uni_v3_factory_test() {
  const ABI = [
    "function getPool(address,address,uint24)public view returns (address)",
  ];

  const uni_v3_factory = new Contract(UNISWAP_V3_FACTORY_ADDRESS, ABI, provider);
  const pool_address = await uni_v3_factory.getPool(WETH_ERC20, PEPE_ERC20, 10000);
  console.log(pool_address);
}

export async function uni_v2_test_2() {
  const ABI = [
    "function fee() view returns (uint24)"
  ];

  const contract = new Contract(PEPE_UNI_V3_POOL, ABI, provider);
  const fee = await contract.fee();
  console.log(fee);
}

export async function quoter_test() {
  console.log("quoter test");
  const ABI = [
    "function quoteExactInputSingle(address,address,uint24,uint256,uint160) view returns (uint256)"
  ];

  const contract = new Contract(UNISWAP_V3_QUOTER_ADDRESS, ABI, provider);
  // const amount = await contract.quoteExactInputSingle(PEPE_ERC20, WETH_ERC20, 10000, 10000, );

  try{
    const amount = await contract.quoteExactInputSingle(
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
      '0x4e3FBD56CD56c3e72c1403e103b45Db9da5B9D2B',
      10000,
      1_000_000,
      0
    );

    console.log(amount);
  }
  catch(err){
    console.log(err);
  }
}