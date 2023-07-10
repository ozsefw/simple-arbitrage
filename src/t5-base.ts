import { Contract, providers, BigNumber, utils} from "ethers";
import { last, toString } from "lodash";
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

const UNI_V3_FACTORY_ADDRESS = "0x1F98431c8aD98523631AE4a59f267346ea31F984"
const UNI_V3_QUOTER_ADDRESS = "0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6"
const UNI_V2_ROUTER_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
const WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
const PEPE_ERC20 = '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD'
const PEPE_UNI_V3_POOL = '0xd738e6a2ef2846a643dc68092ad0fd7f5a8eb6f8'
const PEPE_UNI_V2_POOL = '0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269'

export async function uni_v3_factory_test() {
  const ABI = [
    "function getPool(address,address,uint24)public view returns (address)",
  ];

  const uni_v3_factory = new Contract(UNI_V3_FACTORY_ADDRESS, ABI, provider);
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
  // console.log("quoter test");
  const ABI = [
    "function quoteExactInputSingle(address,address,uint24,uint256,uint160) view returns (uint256)"
  ];
  const signer = provider.getSigner("0x70997970C51812dc3A010C7d01b50e0d17dc79C8");
  const contract = new Contract(UNI_V3_QUOTER_ADDRESS, ABI, signer);

  try{
    const amount = await contract.quoteExactInputSingle(
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
      '0x4e3FBD56CD56c3e72c1403e103b45Db9da5B9D2B',
      10000,
      1_000_000,
      0
    );

    console.log(amount.toString());
  }
  catch(err){
    console.log(err);
  }
}

export async function deposit_test() {
  const from = '0x70997970C51812dc3A010C7d01b50e0d17dc79C8';
  const to = '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266';
  // const WETH_ERC20 = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2';
  const ABI = [
    "function deposit() payable",
    "function balanceOf(address) view returns (uint256)",
    "function transfer(address, uint256) returns (bool)",
  ];

  const signer = provider.getSigner(from);
  // const contract = new Contract(WETH_ERC20, ABI, provider);
  const contract = new Contract(WETH_ERC20, ABI, signer);

  // const result = await contract.deposit({value: (10**18).toString()});
  // console.log(result);

  // const balance = await contract.balanceOf(from);
  // console.log(balance.toString());

  const balance_before = await contract.balanceOf(to);
  console.log("balance before: ", balance_before.toString());

  const result = await contract.transfer(to, 1000_000);
  console.log(result);

  const balance_after = await contract.balanceOf(to);
  console.log("balance after: ", balance_after.toString());
}

export async function simulate_tx() {
  const UNI_V3_QUOTE_ABI= [
    "function quoteExactInputSingle(address,address,uint24,uint256,uint160) view returns (uint256)"
  ];
  const UNI_V2_ROUTER_ABI = [
    "function getAmountsOut(uint256, address[]) view returns (uint256[])",
    "function getAmountOut(uint256, uint256, uint256) view returns (uint256)"
  ];
  const UNI_V2_ABI = [
    "function getReserves() view returns (uint112, uint112, uint32)"
  ];

  // const signer = provider.getSigner("0x70997970C51812dc3A010C7d01b50e0d17dc79C8");
  const uni_v3_quoter = new Contract(UNI_V3_QUOTER_ADDRESS, UNI_V3_QUOTE_ABI, provider);
  const uni_v2_router = new Contract(UNI_V2_ROUTER_ADDRESS, UNI_V2_ROUTER_ABI, provider);
  const pepe_uni_v2 = new Contract(PEPE_UNI_V2_POOL, UNI_V2_ABI, provider);

  try{
    // const amount_in = "1057147387365399552"

    // const amount_out = await uni_v3_quoter.quoteExactInputSingle(
    //   '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
    //   '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD',
    //   10000,
    //   amount_in,
    //   "13443882501629929000910181338733598",
    // );
    // console.log(amount_out.toString());

    const pepe_amount_in = "29998097910326302650298426983"

    // const [reserve0, reserve1, _] = await pepe_uni_v2.getReserves();
    // console.log(reserve0.toString());
    // console.log(reserve1.toString());

    // const reserve0="245632676838043522785"
    // const reserve1="6906670324365987789237864436773"
    // const result = await uni_v2_router.getAmountOut(
    //   pepe_amount_in,
    //   reserve1,
    //   reserve0
    // );
    // console.log(result.toString());

    const result = await uni_v2_router.getAmountsOut(
      pepe_amount_in,
      [PEPE_ERC20, WETH_ERC20],
    )

    console.log(result[1].toString())
    console.log("on-chain: ", "1068308415863593344")

    // 1068308415863593344
    // 1068308522694445586
    // 106830852242

    // const result = await uni_v2_router.getAmountOut(100, 10000, 10000)
    // console.log(result.toString())

  }
  catch(err){
    console.log(err);
  }
}

