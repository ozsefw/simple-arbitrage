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
  // [51.03, 60.36, 379476],
  // [60.36, 64.48, 380336],
  // [64.48, 66.85, 380798],
  // [66.85, 70.98, 382327],
  // [70.98, 72.27, 391693],
  // [72.27, 75.82, 392360],
  // [75.82, 76.28, 406688],
  // [76.28, 80.03, 412778],
  // [80.03, 80.99, 413426],
  // [80.99, 83.46, 427881],
  // [83.46, 85.49, 428560],
  // [85.49, 88.09, 429206],
  // [88.09, 88.62, 441837],
  // [88.62, 89.69, 451735],
  // [89.69, 90.23, 464281],
  // [90.23, 91.87, 472543],
  // [91.87, 94.10, 475117],
  // [94.10, 95.24, 475479],
  // [95.24, 96.39, 484092],
  // [96.39, 98.73, 491398],
  // [98.73, 101.13, 501120],
  // [101.13, 102.35, 508925],
  // [102.35, 105.46, 544134],
  // [105.46, 106.10, 544680],
  // [106.10, 107.38, 458079],
  // [107.38, 109.33, 444710],
  // [109.33, 111.98, 425082],
  // [111.98, 114.02, 431498],
  // [114.02, 114.70, 426022],
  // [114.70, 119.62, 430276],
  // [119.62, 130.89, 429609],
  // [130.89, 131.68, 421632],
  // [131.68, 136.50, 420987],
  // [136.50, 138.98, 420339],
  // [138.98, 139.82, 407793],
  // [139.82, 143.22, 411846],
  // [143.22, 144.08, 410317],
  // [144.08, 149.36, 407743],
  // [149.36, 156.70, 403489],
  // [156.70, 163.42, 387977],
  // [163.42, 172.49, 385936],
  // [172.49, 174.57, 379177],
  // [174.57, 182.06, 371371],
  // [182.06, 183.16, 364955],
  // [183.16, 184.26, 357363],
  // [184.26, 187.61, 348751],
  // [187.61, 188.73, 347960],
  // [188.73, 193.32, 346215],
  // [193.32, 195.65, 336317],
  // [195.65, 198.01, 323686],
  // [198.01, 199.21, 323255],
  // [199.21, 201.61, 322576],
  // [201.61, 202.82, 313210],
  // [202.82, 205.27, 313083],
  // [205.27, 206.51, 312958],
  // [206.51, 209.00, 311916],
  // [209.00, 227.31, 310957],
  // [227.31, 228.68, 304868],
  // [228.68, 235.65, 232860],
  // [235.65, 241.76, 232860],

  [57.99, 64.60, 3],
  [64.60, 65.77, 4],
  [65.77, 72.83, 4],
  [72.83, 73.27, 100],
  [73.27, 76.42, 4],
  [76.42, 110.85, 4],
  [110.85, 165.69, 5],
  [165.69, 184.59, 4],
  [184.59, 267.77, 3],
  [267.77, 274.71, 3],

  // [1.29, 6.02, 64651010],
  // [6.02, 8.29, 64737466],
  // [8.29, 16.36, 64772120],
  // [16.36, 16.69, 65405640],
  // [16.69, 18.08, 65702288],
  // [18.08, 26.97, 65799935],
  // [26.97, 28.64, 65985840],
  // [28.64, 29.22, 66122282],
  // [29.22, 30.41, 66680178],
  // [30.41, 32.94, 66746637],
  // [32.94, 34.98, 66711983],
  // [34.98, 39.44, 67919156],
  // [39.44, 40.24, 67733252],
  // [40.24, 47.22, 77088152],
  // [47.22, 50.14, 77951440],
  // [50.14, 57.67, 77853793],
  // [57.67, 63.74, 77765195],
  // [63.74, 69.05, 79203524],
  // [69.05, 74.80, 88516500],
  // [74.80, 76.31, 90793713],
  // [76.31, 77.85, 98368542],
  // [77.85, 79.42, 98140884],
  // [79.42, 81.03, 97585130],
  // [81.03, 84.33, 97288482],
  // [84.33, 86.04, 96654962],
  // [86.04, 91.36, 133869188],
  // [91.36, 93.20, 131785213],
  // [93.20, 98.97, 129508001],
  // [98.97, 103.00, 129386373],
  // [103.00, 105.08, 121294084],
  // [105.08, 107.21, 110500854],
  // [107.21, 113.84, 109506524],
  // [113.84, 120.88, 72292298],
  // [120.88, 136.29, 72225839],
  // [136.29, 211.61, 64651010],
  // [211.61, 217.09, 64651010],
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
    text: 'RLB/WETH',
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