var d = {{data_tw|safe}};
console.log(d);

var data_pos = d['comm_pos'];
var data_neg = d['comm_neg'];

var pmax = data_pos[0]['score'];
var nmax = data_neg[0]['score'];

var pscore_arr = [];
var nscore_arr = [];

var pscore = 0;
var nscore = 0;

for(var i=0; i<data_pos.length; i++){
  var pstring = 'positive';
  var nstring = 'negative';

  pscore += ((5 - i) * data_pos[i]['score']);
  nscore += ((5 - i) * data_neg[i]['score']);

  pstring += (i + 1);
  nstring += (i + 1);


  if (data_pos[i]['score'] > pmax){
    pmax = data_pos[i]['score'];
  }
  if (data_neg[i]['score'] > nmax){
    nmax = data_neg[i]['score'];
  }

  pscore_arr[i] = data_pos[i]['score'];
  nscore_arr[i] = data_neg[i]['score'];

  document.getElementById(pstring).innerHTML = (i + 1) + "." + data_pos[i]['text'];
  document.getElementById(nstring).innerHTML = (i + 1) + "." + data_neg[i]['text'];      
}
var main_max = Math.max(nmax,pmax);
for (var j=0;j < data_pos.length; j++){
  pscore_arr[j] = 10*(pscore_arr[j] /main_max);
  nscore_arr[j] = 10*(nscore_arr[j] /main_max);
}
pscore_arr = pscore_arr.filter(function (x) {return x >= 0;});
nscore_arr = nscore_arr.filter(function (y) {return y >= 0;});

pos_wrap(pscore_arr);
neg_wrap(nscore_arr);

var percentPos = Math.floor((pscore / (pscore + nscore))*100);

var p_total = pscore_arr.reduce(function (x, y) {return x+y;});
var n_total = nscore_arr.reduce(function (x,y) {return x+y;});

percentPos = Math.floor((p_total + n_total == 0) ? 0 : (p_total/(p_total + n_total)) * 100);
document.getElementById("senti_stat").innerHTML = percentPos + "%";

var data = {
  series: [percentPos, 100 - percentPos]
};