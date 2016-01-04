# spacy is used for pre-processing and traditional NLP
import spacy
from spacy.en import English

# Gensim is used for LDA and word2vec
from gensim import Word2Vec

# Write a function that can take a take a sentence parsed by `spacy` and 
# identify it mentions a company named 'Google'. 
# Remember, `spacy` can find entities and codes them `ORG` if they are a company.


# Write a function that can take a sentence parsed by `spacy` 
# and return the verbs of the sentence (preferably lemmatized)

# Write a function that identifies countries - HINT: the entity label for 
# countries is GPE  (or GeoPolitical Entity)


if __name__ == '__main__':
    # Loading the tweet data
    tweets = [tweet for tweet in open('../../assets/data/captured-tweets.txt', 'r')]

    # Setting up spacy
    nlp_toolkit = English()
