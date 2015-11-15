from textblob import TextBlob
from pprint import pprint
import json
import csv

def analyze_sentiment(json_input_path, csv_path, threshold):
    with open(json_input_path) as data_file:    
        data = json.load(data_file)

    with open(csv_path, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        sentiment_list = []
        for comment in data["comments"]:
            sentiment = TextBlob(comment["text"]).sentiment.polarity
            if sentiment >= threshold:
                sentiment_list.append('positive')
            elif sentiment <= (-1*threshold):
                sentiment_list.append('negative')
            else:
                sentiment_list.append('neutral')

        writer.writerow(sentiment_list)
    
