## getUniswapMarketByToken()
### marketsByTokenAll
```log
{
  '0xdAC17F958D2ee523a2206206994597C13D831ec7': [
    UniswappyV2EthPair {
      _marketAddress: '0x06da0fd433C1A5d7a4faa01111c044910A184553',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  '0xD533a949740bb3306d119CC777fa900bA034cd52': [
    UniswappyV2EthPair {
      _marketAddress: '0x58Dc5a51fE44589BEb22E8CE67720B5BC5378009',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  '0xAba8cAc6866B83Ae4eec97DD07ED254282f6aD8A': [
    UniswappyV2EthPair {
      _marketAddress: '0x95b54C8Da12BB23F7A5F6E26C38D04aCC6F81820',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  '0x408e41876cCCDC0F92210600ef50372656052a38': [
    UniswappyV2EthPair {
      _marketAddress: '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48': [
    UniswappyV2EthPair {
      _marketAddress: '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  '0x06AF07097C9Eeb7fD685c692751D5C66dB49c215': [
    UniswappyV2EthPair {
      _marketAddress: '0x12EDE161c702D1494612d19f05992f43aa6A26FB',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  '0x6B175474E89094C44Da98b954EedeAC495271d0F': [
    UniswappyV2EthPair {
      _marketAddress: '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ]
}
```
### allPairs
### marketsByTokenAll

### allMarketPairs
### allMarketPairs (after updateReserves())
### marketsByToken

## getUniswappyMarkets()
### marketPairs
```log
0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f
[
  UniswappyV2EthPair {
    _marketAddress: '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc',
    _tokens: [
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x12EDE161c702D1494612d19f05992f43aa6A26FB',
    _tokens: [
      '0x06AF07097C9Eeb7fD685c692751D5C66dB49c215',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x06AF07097C9Eeb7fD685c692751D5C66dB49c215': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11',
    _tokens: [
      '0x6B175474E89094C44Da98b954EedeAC495271d0F',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x6B175474E89094C44Da98b954EedeAC495271d0F': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  }
]
0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac
[
  UniswappyV2EthPair {
    _marketAddress: '0x06da0fd433C1A5d7a4faa01111c044910A184553',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xdAC17F958D2ee523a2206206994597C13D831ec7'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xdAC17F958D2ee523a2206206994597C13D831ec7': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x58Dc5a51fE44589BEb22E8CE67720B5BC5378009',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xD533a949740bb3306d119CC777fa900bA034cd52'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xD533a949740bb3306d119CC777fa900bA034cd52': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x95b54C8Da12BB23F7A5F6E26C38D04aCC6F81820',
    _tokens: [
      '0xAba8cAc6866B83Ae4eec97DD07ED254282f6aD8A',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xAba8cAc6866B83Ae4eec97DD07ED254282f6aD8A': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1',
    _tokens: [
      '0x408e41876cCCDC0F92210600ef50372656052a38',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x408e41876cCCDC0F92210600ef50372656052a38': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  }
]
```


