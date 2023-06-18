import * as _ from "lodash";
import { chain } from "lodash";
// class EthMarket{
//     tokens: Array<string>;

//     constructor(tokens: Array<string>){
//         this.tokens = tokens;
//     }
// }

function t1() {
  const allPairs = [
    [1,2,3,4,5],
    [10, 20, 30, 40, 50,],
    [1,2,3,4,5],
  ];
  console.log(allPairs);

//   console.log(_.chain(allPairs).flatten().value())

  const marketsByTokenAll = _.chain(allPairs).flatten().groupBy(n=>n).value();
  console.log(marketsByTokenAll);

  chain(marketsByTokenAll).pickBy

  const result = _.pickBy(marketsByTokenAll, a=>a.length>1)
  console.log(result);

//   const result_2 = _.chain(_.pickBy(marketsByTokenAll, a=>a.length>1)).values().flatten().value();
//   console.log(result_2);
}

t1();
    