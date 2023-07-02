import { Contract, providers, } from "ethers";
import { UNISWAP_PAIR_ABI, UNISWAP_QUERY_ABI } from "./abi";

const ETHEREUM_RPC_URL = "http://localhost:8545"
const provider = new providers.StaticJsonRpcProvider(ETHEREUM_RPC_URL);
const PEPE_UNI_ADDR = "0x076a3e1500f3110D8F4445D396A3d7cA6D0Ca269"

t1();

async function t1() {
    // const pepe_swap = new Contract(PEPE_UNI_ADDR, UNISWAP_PAIR_ABI, provider);
    // const to ="0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
    // await pepe_swap.functions.swap(0, 10000000, to, []);
    // provider.call("0x70a082310000000000000000000000002d2a7d56773ae7d5c7b9f1b57f7be05039447b4d");

    // const block_number = await provider.getBlockNumber();
    // console.log(block_number);
    // uint amount0In = balance0 > _reserve0 - amount0Out ? balance0 - (_reserve0 - amount0Out) : 0;
    // uint amount1In = balance1 > _reserve1 - amount1Out ? balance1 - (_reserve1 - amount1Out) : 0;

    const balance0 = 7632789410651257211;
    const balance1 = 435584822833934301750739653;
    const reserve0 = 192309366971097876968;
    const reserve1 = 10972953907841638321603915235789;
    const amout0Out = 0;
    const amout1Out = 0x100;

    if (balance0 > (reserve0 - amout0Out)){
        console.log("0: >");
    }
    else{
        console.log("0: <");
    }

    if (balance1 > (reserve1 - amout1Out)){
        console.log("1: >")
    }
    else{
        console.log("1: <");
    }
}
