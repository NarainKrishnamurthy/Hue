package com.datumbox.examples;

import java.util.ArrayList;

public class Comment {
	public String text;
	public Integer index;
	public ArrayList<Integer> similar;
	
	public Comment(String input_text, int input_index){
		text = input_text;
		index = input_index;
		similar = new ArrayList<Integer>();
		similar.add(index);
	}
	
	public String toString(){
		return "line: " + text + "\nindex: " + index + "\nsimilar: " + similar;
	}
}
