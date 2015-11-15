function pos_wrap(data1){
  new Chartist.Bar('#positive-chart', {
    labels: ['1', '2', '3', '4', '5'],
    series: [
      data1
    ]
  }, {
    height:200,
    seriesBarDistance: 20,
    reverseData: true,
    horizontalBars: true,
    axisY: {
      offset: 50
    }
  });
}

function neg_wrap(data1){
  new Chartist.Bar('#negative-chart', {
    labels: ['1', '2', '3', '4', '5'],
    series: [
      data1
    ]
  }, {
    height:200,
    seriesBarDistance: 10,
    reverseData: true,
    horizontalBars: true,
    axisY: {
      offset: 50
    }
  });
}