//=======================================================================
// Copyright 2013
// Authors: Xin Liu tonyxliu@hotmail.co.uk
//
// Distributed under GPL v2
//=======================================================================

#include <string>

#include "wn.h"

#include "sentence_similarity.h"
#include "wordnet_extended.h"

typedef WordnetExtended we;

using namespace boost;

void print_graph(we::UndirectedGraph & g);
void print_sim(std::string s1, std::string s2, float sim, float paper_sim = -1);

int main (int argc, char **argv) {

	//wninit2();

	//auto test0 = in_wn("boys",ALL_POS);
	//test0 = in_wn("boy",ALL_POS);
	//auto test1 = is_defined("boy",NOUN);

	//auto test = findtheinfo_ds("boys", NOUN, HYPERPTR, ALLSENSES);
	//auto test3 = findtheinfo_ds("boy", NOUN, HYPERPTR, 2);
	//auto test2 = read_synset(NOUN, 9890332, "boy");

	we we("/home/sohils/work/WordNet-3.0/dict",
	      "../dicts/freq.txt");
	we::UndirectedGraph g;

	//std::vector<std::string> v(2);
	//v[0] = "hammer";
	//v[1] = "nail";

	//we.build_synset_adjacency_list(v, g);

	//print_graph(g);
	//
	//we::vertex_t v1, v2;
	//auto dis = we.compute_distance(g, "hammer", "nail", v1, v2);

	//we.normalization(v);

	//auto freq_test = we.get_freq_weight("boy");
	
	SentenceSimilarityLi2006 ss(we);
	
	auto s = ss.compute_similarity("party rock is in the house tonight, everybody gonna have a good time", "i'm sexy and i know it, shuffling, shuffling, i'm sexy and i know it", g);
	std::cout << s  << std::endl;

	//morphinit();
	//auto t2 = morphstr("boys", NOUN);
	//auto t3 = morphword("boys", NOUN);
	//t2 = morphstr("she", NOUN);
	//t3 = morphword("she", NOUN);

	return 1;
}

void print_sim(std::string s1, std::string s2, float sim, float paper_sim)
{
	std::cout << s1 << " * " << s2 << "(sim:" << sim << ", paper-sim:" << paper_sim <<")\n";
}

void print_graph(we::UndirectedGraph & g)
{
	typedef boost::property_map<we::UndirectedGraph, boost::vertex_index_t>::type VertexIndex;
	VertexIndex index = get(boost::vertex_index, g);

	std::cout << "vertices(g) = ";
	boost::graph_traits < we::UndirectedGraph >::vertex_iterator vi, vend;
	for (boost::tie(vi, vend) = boost::vertices(g); vi != vend; ++vi) 
	{
		std::cout << "(" << g[*vi]->words[0] << " " << *vi << " " << g[*vi]->depth << "), ";
	}
	std::cout << "\n\n" << std::endl;

	
	std::cout << "edges(g) = ";
	boost::graph_traits<we::UndirectedGraph>::edge_iterator ei, ei_end;
	for (boost::tie(ei, ei_end) = edges(g); ei != ei_end; ++ei)
	{
		std::cout << "(" << g[index[source(*ei, g)]]->words[0]<<source(*ei, g)
		<< "," << g[index[target(*ei, g)]]->words[0] << target(*ei, g) << "," 
		<< g[index[target(*ei, g)]]->depth << "), ";
	}
	std::cout << "\n\n"  << std::endl;


	//graph_traits < we::UndirectedGraph >::out_edge_iterator out, out_end;
 // graph_traits < we::UndirectedGraph >::in_edge_iterator in, in_end;
	//std::cout << "out_edges(1): ";
 // for (boost::tie(out, out_end) = out_edges(1, g); out != out_end; ++out)
 //   std::cout << *out;
 // std::cout << std::endl << "in_edges(0): ";
 // for (boost::tie(in, in_end) = in_edges(1, g); in != in_end; ++in)
 //   std::cout << *in;
 // std::cout << "\n\n" << std::endl;
}