export async function simulate_tx2(){

  const UNI_V3_QUOTE_ABI= [
    "function quoteExactInputSingle(address,address,uint24,uint256,uint160) view returns (uint256)"
  ]

  const UNI_V2_ROUTER_ABI = [
    "function getAmountsOut(uint256, address[]) view returns (uint256[])",
    "function getAmountOut(uint256, uint256, uint256) view returns (uint256)"
  ];

  const uni_v3_quoter = new Contract(UNI_V3_QUOTER_ADDRESS, UNI_V3_QUOTE_ABI, provider)
  const uni_v2_router = new Contract(UNI_V2_ROUTER_ADDRESS, UNI_V2_ROUTER_ABI, provider);

  const base_eth_amount_in = BigNumber.from("1057147387365399552");
  // let last_max_result = {
  //   index: Number,
  // };
  let last_max_result;

  for(let i=0; i<100; i++){
    const eth_amount_in = base_eth_amount_in.add(i*10000000000000);
    const pepe_amount_out = await uni_v3_quoter.quoteExactInputSingle(
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xfb66321D7C674995dFcC2cb67A30bC978dc862AD',
      10000,
      eth_amount_in,
      0
      // "13443882501629929000910181338733598",
    )

    // console.log("pepe out from uni-v3: ", pepe_amount_out.toString())

    const pepe_amount_in = pepe_amount_out.sub(pepe_amount_out.div(100))

    // console.log("pepe in to uni-v2: ", pepe_amount_in.toString())

    const result = await uni_v2_router.getAmountsOut(
      pepe_amount_in,
      [PEPE_ERC20, WETH_ERC20],
    );

    const eth_amount_out = BigNumber.from(result[1]);
    // console.log("eth out from uni-v3: ", eth_amount_out.toString());

    const profit = eth_amount_out.sub(eth_amount_in);

    if(i==0){
      // last_max_result = new Map([i, profit, eth_amount_in, eth_amount_out]);
      // last_max_result = new Set([i, profit, eth_amount_in, eth_amount_out]);
      last_max_result = {id: i, profit: profit, in: eth_amount_in, out: eth_amount_out};
    }
    else{
        const last_profit = last_max_result?.profit!;
        if (last_profit < profit){
          last_max_result = {id: i, profit: profit, in: eth_amount_in, out: eth_amount_out};
        }
    }

    // console.log(
    //   "result: amount_in: %s, amount_out: %s, profit: \n%s",
    //   eth_amount_in,
    //   eth_amount_out,
    //   utils.formatEther(profit),
    //   // profit
    // );
  }

  console.log(
    "result: index: %s,  profit: %s, amount_in: %s, amount_out: %s",
    last_max_result?.id,
    last_max_result?.profit,
    last_max_result?.in,
    last_max_result?.out,
    // profit
  );
}

export async function inspect_t01(){
  const UNI_V2_ABI = [
    "function getReserves() view returns (uint112, uint112, uint32)"
  ];
  // struct Slot0 {
  //   // the current price
  //   uint160 sqrtPriceX96;
  //   // the current tick
  //   int24 tick;
  //   // the most-recently updated index of the observations array
  //   uint16 observationIndex;
  //   // the current maximum number of observations that are being stored
  //   uint16 observationCardinality;
  //   // the next maximum number of observations to store, triggered in observations.write
  //   uint16 observationCardinalityNext;
  //   // the current protocol fee as a percentage of the swap fee taken on withdrawal
  //   // represented as an integer denominator (1/x)%
  //   uint8 feeProtocol;
  //   // whether the pool is locked
  //   bool unlocked;
  // }
  const UNI_V3_ABI = [
    "function slot0() view returns (uint160, int24, uint16, uint16, uint16, uint8, bool)"
  ];

  const pepe_uni_v2 = new Contract(PEPE_UNI_V2_POOL, UNI_V2_ABI, provider)
  const pepe_uni_v3 = new Contract(PEPE_UNI_V3_POOL, UNI_V3_ABI, provider)

  const slot0 = await pepe_uni_v3.slot0()
  console.log(slot0)

  const reserves = await pepe_uni_v2.getReserves();
  const token0 = reserves[0].toString();
  const token1 = reserves[1].toString();
  console.log(token0)
  console.log(token1)
}