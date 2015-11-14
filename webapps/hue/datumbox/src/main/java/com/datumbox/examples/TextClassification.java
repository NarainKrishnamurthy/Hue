/**
 * Copyright (C) 2013-2015 Vasilis Vryniotis <bbriniotis@datumbox.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.datumbox.examples;



import com.datumbox.applications.nlp.TextClassifier;
import com.datumbox.common.dataobjects.Record;
import com.datumbox.common.persistentstorage.ConfigurationFactory;
import com.datumbox.common.persistentstorage.interfaces.DatabaseConfiguration;
import com.datumbox.common.utilities.PHPfunctions;
import com.datumbox.common.utilities.RandomGenerator;
import com.datumbox.framework.machinelearning.classification.MultinomialNaiveBayes;
import com.datumbox.framework.machinelearning.common.bases.mlmodels.BaseMLmodel;
import com.datumbox.framework.machinelearning.featureselection.categorical.ChisquareSelect;
import com.datumbox.framework.utilities.text.extractors.NgramsExtractor;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.InputStream;
import java.io.PrintWriter;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.HashMap;
import java.util.Map;

/**
 * Text Classification example.
 * 
 * @author Vasilis Vryniotis <bbriniotis@datumbox.com>
 */
public class TextClassification {
    
    /**
     * Example of how to use the TextClassifier class.
     * 
     * @param args the command line arguments
     * @throws java.net.URISyntaxException
     */
    public static void main(String[] args) throws URISyntaxException {        
        /**
         * There are two configuration files in the resources folder:
         * 
         * - datumbox.config.properties: It contains the configuration for the storage engines (required)
         * - logback.xml: It contains the configuration file for the logger (optional)
         */

        String in_file_path = args[0];
        String out_file_path = args[1];
        System.out.println("in_file_path: " + in_file_path);
        System.out.println("out_file_path: " + out_file_path);
    	
        //Initialization
        //--------------
        RandomGenerator.setGlobalSeed(42L); //optionally set a specific seed for all Random objects
        DatabaseConfiguration dbConf = ConfigurationFactory.INMEMORY.getConfiguration(); //in-memory maps
        //DatabaseConfiguration dbConf = ConfigurationFactory.MAPDB.getConfiguration(); //mapdb maps
        
        
        
        //Reading Data
        //------------
        Map<Object, URI> dataset = new HashMap<>(); //The examples of each category are stored on the same file, one example per row.
        System.out.println(TextClassification.class.getResource("/src/main/resources/datasets/sentiment-analysis/rt-polarity.pos").toURI());
        InputStream pos_is = TextClassification.class.getClassLoader().getResourceAsStream("/datasets/sentiment-analysis/rt-polarity.pos");
        dataset.put("positive", TextClassification.class.getResource("/src/main/resources/datasets/sentiment-analysis/rt-polarity.pos").toURI());
        dataset.put("negative", TextClassification.class.getResource("/src/main/resources/datasets/sentiment-analysis/rt-polarity.neg").toURI());
        
        
        //Setup Training Parameters
        //-------------------------
        TextClassifier.TrainingParameters trainingParameters = new TextClassifier.TrainingParameters();
        
        //Classifier configuration
        trainingParameters.setMLmodelClass(MultinomialNaiveBayes.class);
        trainingParameters.setMLmodelTrainingParameters(new MultinomialNaiveBayes.TrainingParameters());
        
        //Set data transfomation configuration
        trainingParameters.setDataTransformerClass(null);
        trainingParameters.setDataTransformerTrainingParameters(null);
        
        //Set feature selection configuration
        trainingParameters.setFeatureSelectionClass(ChisquareSelect.class);
        trainingParameters.setFeatureSelectionTrainingParameters(new ChisquareSelect.TrainingParameters());
        
        //Set text extraction configuration
        trainingParameters.setTextExtractorClass(NgramsExtractor.class);
        trainingParameters.setTextExtractorParameters(new NgramsExtractor.Parameters());
        
        
        
        //Fit the classifier
        //------------------
        TextClassifier classifier = new TextClassifier("SentimentAnalysis", dbConf);
        classifier.fit(dataset, trainingParameters);
        
        
        
        //Use the classifier
        //------------------
        
        //Get validation metrics on the training set
        BaseMLmodel.ValidationMetrics vm = classifier.validate(dataset);
        classifier.setValidationMetrics(vm); //store them in the model for future reference
        
        //Classify a single sentence
        
       /*
        String sentence = "I love Hilary Clinton";
        Record r = classifier.predict(sentence);
        System.out.println("Classifing sentence: \""+sentence+"\"");
        System.out.println("Predicted class: "+r.getYPredicted());
        System.out.println("Probability: "+r.getYPredictedProbabilities().get(r.getYPredicted())); 
        
        System.out.println("Classifier Statistics: "+PHPfunctions.var_export(vm));
        System.out.println("evaluating input file"); */
        try {
			JsonReader reader = new JsonReader(new FileReader(in_file_path));
			PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(out_file_path)));
			boolean first = true;
			
			reader.beginObject();
			while(reader.hasNext()){
				String key = reader.nextName();
				if (key.equals("comments")){
					reader.beginArray();
					while(reader.hasNext()){
						reader.beginObject();
						while(reader.hasNext()){
							String tweet_key = reader.nextName();
							if (tweet_key.equals("text")){
								String line = reader.nextString();
								System.out.println(line);
								Record r_line = classifier.predict(line);
								if (!first){
									out.print(",");
								} else {
									first = false;
								}
								out.print(r_line.getYPredicted());
							} else {
								reader.skipValue();
							}
						}
						reader.endObject();
					}
					reader.endArray();
				}
			}
			
			/*
			String line = in.readLine();
			while(line != null){
				Record r_line = classifier.predict(line);
				out.println(line + "(" + r_line.getYPredicted() + ")");
				line = in.readLine();
			} */
			reader.endObject();
			reader.close();
			
			out.close();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        System.out.println("FINISHED");
 
        
        
        //Clean up
        //--------
        
        //Erase the classifier. This removes all files.
        classifier.erase();
    }
    
}