0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac
[
  UniswappyV2EthPair {
    _marketAddress: '0x06da0fd433C1A5d7a4faa01111c044910A184553',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xdAC17F958D2ee523a2206206994597C13D831ec7'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xdAC17F958D2ee523a2206206994597C13D831ec7': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x58Dc5a51fE44589BEb22E8CE67720B5BC5378009',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xD533a949740bb3306d119CC777fa900bA034cd52'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xD533a949740bb3306d119CC777fa900bA034cd52': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x95b54C8Da12BB23F7A5F6E26C38D04aCC6F81820',
    _tokens: [
      '0xAba8cAc6866B83Ae4eec97DD07ED254282f6aD8A',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xAba8cAc6866B83Ae4eec97DD07ED254282f6aD8A': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1',
    _tokens: [
      '0x408e41876cCCDC0F92210600ef50372656052a38',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x408e41876cCCDC0F92210600ef50372656052a38': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x117d4288B3635021a3D612FE05a3Cbf5C717fEf2',
    _tokens: [
      '0x476c5E26a75bd202a9683ffD34359C0CC15be0fF',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x476c5E26a75bd202a9683ffD34359C0CC15be0fF': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xC352e63B7297FCaAe115E0758A6e84355181Cdaf',
    _tokens: [
      '0x566113069683Ce664958A784f18336B4020a1350',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x566113069683Ce664958A784f18336B4020a1350': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x001b6450083E531A5a7Bf310BD2c1Af4247E23D4',
    _tokens: [
      '0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x31503dcb60119A812feE820bb7042752019F2355',
    _tokens: [
      '0xc00e94Cb662C3520282E6f5717214004A7f26888',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xc00e94Cb662C3520282E6f5717214004A7f26888': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xA75F7c2F025f470355515482BdE9EFA8153536A8',
    _tokens: [
      '0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xBA11D00c5f74255f56a5E366F4F77f5A186d7f55': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xA1d7b2d891e3A1f9ef4bBC5be20630C2FEB1c470',
    _tokens: [
      '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x5E63360E891BD60C69445970256C260b0A6A54c6',
    _tokens: [
      '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xF1F85b2C54a2bD284B1cf4141D64fD171Bd85539',
    _tokens: [
      '0x57Ab1ec28D129707052df4dF418D58a2D46d5f51',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x57Ab1ec28D129707052df4dF418D58a2D46d5f51': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xCb2286d9471cc185281c4f763d34A962ED212962',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xD46bA6D942050d489DBd938a2C909A5d5039A161'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xD46bA6D942050d489DBd938a2C909A5d5039A161': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xC40D16476380e4037e6b1A2594cAF6a6cc8Da967',
    _tokens: [
      '0x514910771AF9Ca656af840dff83E8264EcF986CA',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x514910771AF9Ca656af840dff83E8264EcF986CA': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x088ee5007C98a9677165D78dD2109AE4a3D04d0C',
    _tokens: [
      '0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xC3D03e4F041Fd4cD388c549Ee2A29a9E5075882f',
    _tokens: [
      '0x6B175474E89094C44Da98b954EedeAC495271d0F',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x6B175474E89094C44Da98b954EedeAC495271d0F': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x397FF1542f962076d0BFE58eA045FfA2d347ACa0',
    _tokens: [
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x795065dCc9f64b5614C407a6EFDC400DA6221FB0',
    _tokens: [
      '0x6B3595068778DD592e39A122f4f5a5cF09C90fE2',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x6B3595068778DD592e39A122f4f5a5cF09C90fE2': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xbf8722F17E8017c96389C20b41eCB62e1f34e4Bd',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xdeFCb64c13442D40db6e45CF7fE1E064e5E360C9'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xdeFCb64c13442D40db6e45CF7fE1E064e5E360C9': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x28B5E0090Ff9C1192e1134135deb17e0b1C1cdBF',
    _tokens: [
      '0xBB14B9B385ca3bd3668BbA114b555B3a3e1fA705',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xBB14B9B385ca3bd3668BbA114b555B3a3e1fA705': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xc66eD7c8034E11EBd32499389C35b3E6E9eE3e78',
    _tokens: [
      '0x5c4ac68aAc56eBe098D621Cd8CE9F43270Aaa355',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x5c4ac68aAc56eBe098D621Cd8CE9F43270Aaa355': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x75e66d062a2a8BE5c99d71db11d72aB3B82bA8b3',
    _tokens: [
      '0x4CC19356f2D37338b9802aa8E8fc58B0373296E7',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x4CC19356f2D37338b9802aa8E8fc58B0373296E7': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xBb7aB09971E56Aaf248dCc6C3DF865aF69D97372',
    _tokens: [
      '0x84cA8bc7997272c7CfB4D0Cd3D55cd942B3c9419',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x84cA8bc7997272c7CfB4D0Cd3D55cd942B3c9419': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x8283DD24f8D8E7b083e2855a4c3EA1A7Feba08C2',
    _tokens: [
      '0x31024A4C3e9aEeb256B825790F5cb7ac645e7cD5',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x31024A4C3e9aEeb256B825790F5cb7ac645e7cD5': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  }
]
0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f
[
  UniswappyV2EthPair {
    _marketAddress: '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc',
    _tokens: [
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x12EDE161c702D1494612d19f05992f43aa6A26FB',
    _tokens: [
      '0x06AF07097C9Eeb7fD685c692751D5C66dB49c215',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x06AF07097C9Eeb7fD685c692751D5C66dB49c215': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11',
    _tokens: [
      '0x6B175474E89094C44Da98b954EedeAC495271d0F',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x6B175474E89094C44Da98b954EedeAC495271d0F': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xCe407CD7b95B39d3B4d53065E711e713dd5C5999',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xfA3E941D1F6B7b10eD84A0C211bfA8aeE907965e'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xfA3E941D1F6B7b10eD84A0C211bfA8aeE907965e': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xB6909B960DbbE7392D405429eB2b3649752b4838',
    _tokens: [
      '0x0D8775F648430679A709E98d2b0Cb6250d2887EF',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x0D8775F648430679A709E98d2b0Cb6250d2887EF': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xBb2b8038a1640196FbE3e38816F3e67Cba72D940',
    _tokens: [
      '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x9896BD979f9DA57857322Cc15e154222C4658a5a',
    _tokens: [
      '0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x598E740cda7C525080d3FCb9Fa7C4E1bd0044B34',
    _tokens: [
      '0x5e74C9036fb86BD7eCdcb084a0673EFc32eA31cb',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x5e74C9036fb86BD7eCdcb084a0673EFc32eA31cb': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x43AE24960e5534731Fc831386c07755A2dc33D47',
    _tokens: [
      '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x231F3381D10478BfC2cA552195b9d8B15968B60c',
    _tokens: [
      '0x4D13d624a87baa278733c068A174412AfA9ca6C8',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x4D13d624a87baa278733c068A174412AfA9ca6C8': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x3b0F0fe3Be830826D833a67cD1d7C80edF3Fb49b',
    _tokens: [
      '0x86FADb80d8D2cff3C3680819E4da99C10232Ba0F',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x86FADb80d8D2cff3C3680819E4da99C10232Ba0F': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x67660E35fee501d0876B9493bb5eC90E10675957',
    _tokens: [
      '0x4470BB87d77b963A013DB939BE332f927f2b992e',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x4470BB87d77b963A013DB939BE332f927f2b992e': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x260E069deAd76baAC587B5141bB606Ef8b9Bab6c',
    _tokens: [
      '0x3A9FfF453d50D4Ac52A6890647b823379ba36B9E',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x3A9FfF453d50D4Ac52A6890647b823379ba36B9E': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x5D27dF1a6E03254E4f1218607D8E073667ffae2F',
    _tokens: [
      '0xaeC2E87E0A235266D9C5ADc9DEb4b2E29b54D009',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xaeC2E87E0A235266D9C5ADc9DEb4b2E29b54D009': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xB784CED6994c928170B417BBd052A096c6fB17E2',
    _tokens: [
      '0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x1776e1F26f98b1A5dF9cD347953a26dd3Cb46671': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xa2107FA5B38d9bbd2C461D6EDf11B11A50F6b974',
    _tokens: [
      '0x514910771AF9Ca656af840dff83E8264EcF986CA',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x514910771AF9Ca656af840dff83E8264EcF986CA': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x718Dd8B743ea19d71BDb4Cb48BB984b73a65cE06',
    _tokens: [
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2',
      '0xC0F9bD5Fa5698B6505F643900FFA515Ea5dF54A9'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber],
      '0xC0F9bD5Fa5698B6505F643900FFA515Ea5dF54A9': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x55D5c232D921B9eAA6b37b5845E439aCD04b4DBa',
    _tokens: [
      '0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x2b591e99afE9f32eAA6214f7B7629768c40Eeb39': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xa5E79baEe540f000ef6F23D067cd3AC22c7d9Fe6',
    _tokens: [
      '0xaaAEBE6Fe48E54f431b0C390CfaF0b017d09D42d',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0xaaAEBE6Fe48E54f431b0C390CfaF0b017d09D42d': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xC2aDdA861F89bBB333c90c492cB837741916A225',
    _tokens: [
      '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0x99731C13ef1aaB58e48FA9a96deFEFdf1b8DE164',
    _tokens: [
      '0x054B642117892205A6F5a0b8c29Ffd10a6369d19',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x054B642117892205A6F5a0b8c29Ffd10a6369d19': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xad3B5027d090b7bc120Dc264906ca4642b0fb9F3',
    _tokens: [
      '0x78a685E0762096ed0F98107212e98F8C35A9D1D8',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x78a685E0762096ed0F98107212e98F8C35A9D1D8': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  },
  UniswappyV2EthPair {
    _marketAddress: '0xF49144E61C05120f1b167E4B4F59cf0a5d77903F',
    _tokens: [
      '0x07597255910a51509CA469568B048F2597E72504',
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    ],
    _protocol: '',
    _tokenBalances: {
      '0x07597255910a51509CA469568B048F2597E72504': [BigNumber],
      '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2': [BigNumber]
    }
  }
]
[
  [
    UniswappyV2EthPair {
      _marketAddress: '0x06da0fd433C1A5d7a4faa01111c044910A184553',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x58Dc5a51fE44589BEb22E8CE67720B5BC5378009',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x95b54C8Da12BB23F7A5F6E26C38D04aCC6F81820',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x611CDe65deA90918c0078ac0400A72B0D25B9bb1',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x117d4288B3635021a3D612FE05a3Cbf5C717fEf2',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xC352e63B7297FCaAe115E0758A6e84355181Cdaf',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x001b6450083E531A5a7Bf310BD2c1Af4247E23D4',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x31503dcb60119A812feE820bb7042752019F2355',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xA75F7c2F025f470355515482BdE9EFA8153536A8',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xA1d7b2d891e3A1f9ef4bBC5be20630C2FEB1c470',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x5E63360E891BD60C69445970256C260b0A6A54c6',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xF1F85b2C54a2bD284B1cf4141D64fD171Bd85539',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xCb2286d9471cc185281c4f763d34A962ED212962',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xC40D16476380e4037e6b1A2594cAF6a6cc8Da967',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x088ee5007C98a9677165D78dD2109AE4a3D04d0C',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xC3D03e4F041Fd4cD388c549Ee2A29a9E5075882f',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x397FF1542f962076d0BFE58eA045FfA2d347ACa0',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x795065dCc9f64b5614C407a6EFDC400DA6221FB0',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xbf8722F17E8017c96389C20b41eCB62e1f34e4Bd',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x28B5E0090Ff9C1192e1134135deb17e0b1C1cdBF',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xc66eD7c8034E11EBd32499389C35b3E6E9eE3e78',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x75e66d062a2a8BE5c99d71db11d72aB3B82bA8b3',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xBb7aB09971E56Aaf248dCc6C3DF865aF69D97372',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x8283DD24f8D8E7b083e2855a4c3EA1A7Feba08C2',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ],
  [
    UniswappyV2EthPair {
      _marketAddress: '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x12EDE161c702D1494612d19f05992f43aa6A26FB',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xCe407CD7b95B39d3B4d53065E711e713dd5C5999',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xB6909B960DbbE7392D405429eB2b3649752b4838',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xBb2b8038a1640196FbE3e38816F3e67Cba72D940',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x9896BD979f9DA57857322Cc15e154222C4658a5a',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x598E740cda7C525080d3FCb9Fa7C4E1bd0044B34',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x43AE24960e5534731Fc831386c07755A2dc33D47',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x231F3381D10478BfC2cA552195b9d8B15968B60c',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x3b0F0fe3Be830826D833a67cD1d7C80edF3Fb49b',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x67660E35fee501d0876B9493bb5eC90E10675957',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x260E069deAd76baAC587B5141bB606Ef8b9Bab6c',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x5D27dF1a6E03254E4f1218607D8E073667ffae2F',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xB784CED6994c928170B417BBd052A096c6fB17E2',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xa2107FA5B38d9bbd2C461D6EDf11B11A50F6b974',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x718Dd8B743ea19d71BDb4Cb48BB984b73a65cE06',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x55D5c232D921B9eAA6b37b5845E439aCD04b4DBa',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xa5E79baEe540f000ef6F23D067cd3AC22c7d9Fe6',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xC2aDdA861F89bBB333c90c492cB837741916A225',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0x99731C13ef1aaB58e48FA9a96deFEFdf1b8DE164',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xad3B5027d090b7bc120Dc264906ca4642b0fb9F3',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    },
    UniswappyV2EthPair {
      _marketAddress: '0xF49144E61C05120f1b167E4B4F59cf0a5d77903F',
      _tokens: [Array],
      _protocol: '',
      _tokenBalances: [Object]
    }
  ]
]
