#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

#define THRESHOLD 0.35

#include "rapidjson/document.h"
#include "rapidjson/prettywriter.h"
#include <cstdio>

using namespace rapidjson;
using namespace std;

#include "wn.h"

#include "sentence_similarity.h"
#include "wordnet_extended.h"

typedef WordnetExtended we;

struct comment {
  string text;
  int score;
};

vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

int max(vector<struct comment> list) {
  int max_score = -2;
  int max;
  for (int i = 0; i < list.size(); i++) {
    if (list[i].score > max_score) {
      max_score = list[i].score;
      max = i;
    }
  }
  return max;
}


int main(int argc, char **argv) {

  if (argc < 4) return 1;

  const char *INPUT_COMMENTS_FILE = argv[1];
  const char *INPUT_SENTIMENT_FILE = argv[2];
  const char *OUTPUT_FILE = argv[3];
  
  ifstream in(INPUT_COMMENTS_FILE);
  string json;
  getline(in, json);

  ifstream infile(INPUT_SENTIMENT_FILE);
  string sent_csv;
  getline(infile, sent_csv);
  vector<string> sentiment;
  split(sent_csv, ',', sentiment);
  
  Document comments;
  
  comments.Parse(json.c_str());
  
  printf("\nParsing to document succeeded.\n");

  vector<struct comment> Lp, Ln;

  we we("hue/semantic-similarity-master/src/WordNet-3.0/dict", "hue/semantic-similarity-master/dicts/freq.txt");
  we::UndirectedGraph g;
  SentenceSimilarityLi2006 ss(we);  

  for (int i = 0; i < sentiment.size(); i++) {
    struct comment c;
    c.text = comments["comments"][i]["text"].GetString();
    c.score = comments["comments"][i]["favorites"].GetInt() + comments["comments"][i]["retweets"].GetInt();
    if (sentiment[i] == "positive") Lp.push_back(c);
    else if (sentiment[i] == "negative") Ln.push_back(c);
  }

  std::sort(Lp.begin(), Lp.end(), [](const struct comment &a, const struct comment &b) -> bool {
      return a.score > b.score;
    });
  std::sort(Ln.begin(), Ln.end(), [](const struct comment &a, const struct comment &b) -> bool {
      return a.score > b.score;
    });

  for (int i = 0; i < Lp.size() - 1; i++) {
    for (int j = i + 1; j < Lp.size(); j++) {
      if (Lp[j].score < 0) continue;
      float s = ss.compute_similarity(Lp[i].text, Lp[j].text, g);
      if (s >= THRESHOLD) {
	Lp[i].score += Lp[j].score;
	Lp[j].score = -1;
      }   
    }
  }
  
  for (int i = 0; i < Ln.size() - 1; i++) {
    for (int j = i + 1; j < Ln.size(); j++) {
      if (Lp[j].score < 0) continue;
      float s = ss.compute_similarity(Ln[i].text, Ln[j].text, g);
      if (s >= THRESHOLD) {
	Ln[i].score += Ln[j].score;
	Ln[j].score = -1;
      }   
    }
  }
    
  struct comment max_pos[5];
  struct comment max_neg[5];

  for (int i = 0; i < 5; i++) {
    int m = max(Lp);
    max_pos[i] = Lp[m];
    Lp.erase(Lp.begin() + m);
    
    m = max(Ln);
    max_neg[i] = Ln[m];
    Ln.erase(Ln.begin() + m);
  }

  
  StringBuffer s;
  Writer<StringBuffer> writer(s);


  writer.StartObject();
  
  writer.String("comm_pos");
  writer.StartArray();
  for (int i = 0; i < 5; i++) {
    writer.StartObject();
    writer.String("text");
    writer.String(max_pos[i].text.c_str());
    writer.String("score");
    writer.Int(max_pos[i].score);
    writer.EndObject();
  }
  writer.EndArray();

  writer.String("comm_neg");
  writer.StartArray();
  for (int i = 0; i < 5; i++) {
    writer.StartObject();
    writer.String("text");
    writer.String(max_neg[i].text.c_str());
    writer.String("score");
    writer.Int(max_neg[i].score);
    writer.EndObject();
  }
  writer.EndArray();
  writer.EndObject();
			    
  
  ofstream out(OUTPUT_FILE);
  
  out << s.GetString() << endl;

  return 0;  
}
