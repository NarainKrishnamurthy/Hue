#Backend
- Extract text corpus on topic. Solution: Reddit, FB, and Twiter APIs
- Classify comments into positive and negative using sentiment analysis. Solution: (http://www.datumbox.com/)
- Compute the popularity of each comment by weighting likes, upvotes, etc.

For each comment:
- Expand all acronyms to their full words. Inject some synonyms for the key nouns in the sentence (taking care NOT to inject synonyms for the, at, for). Solution: Wordnet (https://wordnet.princeton.edu/)
- /* Optional */ Count the comment geographies 

Combine all comments using sentiment analysis
- Compare the two sentences to determine if they have the same meaning. Solution: SEMILAR (http://deeptutor2.memphis.edu/Semilar-Web/public/semilar-api.html)

- Find the top 10 positive and negative comments (by popularity)
