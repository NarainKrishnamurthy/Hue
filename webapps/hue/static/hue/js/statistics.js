function pos_wrap(data1){
  new Chartist.Bar('#positive-chart', {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    series: [
      data1
    ]
  }, {
    seriesBarDistance: 10,
    reverseData: true,
    horizontalBars: true,
    axisY: {
      offset: 70
    }
  });
}

function neg_wrap(data1){
  new Chartist.Bar('#negative-chart', {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    series: [
      data1
    ]
  }, {
    seriesBarDistance: 10,
    reverseData: true,
    horizontalBars: true,
    axisY: {
      offset: 70
    }
  });
}