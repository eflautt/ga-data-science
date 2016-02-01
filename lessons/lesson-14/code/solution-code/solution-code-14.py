# spacy is used for pre-processing and traditional NLP
import spacy
from spacy.en import English

# Gensim is used for LDA and word2vec
from gensim.models.word2vec import Word2Vec

# Solution for 1a/b
# Write a function that can take a take a sentence parsed by `spacy` and 
# identify if it mentions a company named 'Google'. 
# Remember, `spacy` can find entities and code them `ORG` if they are a company.
def mentions_company(parsed, company='Google'):
    for entity in parsed.ents:
        if entity.text == company and entity.label_ == 'ORG':
            return True
    return False

# Solution for 1c
# Write a function that can take a sentence parsed by `spacy` 
# and return the verbs of the sentence (preferably lemmatized)
def get_actions(parsed):
    actions = [el.lemma_ 
                for el in parsed 
                if el.pos == spacy.parts_of_speech.VERB
               ]
    return actions

# Solution for 1e
# Write a function that identifies countries - HINT: the entity label for 
# countries is GPE (or GeoPolitical Entity)
def mentions_country(parsed, country):
    for entity in parsed.ents:
        if entity.text == country and entity.label_ == 'GPE':
            return True
    return False


if __name__ == '__main__':
    # Loading the tweet data
    tweets = [unicode(tweet, errors='ignore') for tweet in open('../../assets/dataset/captured-tweets.txt', 'r')]

    # Setting up spacy
    nlp_toolkit = English()

    # Solution to 1d
    # For each tweet, parse it using `spacy` and print out if the tweet 
    # has 'release' or 'announce' as a verb.
    for tweet in tweets:
        parsed = nlp_toolkit(tweet)

        if mentions_company(parsed, 'Google'):
            actions = get_actions(parsed)
            if 'release' in actions or 'announce' in actions:
                print(tweet)

    # Solution to 1f
    # Re-run (d) find country tweets that discuss 'Iran' announcing or releasing.
    for tweet in tweets:
        parsed = nlp_toolkit(tweet)

        if mentions_country(parsed, 'Iran'):
            actions = get_actions(parsed)
            if 'release' in actions or 'announce' in actions:
                print(tweet)

    # Solution to 2a
    # First take the collection of tweets and tokenize them using `spacy`

    # Many solutions here!
    # I decided to lemmatized the verbs for easier searching and keep symbols
    # and punctuations

    text_split = [[x.text if x.pos != spacy.parts_of_speech.VERB else x.lemma_ 
                    for x in nlp_toolkit(t)] for t in tweets]

    # Solution to 2b
    # Build a `word2vec` model
    model = Word2Vec(text_split, size=100, window=4, min_count=5, workers=4)

    # Solution to 2c
    model.most_similar(positive=['Syria'])

    # Solution to 3
    # Filter tweets down to those that mention 'Iran' or similar entities and 
    # 'war' or similar entities

    # a: Using spacy
    for tweet in tweets:
        parsed = nlp_toolkit(tweet)
        if mentions_country(parsed, 'Iran') or mentions_country(parsed, 'Iraq'): # ... you could add more
            if 'attack' in get_actions(parsed):
                print(tweet)

    # b: using similarity scores
    for tweet in tweets:
        parsed = nlp_toolkit(tweet)

        similarity_to_iran = max([model.similarity('Iran', tok.text) for tok in parsed if tok.text in model.vocab], 0)
        similarity_to_war = max([model.similarity('war', tok.text) for tok in parsed if tok.text in model.vocab], 0)
        if similarity_to_iran > 0.75 and similarity_to_war > 0.75:
            print(similarity_to_iran, similarity_to_war, tweet)
