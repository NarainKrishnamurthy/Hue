# Hue - Crowd Sentiment Analyzer (Hack Princeton 2015)

# Inspiration
Being on social media is akin to being constantly surrounded by other's perspectives, beliefs, and standards. We thought of the important of crowd sentiment in recent historical events and wondered why there was no simple platform for quickly gauging both positive and negative sentiment toward particular topics.

# What it does
Hue mines Twitter and Reddit to determine crowd sentiment, both positive and negative, toward a particular topic. Using sentiment analysis, Hue aggregates similar opinions to determine the 5 most popular positive and negative notions towards the topic

# How we built it
We used the Twitter and Reddit APIs to extract large sets of public messages for specific topics. We utilized NTLK, WordNet, and the semantic methods described in "Sentence Similarity Based on Semantic Nets and Corpus Statistics" Yuhua Li et al, 2006 to determine sentiment and semantic meaning of messages. On the front-end, we utilized Chartist.js and Bootstrap to render our data and views.


## Backend
- Extract text corpus on topic. Solution: Reddit, FB, and Twitter APIs
- Classify comments into positive and negative using sentiment analysis. Solution: (http://www.datumbox.com/)
- Compute the popularity of each comment by weighting likes, upvotes, etc.

For each comment:
- ~~Correct words:~~ http://norvig.com/spell-correct.html
- Expand all acronyms to their full words. Inject some synonyms for the key nouns in the sentence (taking care NOT to inject synonyms for the, at, for). Solution: Wordnet (https://wordnet.princeton.edu/)
- /* Optional */ Count the comment geographies 

Combine all comments using sentiment analysis
- Compare the two sentences to determine if they have the same meaning. Solution: SEMILAR (http://deeptutor2.memphis.edu/Semilar-Web/public/semilar-api.html)

- Find the top 10 positive and negative comments (by popularity)
