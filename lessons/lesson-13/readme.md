---
title: Natural Language Processing (NLP) and Text Classification
duration: "3:00"
creator:
    name: Arun Ahuja
    city: NYC
---


# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Natural Language Processing and Text Classification
Week # | Lesson 13

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Define natural language processing
- List common tasks associated with:
  - use-cases
  - tokenization
  - tagging 
  - parsing
- Demonstrate how to classify text or documents using `scikit-learn`

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Experience with sckit-learn classifiers, specifically Random Forests and Decision trees
- Install `spacy` with `pip install spacy` (or use Anaconda)
- Run the `spacy` download data command
  ```python
  python -m spacy.en.download --force all
  ```

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Install `spacy` with `pip install spacy` (or use Anaconda)
- Run the `spacy` download data command
  ```python
  python -m spacy.en.download --force all
  ```

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min  | [Opening](#opening)  | Decision Trees and Random Forests |
| 30 mins  | [Introduction](#introduction-nlp)   | Natural Language Processing (NLP)  |
| 30 mins  | [Demo](#demo-spacy)  | NLP with spacy in Python  |
| 30 mins  | [Introduction](#introduction-classification)   | Text Classification  |
| 30 mins  | [Demo](#demo-text-sklearn)  | Text Classification with scikit-learn |
| 30 mins  | [Independent Practice](#ind-practice)  | Text Classification with scikit-learn  |
| 10 mins  | [Conclusion](#conclusion)  |   |

---
<a name="opening"></a>
## Review: Decision Trees and Random Forests  (10 mins)
Recall definitions of Decision Trees and Random Forests from previous lesson.

**Check:** What are some important features of decision trees and random forests?
  - Decision trees are weak learners that are easy to overfit
  - Random forests are strong models that made up a collection of decision trees
    - They are non-linear (while logistic regression is linear)
    - They are mostly black-boxes (no coefficients, but we do have a measure of feature importance)
    - They can be used for classification or regression

<a name="introduction-nlp"></a>
## Introduction: Natural Language Processing (30 mins)

### What is Natural Language Procesing (NLP)

Natural language processing is the task of extracting meaning and information from text documents. There are many pieces of information we want to extract.  These might include simple classification tasks, such as deciding what category a piece of text falls into or what tone it has as well as more complex tasks like translating or summarizing text.

Most AI or assistant systems are typically powered by fairly advanced NLP engine. A system like Siri uses voice-to-transcription to record the command and then various NLP algorithms to identify the question asked and possible answers.

For any of the tasks, from classification to translation, a fair amount pre-processing is required to make the text digestible for our algorithms. Typically we need to add some structure to the text (unstructured data) before we can make decisions based on it.


### Tokenization

Tokenization is the task of separating a sentence into it's constiuient parts, or **tokens**. How do we know what the "words" are in a particular sentence? While this may seem easy (for example, we can separate words using spaces or pauses) it becomes more complex when we consider unusual punctuation (common in social media) or different language conventions.

For example, can you spot any potential difficulties with this sentence?
_The L.A. Lakers won the NBA championship in 2010, defeating the Boston Celtics._


To perform a proper analysis, we need to be able to identify that:
- The periods in _L.A._ don't mark the end of a sentence but an abbreviation.
- _L.A. Lakers_ and _Boston Celtics_ are one concept.
- _"2010"_ is the word used, not _"2010,"_


### Lemmatization and Stemming

Abbreviations, proper nouns, and dates can pose a problem but there are many other language features that also have to be broken down. Consider the terms 'bad' and 'badly' or 'different' and 'differences'. How can we describe the relationship between these terms?

Stemming and lemmatization are two solutions to this type of problem. Once we've identified the **tokens** of our sample text, we can use these tools to identify common roots.

**Stemming** is a crude process of removing common endings from sentences:
  - Stemming removes endings with `s`, `es`, `ly`, `ing`, and `ed`.

This is useful so that we can treat the word `happy` and `happily` similarly. 

There are many well-known stemmer functions that can import many of these common endings, most notably the [Porter stemmer](http://tartarus.org/martin/PorterStemmer/).

**Lemmatization** is a more refined version that attempts to accomplish the same goal as stemming, but uses specific language and grammar rules to do so. A lemmatizer relies on a large collection of pre-defined grammar rules to perform this task.

For example, we can identify that "bad" and "badly" are similar using stemming.  However, this heuristic won't be able to tell that "better" and "best" are similar. That's where lemmatization comes in handy.

**Check:** Can you think of other problem words or phrases that might require these tools?

### Parsing and Tagging

Another classic NLP problem involves _parsing_ text and _tagging_. In order to understand the various elements of a sentence, we need to **tag** important topics and **parse** their dependencies. Our goal is to successfully identify the actors and actions in the text in order to make informed decisions. 

For example if we are processing financial news, we might need to identify which companies are involved and any actions they are taking. We would then be able to create an alert when a specific company releases a new product.  

Alternatively, if we are writing an assistant application, we might need to identify command phrases and determine what is being asked. For instance, given the phrase: 'Siri, what time is my next appointment?' what needs to be tagged and what needs to be parsed?

Tagging and parsing is in fact made up of a few overlapping sub-problems:
  - "Parts of speech" tagging:
    - Can we identify the parts of speech in a sentence? Which is the noun, verb, adjective, etc?
  - Chunking:
    - Can we identify the pieces of the sentence that go together in meaningful chunks? For instance, noun or verb phrases?
  - Named entity recognition:
    - Can we identify *specific* proper nouns? Can we pick out people and locations?

As you can see, NLP requires a large number of overlapping rules and dictionaries; however, the potential benefits are enormous.

**Check:** How might NLP be applied within your current jobs or final projects? What are some potential use-cases?

***

<a name="demo-spacy"></a>
## Demo / Codealong: Natural Language Processing with 'spacy'

Most techniques for NLP involve pre-processing large collections of annotated text in order to learn specific language rules. There are many of these systems in-use for English and other popular languages, but some languages tend to have fewer tools available. Each tool typically uses a large amount of data to learn general rules and patterns for its task. Many require large databases of special use-cases, since languages like English are full of inconsistencies.

Two popular NLP toolkits in Python are `nltk` and `spacy`. `nltk` is the most popular, but it hasn't kept up with advances and isn't very well maintained. `spacy` is more modern, but isn't available for commercial-use.

We'll be using `spacy` in this class, although `nltk` has a similar interface and functionality. Most of the utilities and individual tasks we'll be performing also have their own specialized tools available as well.

Let's start by attempting to process some of the titles. 

First, we'll load our NLP toolkit by specifying the language:

  ```python
  from spacy.en import English

  nlp_toolkit = English()
  ```

  This toolkit has 3 pre-processing engines.
    - a tokenizer: to identify the word tokens
    - a tagger: to identify the concepts described by the words
    - a parser: to identify the phrases and links between the different words

Each of these pre-processing can be overridden with a specific tool you have (you may want a specialized tokenizer or stock quotes or instagram posts compared to news headlines). You could write your own tokenizer or tagger for those tasks and use them in place of the default ones `spacy` provides, but we will use the defaults for now.

The first title is:
 > IBM Sees Holographic Calls, Air Breathing Batteries

 [http://www.bloomberg.com/news/articles/2010-12-23/ibm-predicts-holographic-calls-air-breathing-batteries-by-2015](http://www.bloomberg.com/news/articles/2010-12-23/ibm-predicts-holographic-calls-air-breathing-batteries-by-2015)

 From this we may wish to extract that it references a company and the company is referencing a new possible product: air-breathing batteries.

 ```python

 title = "IBM sees holographic calls, air breathing batteries"
 parsed = nlp_toolkit(title)

 for (i, word) in enumerate(parsed): 
    print("Word: {}".format(word))
    print("\t Phrase type: {}".format(word.dep_))
    print("\t Is the word a known entity type? {}".format(word.ent_type_  if word.ent_type_ else "No"))
    print("\t Lemma: {}".format(word.lemma_))
    print("\t Parent of this word: {}".format(word.head.lemma_))
```

The `nlp_toolkit` here runs each of the individual pre-processing tools. First tokenizing the sentence, identifying the components and building an interpretation of the sentence.

Output:

```Word: IBM 
   Phrase type: nsubj
   Is the word a known entity type? ORG
   Lemma: ibm
   Parent of this word: see
Word: sees 
   Phrase type: ROOT
   Is the word a known entity type? No
   Lemma: see
   Parent of this word: see
Word: holographic 
   Phrase type: amod
   Is the word a known entity type? No
   Lemma: holographic
   Parent of this word: call
Word: calls
   Phrase type: dobj
   Is the word a known entity type? No
   Lemma: call
   Parent of this word: see
Word: , 
   Phrase type: punct
   Is the word a known entity type? No
   Lemma: ,
   Parent of this word: call
Word: air 
   Phrase type: compound
   Is the word a known entity type? No
   Lemma: air
   Parent of this word: breathing
Word: breathing 
   Phrase type: compound
   Is the word a known entity type? No
   Lemma: breathing
   Parent of this word: battery
Word: batteries
   Phrase type: conj
   Is the word a known entity type? No
   Lemma: battery
   Parent of this word: call
```

In this output, 
- "IBM" is identified as an organization (ORG). 
- We identify a phrase 'holographic calls' 
- We identify a compand noun phrase at the end - 'air breathing batteries'.
- We can that 'see' is at a root as it is the action 'IBM' is taking.
- Additionally, we can see that 'batteries' was lemmatized to 'battery'.

We can also use this to find all titles that discuss an organization.

```python
def references_organization(title):
  parsed = nlp(title)
  return any([word.ent_type_ == 'ORG' for word in parsed])

data['references_organization'] = data['title'].fillna('').map(references_organization)

data[data['references_organization']][['title']].head()
```

**Check:** Write function to identify titles that have mention an organization (ORG) and person (PERSON)

Solution:
```python
def references_organization_and_person(title):
    parsed = nlp(title)
    has_org = any([word.ent_type_ == 'ORG' for word in parsed])
    has_person = any([word.ent_type_ == 'PERSON' for word in parsed])
    return has_org and has_person

data['references_organization_and_person'] = data['title'].fillna('').map(references_organization_and_person)  
data[data['references_organization_and_person']][['title']].head()
```

### Common Problems in NLP

It's important to keep in mind that each of these subtasks are still very difficult because of the complexity of language. Most often we are looking for heuristics to search through large amounts of text data. There is still a lot of active research in each of these areas.

In the last few years there has been less focus on the rule-based systems seen here to more flexible approaches. While these techniques first attempt to uncover the rules of the language and then use those rules to understand text, modern approaches do not attempt to _parse_ or understand the structure of a sentence and instead just rely on what words are used.

We will see those approaches in the next class.

***

<a name="introduction-classification"></a>
## Introduction: Text Classification (20 mins)

Text classification is the task of predicting what category or topic a piece of text is from. We may want to identify whether an article is a sports or a business story.  We may want to identify whether an article is positive in sentiment or negative in sentiment.

Typically this is done by using the text as the features or input to the model, and as in previous classifications using the label (sports or business, positive or negative) as the target or output to train on.

When we want to include the text as features, we usually create a _binary_ feature for each word. Then each feature boils down do - "does this piece of text contain that word?"

To do this, we first need to create a vocabulary, where we know all of the possible words in our universe. We will do this in a data-driven way, usually, taking all of the words that appear in our corpus. We filter them based on occurrence or usefulness.

We have many encoding or representation questions along the way.
  - Does the order of words matter?
  - Does punctuation matter?
  - Upper or lower case? Should we treat Python different from python?

The answer to each of these is problem dependent, but each will affect the modeling problem.

- Order of words may matter
  - If we are predicting postive or negative sentiment, 
- Punctuation may matter
  - Again in sentiment prediction, saying "amazing!!!" may be different than "amazing."
- Case may matter
  - "Python" is more likely to refer to a programming language, while "python" may refer to a programming language or a snake.

Classification using the words as features is known as **bag-of-words** classification.


**Check:** Identify common classification tasks for text documents.
***

<a name="demo-text-sklearn"></a>
## Demo / Codealong: Text Processing in scikit-learn (# mins)

Scikit-learn has many pre-processing utilities to make many of the tasks of converting text into feature for a model easy. These are in the `sklearn.preprocesing.text` package.

We will use the StumbleUpon web crawl dataset again and perform a text classification text. Instead of using other features of the webpages, we will use the text content itself to predict whether or not the webpage is 'evergreen'.

#### CountVectorizer

There are built-in utilities to pull out features from text in `scikit-learn` - most importantly `CountVectorizer`. It converts a collection of text, into a matrix of features.  Each row will be a sample (an article or piece of text) and each column will be a text feature (usually a count or binary feature per word).

`CountVectorizer` takes a column of text and creates a new dataset - one row per piece of text (i.e. one row per title) and generates a feature for **every** word in the all of the titles.

REMEMBER: Using all of the words can be very useful, but we need to remember to use regularization to avoid overfitting. Otherwise, using a rare words may result in the model learning something when it is not generalizable.

For example, if we attempting to predict sentiment and see an article that has the word "bessst!", we may link this word to positive sentiment. But, very few articles in the future may use this word, so it may not be useful to keep in our model. 

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features = 1000, 
                             ngram_range=(1, 2), 
                             stop_words='english',
                             binary=True)
```


`CountVectorizer` arguments
        - `ngram_range` - a range of of length of phrases to use 
            - `(1,1)` means use all single words
            - `(1,2)` all contiguous pairs of words
            - `(1,3)` all triples etc.
        - `stop_words='english'`
           - Stop words are non-content words - (to, the, it, at, what).  
           - They aren't helpful for prediction (most of the time) and this parameter removes them.
        - `max_features=1000` 
          - maximum number of words to consider (uses the first N most frequent)
        - `binary=True` 
          - to use a dummy column as the entry (1 or 0, as opposed to the count)
          - This is useful if you think a word appearing 10 times is not more important than whether the word appearing at all.

Like models or estimators in `scikit-learn`, vectorizers follow a similar interface.  
  - We create a vectorizer object with the parameters of our feature space. 
  - We `fit` a vectorizer to learn the vocabulary
  - We `transform` a set of text into that feature space.

The distinction of `fit` and `transform` when it comes to splitting datasets into training and test sets. We want to fit (or learn our vocabulary) from our training set. Since choosing features is a part of our model building process, we **should not** look at our test set to do this.

Whenever we want to make predictions, we will need to create a new data point that contains **exactly** the same columns as our model.  If feature 234 in our model represents the word 'cheeseburger', then we need to make sure our test or future example also has 'cheeseburger' as feature 234. We can use`transform` to do perform this conversion on the test set (and any future dataset) in the same way.

```python

titles = data['title'].fillna('')

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features = 1000, 
                             ngram_range=(1, 2), 
                             stop_words='english',
                             binary=True)

# Use `fit` to learn the vocabulary of the titles
vectorizer.fit(titles)

# Use `tranform` to generate the sample X word matrix - one column per feature (word or n-grams)
X = vectorizer.transform(titles)
```

- Build a random forest model to predict evergreeness of a website using the title features

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 20)
    
# Use `fit` to learn the vocabulary of the titles
vectorizer.fit(titles)

# Use `tranform` to generate the sample X word matrix - one column per feature (word or n-grams)
X = vectorizer.transform(titles)
y = data['label']

from sklearn.cross_validation import cross_val_score

scores = cross_val_score(model, X, y, scoring='roc_auc')
print('CV AUC {}, Average AUC {}'.format(scores, scores.mean()))
```

#### Term Frequency - Inverse Document Frequency (TF-IDF)

An alternative representation of, rather than the _bag-of-words_ approach from `CountVectorizer` is a TF-IDF representation.  TF-IDF stands for Term Frequency - Inverse Document Frequency.

As opposed to using the count of words as features, TF-IDF uses the product of two intermediate values, the Term Frequency and the Inverse Document Frequency.

The Term Frequency is equivalent to the `CountVectorizer` features, the number of times (or count) that a word appear in the document.  This is our most basic representation of text.

To define Inverse Document Frequency, first let's define Document Frequency.  **Document Frequency** is the % of documents that a particular word appears in.  For example, you could assume `the` appears in 100% of documents, while words like `Syria` would have low document frequency.  

**Inverse Document Frequency** is simply `1 / Document Frequency` (although frequently this is altered to `log(1 / Document Frequency)`). 

Looking at our final term:
  Term Frequency * Inverse Document Frequency 
  = Term Frequency / Document Frequency.  

The intuition behind a TF-IDF representation is that words that have high weight are those that either appear frequently in this document or appear in rarely in other documents (somehow unique to this document).

This is a good alternative to using a static set of stop-words.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

```

`TfidfVectorizer` follows the same `fit` and `fit_transform` interface of `CountVectorizer`.

**Check:** Have the student use `TfidfVectorizer` to create a feature representation of the titles.

***

<a name="ind-practice"></a>
## Independent Practice: Text Classification in scikit-learn (# minutes)

- Tie together the text features of the title with one more feature sets from the previous random forest model. Train and model and see if this improves the AUC.
- Use the `body` text instead of the `title` text - is this an improvement?
- Use `TfIdfVectorizer` instead of `CountVectorizer` - is this an improvement?

**Check:** Can the student prepare a model that uses both quantitative features and text features? Does this model improve the AUC?

***

<a name="conclusion"></a>
## Conclusion (5 mins)

- Natural language processing is the task of pulling meaning and information from text
- This typically involves solving many subproblems - tokenizing, cleaning (stemming and lemmatization) and parsing.
- After we have structured our text somewhat, we can use the identified features of the text for other tasks: classification, summarization, translation.
- In `scikit-learn` we use vectorizers to create text features for classification, either `CountVectorizer` or `TfIdfVectorizer`


***

### BEFORE NEXT CLASS
|   |   |
|---|---|
| **HOMEWORK** | |
| **UPCOMING PROJECTS**  | |

### ADDITIONAL RESOURCES
- [Natural Language Understanding: Foundations and State of the Art](icml.cc/2015/tutorials/icml2015-nlu-tutorial.pdf)
- [Text Mining Online](http://textminingonline.com/)
