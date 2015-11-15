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

var rdata_pos = rd['comm_pos'];
var rdata_neg = rd['comm_neg'];

var rpmax = data_pos[0]['score'];
var rnmax = data_neg[0]['score'];

var rpscore_arr = [];
var rnscore_arr = [];

var rpscore = 0;
var rnscore = 0;

for(var i=0; i<data_pos.length; i++){
  var rpstring = 'rpositive';
  var rnstring = 'rnegative';

  rpscore += ((5 - i) * data_pos[i]['score']);
  rnscore += ((5 - i) * data_neg[i]['score']);

  rpstring += (i + 1);
  rnstring += (i + 1);


  if (rdata_pos[i]['score'] > rpmax){
    rpmax = rdata_pos[i]['score'];
  }
  if (rdata_neg[i]['score'] > rnmax){
    rnmax = rdata_neg[i]['score'];
  }

  rpscore_arr[i] = rdata_pos[i]['score'];
  rnscore_arr[i] = rdata_neg[i]['score'];

  document.getElementById(rpstring).innerHTML = (i + 1) + "." + rdata_pos[i]['text'];
  document.getElementById(rnstring).innerHTML = (i + 1) + "." + rdata_neg[i]['text'];      
}
var rmain_max = Math.max(rnmax,rpmax);
for (var j=0;j < rdata_pos.length; j++){
  rpscore_arr[j] = 10*(rpscore_arr[j] / rmain_max);
  rnscore_arr[j] = 10*(rnscore_arr[j] / rmain_max);
}
rpscore_arr = rpscore_arr.filter(function (x) {return x >= 0;});
rnscore_arr = rnscore_arr.filter(function (y) {return y >= 0;});

rpos_wrap(rpscore_arr);
rneg_wrap(rnscore_arr);

var percentPos = Math.floor((pscore / (pscore + nscore))*100);

var p_total = pscore_arr.reduce(function (x, y) {return x+y;});
var n_total = nscore_arr.reduce(function (x,y) {return x+y;});

percentPos = Math.floor((p_total + n_total == 0) ? 0 : (p_total/(p_total + n_total)) * 100);
document.getElementById("senti_stat").innerHTML = percentPos + "%";
