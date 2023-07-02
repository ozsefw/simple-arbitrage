import fs from "fs";

import * as _ from "lodash";
import { Contract, providers, } from "ethers";
import { UniswappyV2EthPair } from "./UniswappyV2EthPair";
import { UNISWAP_QUERY_ABI } from "./abi";
import {
  UNISWAP_LOOKUP_CONTRACT_ADDRESS,
  WETH_ADDRESS,

  SUSHISWAP_FACTORY_ADDRESS,
  UNISWAP_FACTORY_ADDRESS,
  CRO_FACTORY_ADDRESS,
  ZEUS_FACTORY_ADDRESS,
  LUA_FACTORY_ADDRESS,
} from "./addresses";

// import unipairs from "../sample/uniswap-v2-pair.json";
// import "./addresses";
// import { SSL_OP_EPHEMERAL_RSA } from "constants";


// const ETHEREUM_RPC_URL = "https://eth-mainnet.public.blastapi.io"
const ETHEREUM_RPC_URL = "https://virginia.rpc.blxrbdn.com"
// const SUSHISWAP_FACTORY_ADDRESS = '0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac';
// const UNISWAP_FACTORY_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f';
const provider = new providers.StaticJsonRpcProvider(ETHEREUM_RPC_URL);

const BATCH_COUNT_LIMIT = 1000;
const UNISWAP_BATCH_SIZE = 1000;

t3();

async function t3() {
  // let uni_pair;
  // fs.readFile(file_path, "utf-8", function (err, data) {
  //   if (err){
  //     return err;
  //   }
  //   else{
  //     console.log("read success");
  //     uni_pair = JSON.parse(data);
  //     console.log(uni_pair);
  //     // return JSON.parse(data);
  //   }
  // });

  // const = fs.readFileSync(file_path, "utf-8");
  const uni_path = "sample/uniswap-v2-pair.json";
  const uni_pairs = JSON.parse(fs.readFileSync(uni_path, "utf-8"));
  console.log("uni pairs: ", _.chain(uni_pairs).value().length);

  const sushi_path = "sample/sushiswap-pair.json";
  const sushi_pairs = JSON.parse(fs.readFileSync(sushi_path, "utf-8"));
  console.log("sushi pairs: ", _.chain(sushi_pairs).value().length);

  // const all_pairs = _.chain(uni_pairs).concat(sushi_pairs).value();
  // console.log(all_pairs.length);

  // const marketsyByToken = _.chain(uni_pairs)
  //   .flatten()
  //   .groupBy(pair => pair.tokens[0] === WETH_ADDRESS ? pair.tokens[1] : pair.tokens[0])
  //   .value();
  const marketsByToken = _.chain(uni_pairs).concat(sushi_pairs)
    .flatten()
    .groupBy(pair => pair.tokens[0] === WETH_ADDRESS ? pair.tokens[1] : pair.tokens[0])
    .value();
  
  const result_pairs = _.chain(
      _.pickBy(marketsByToken, a=>a.length >1)
    )
    .values()
    .flatten()
    .value();

  console.log("common pairs: ", result_pairs.length)
  // console.log(JSON.stringify(result, null, 2));

  // fs.writeFileSync( result_path, JSON.stringify(result, null, 2))
  // const result_path = "sample/common_"
  // fs.writeFileSync(result_path, JSON.stringify(result, null, 2));

  // console.log(uni_pair);

  // const uni_pairs = require("../sample/uniswap-v2-pair.json");
  // fs.readFile(path)
}

async function t2() {
  const file_path = "sample/sushiswap-pair.json";
  // const f = fs.mkdir("sample/sushiswap-pair.json");
  // const fd = await fs.open("sample/sushi-pair.json", "w+", function (err, fd) {
  //   if (err){
  //     return console.error(err);
  //   }
  //   else{
  //     console.log("open success");
  //     fd
  //   }
  // });
  const pairs = [
    {
      market: '0x73d5285f1221564bCE82521F901cbF23FBCB876b',
      tokens: [
        '0x92B914f1DDcBb1D117a718E83C9ED7eB32fc44d1',
        '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
      ],
    },
    {
      market: '0xe26433358fDB9aDdcc59ba3F2Df0e8490B015FF4',
      tokens: [
        '0x7756Edf05Ef3c2b321A85D77B5cbF7c8A9a7C247',
        '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
      ],
    }
  ];

  await fs.writeFile(file_path, JSON.stringify(pairs, null, 2), function (err) {
    if (err){
      console.log("error: ", err);
    }
    else{
      console.log("write success");
    }
  });
}

async function t1() {
  // const markets = await UniswappyV2EthPair.getUniswapMarketsByToken(provider, SUSHISWAP_FACTORY_ADDRESS);
  // const file_path = "sample/sushiswap-pair.json";
  // const FACTORY_ADDRESS = SUSHISWAP_FACTORY_ADDRESS;
  // const file_path = "sample/uniswap-v2-pair.json";
  // const FACTORY_ADDRESS = UNISWAP_FACTORY_ADDRESS;
  // const file_path = "sample/cro-pair.json";
  // const FACTORY_ADDRESS = CRO_FACTORY_ADDRESS;
  const file_path = "sample/lua-pair.json";
  const FACTORY_ADDRESS = LUA_FACTORY_ADDRESS;

  const foramt_pairs = await getUniswappyMarkets(provider, FACTORY_ADDRESS)
  // const pair = new Array[];
  const pairs = [];
  for(const p of foramt_pairs){
    const pair_item = {
      address: p.marketAddress,
      tokens: p.tokens,
    };

    pairs.push(pair_item);
  }


  await fs.writeFile(file_path, JSON.stringify(pairs, null, 2), function (err) {
    if (err){
      console.log("error: ", err);
    }
    else{
      console.log("write success");
    }
  });
}

async function getUniswappyMarkets(provider: providers.JsonRpcProvider, factoryAddress: string)
  :Promise<Array<UniswappyV2EthPair>>
{
  const uniswapQuery = new Contract(UNISWAP_LOOKUP_CONTRACT_ADDRESS, UNISWAP_QUERY_ABI, provider);

  const marketPairs = new Array<UniswappyV2EthPair>()
  for (let i = 0; i < BATCH_COUNT_LIMIT * UNISWAP_BATCH_SIZE; i += UNISWAP_BATCH_SIZE) {
    const pairs: Array<Array<string>> = (
      await uniswapQuery.functions.getPairsByIndexRange(factoryAddress, i, i + UNISWAP_BATCH_SIZE)
    )[0];

    console.log(i);

    for (let i = 0; i < pairs.length; i++) {
      const pair = pairs[i];
      const marketAddress = pair[2];
      // let tokenAddress: string;

      if (pair[0]!=WETH_ADDRESS && pair[1] != WETH_ADDRESS){
        continue;
      }
      
      const uniswappyV2EthPair = new UniswappyV2EthPair(marketAddress, [pair[0], pair[1]], "");
      marketPairs.push(uniswappyV2EthPair);
    }

    // await new Promise((r)=>setTimeout(r, 1000));

    if (pairs.length < UNISWAP_BATCH_SIZE) {
      break
    }
  }

  console.log("pairs in one market: %s, %d", factoryAddress, marketPairs.length);

  return marketPairs
}