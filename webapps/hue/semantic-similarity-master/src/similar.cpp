#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

#define INPUT_COMMENTS_FILE "comments.json"
#define INPUT_SENTIMENT_FILE "comments.csv"
#define OUTPUT_FILE "TopSentiments.json"
#define THRESHOLD 0.5

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


int main() {

  FILE *file = fopen(INPUT_COMMENTS_FILE, "r");

  char *json;
  size_t length;
  getline(&json, &length, file);
  fclose(file);

  ifstream infile(INPUT_SENTIMENT_FILE);
  string sent_csv;
  getline(infile, sent_csv);
  vector<string> sentiment;
  split(sent_csv, ',', sentiment);

  Document comments;
  
  comments.Parse(json);
  
  printf("\nParsing to document succeeded.\n");

  // Value& v = document["comments"][0]["text"];

  vector<struct comment> Lp, Ln;

  we we("/home/sohils/work/WordNet-3.0/dict", "../semantic-similarity-master/dicts/freq.txt");
  we::UndirectedGraph g;
  SentenceSimilarityLi2006 ss(we);  
  
  for (int i = 0; i < sentiment.size(); i++) {
    struct comment c;
    c.text = comments["comments"][i]["text"].GetString();
    c.score = comments["comments"][i]["favorites"].GetInt() + comments["comments"][i]["retweets"].GetInt();
    if (sentiment[i] == "positive") Lp.push_back(c);
    else if (sentiment[i] == "negative") Ln.push_back(c);
  }
  
  for (int i = 0; i < Lp.size() - 1; i++) {
    int i_score = Lp[i].score;
    for (int j = i + 1; j < Lp.size(); j++) {
      float s = ss.compute_similarity(Lp[i].text, Lp[j].text, g);
      if (s >= THRESHOLD) {
	Lp[j].score += i_score;
	Lp[i].score = -1;
      }   
    }
  }
  
  for (int i = 0; i < Ln.size() - 1; i++) {
    int i_score = Ln[i].score;
    for (int j = i + 1; j < Ln.size(); j++) {
      float s = ss.compute_similarity(Ln[i].text, Ln[j].text, g);
      if (s >= THRESHOLD) {
	Ln[j].score += i_score;
	Ln[i].score = -1;
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


  for (int i = 0; i < 5; i++) {
    cout << "Text: " << max_pos[i].text << " \nScore: " << max_pos[i].score << endl << endl;
  }
  
  cout << endl << endl;

  for (int i = 0; i < 5; i++) {
    cout << "Text: " << max_neg[i].text << " \nScore: " << max_neg[i].score << endl << endl;    
  }
  

  return 0;  
}
