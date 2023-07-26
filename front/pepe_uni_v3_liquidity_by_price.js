// import {data} from "./pepe_data";
var myChart = echarts.init(document.getElementById('main'));

// const data = [
//   [10, 16, 3, 'A'],
//   [16, 18, 15, 'B'],
//   [18, 26, 12, 'C'],
//   [26, 32, 22, 'D'],
//   [32, 56, 7, 'E'],
//   [56, 62, 17, 'F']
// ].map(function (item, index) {
//   return {
//     value: item,
//     itemStyle: {
//       color: '#604a7b'
//     }
//     // itemStyle: {
//     //   color: colorList[index]
//     // }
//   };
// });

const data = [
  [1.29, 6.02, 2103],
  [6.02, 8.29, 88559],
  [8.29, 16.36, 123213],
  [16.36, 16.69, 756733],
  [16.69, 18.08, 1053381],
  [18.08, 26.97, 1151028],
  [26.97, 28.64, 1336933],
  [28.64, 29.22, 1473375],
  [29.22, 30.41, 2031271],
  [30.41, 32.94, 2097730],
  [32.94, 34.98, 2063076],
  [34.98, 39.44, 3270249],
  [39.44, 40.24, 3084344],
  [40.24, 47.22, 12439245],
  [47.22, 50.14, 13302533],
  [50.14, 57.67, 13204886],
  [57.67, 63.74, 13116288],
  [63.74, 69.05, 14554617],
  [69.05, 74.80, 23867593],
  [74.80, 76.31, 26144806],
  [76.31, 77.85, 33719635],
  [77.85, 79.42, 33491977],
  [79.42, 81.03, 32936223],
  [81.03, 84.33, 32639575],
  [84.33, 86.04, 32006055],
  [86.04, 91.36, 69220281],
  [91.36, 93.20, 67136306],
  [93.20, 98.97, 64859094],
  [98.97, 103.00, 64737466],
  [103.00, 105.08, 56645177],
  [105.08, 107.21, 45851947],
  [107.21, 113.84, 44857617],
  [113.84, 120.88, 7643390],
  [120.88, 136.29, 7576932],
  [136.29, 211.61, 2103],
  [211.61, 217.09, 2103],
].map(function (item, index) {
  return {
    value: item,
    itemStyle: {
      color: '#4f81bd',
    }
    // itemStyle: {
    //   color: colorList[index]
    // }
  };
});

const option = {
  title: {
    text: 'PEPE/WETH',
    left: 'center'
  },
  tooltip: {},
  xAxis: {
    // type: "index",
    scale: true
  },
  yAxis: {},
  dataZoom:[
    // {
    //   type: 'inside',
    //   start: 30,
    //   end: 60
    // },
    {
      show: true,
      type: 'slider',
      top: '90%',
      start: 30,
      end: 60
    }
  ],
  series: [
    {
      type: 'custom',
      renderItem: function (params, api) {
        var yValue = api.value(2);
        var start = api.coord([api.value(0), yValue]);
        var size = api.size([api.value(1) - api.value(0), yValue]);
        var style = api.style();
        return {
          type: 'rect',
          shape: {
            x: start[0],
            y: start[1],
            width: size[0],
            height: size[1]
          },
          style: style
        };
      },
      label: {
        show: false,
        position: 'top'
      },
      dimensions: ['start', 'end', 'liquidity'],
      encode: {
        x: [0, 1],
        y: 2,
        tooltip: [0, 1, 2],
        // itemName: 3
      },
      data: data,
      markLine: {
        symbol:"none",               //去掉警戒线最后面的箭头
        label:{
          position:"start"          //将警示值放在哪个位置，三个值“start”,"middle","end"  开始  中点 结束
        },
        data : [
          {
            silent:false,             //鼠标悬停事件  true没有，false有
            lineStyle:{               //警戒线的样式  ，虚实  颜色
              // type:"solid",
              color:"#FA3934",
              width: 4,
            },
            xAxis:  100               // 警戒线的标注值，可以有多个yAxis,多条警示线   或者采用   {type : 'average', name: '平均值'}，type值有  max  min  average，分为最大，最小，平均值
          }
        ]
      }
    },
    // {
    //   type:"line",
    // }
  ]
};

myChart.setOption(option);