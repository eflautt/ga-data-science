---
title: Decision Trees and Random Forests
duration: "3:00"
creator:
    name: Arun Ahuja
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Decision Trees & Random Forests
Week 6 | Lesson 12

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand and build decision tree models for classification and regression
- Understand the differences between linear and non-linear models
- Understand and build random forest models for classification and regression
- Know how to extract the most important predictors in a random forest model

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Use seaborn to create plots
- Knowledge of a boostrap sample
- Previous lesson on overfitting
- Know how to build and evaluate _some_ classification model in sckit-learn using cross-validation and AUC

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Review materials & dataset

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Topic description  |
| 10 min  | [Introduction](#introduction)   | Topic description  |
| 15 min  | [Demo](#demo)  | Topic description  |
| 45 min  | [Guided Practice](#guided-practice)  | Topic description  |
| 25 min  | [Independent Practice](#ind-practice)  | Topic description  |
| 10 min  | [Conclusion](#conclusion)  | Topic description  |

---

## Review of the Modeling Assignment (30 min)

## Modeling and the Data Science Workflow (25 min)
#### The dataset

The dataset we will be looking at today is from [StumbleUpon](http://stumbleupon.com). StumbleUpon provides a service to recommend webpages to users, and mostly they would like these websites to be 'evergreen'.

What are 'evergreen' sites?

Evergreen sites are those that are always relevant. As opposed to breaking news or current events, evergreen websites are relevant no matter the time or season. This typically means websites that are **not** current events like recipes, how-to guides or art.

##### Exercises to explore the dataset (Independent Practice)
We will revisit our data science workflow to explore the dataset and answer questions about what are the most important characteristics for a webpage to be 'evergreen'.

1. In a group: 

Prior to looking at the available data, brainstorm 3 - 5 characteristics that would be useful for predicting evergreen websites

After looking at the dataset, can model or quantify any of the characteristics you wanted?
 - I.E. If you believe high-image content websites are likely to be evergreen how you can you build a feature that represents high image content
 - I.E. If you believe weather content is likely to NOT be evergreen how can you build a feature that represents that.

_See notebook for data dictionary_
_See notebook for starter code for exercises_

2. Does being a news site affect greeness? Compute or plot the percent of evergreen sites for news sites.
3. Does category in general affect greeness? Plot the rate of evergreen sites for all Alchemy categories.
4. How many articles are there per category?
4. Create a feature for the title containing 'recipe'. Is the % of evegreen websites higher or lower on pages that have recipe in the the title?

> Assess: Each student should build intuition for the dataset by plotting the requested features

##### Review the data science workflow

In this lesson we will focus on mining the dataset and building a model. We will focus on refining the model for the best predicitive ability.

## Introduction to Decision Trees (30 min)
#### Intuition

Decisions trees are similar to the game 20 questions. They make predictions by answering a series of questions, most often yes or no questions.  What we typically want is the smallest set of questions to get to to the right answer. We want each question to reduce our search space as much as possible.

_Trees_ are a data structure made up of _nodes_ and _branches_. Each node typically has two (or more) branches that connect it to it's children. Each child is another node in the tree and contains it's own _subtree_. Nodes without any children are known as _leaf_ nodes.

A _decision tree_ contains a question at every node. Depending on the answer to that question we will proceed down the left or right branch of the tree and ask another question. At the _leaf_ nodes, once we don't have any more questions, we make a prediction.

It's important to note the next question we ask is dependent on the last.  We'll see how this sets decision trees apart from previously seen models.

For example, suppose we want to predict if an article is a news article. We may start by asking does it mention a President? 
    - If it does, it must be a news article
    - If not, let's ask another question - does the article contain other political figures? etc.

Using our dataset from earlier. We want to predict whether an article is evergreen.  So our tree may look like:

#### Comparison to previous models 
Decision trees have an advantage over logistic regression by being _non-linear_. A _linear_ model is one in which a change in an input variable has a constant change on the output variable. 

Think of years of education and salary. We know that as education increases, salary should as well. A linear model would say this effect is constant.  As your years of education goes from 10 to 15 or 15 to 20, the increase in salary should be the same. A _non-linear_ allows us to change the effect depending on the input. We can say  that if the increase in salary due to a change in education of 10 years to 15 years is 20k, but from 15 years to 20k it might only be 5k or even negative.

Additionally, trees automatically contain interactions of features. Since each question is dependent on the last the features are naturally interacting.

#### Training a Decision Tree Model

Training a decision tree is about deciding on the best set of questions to ask. A good question will be one that best segregates the positive group from the negative group and narrows in on the correct answer. For example, in our toy problem of classifying news stories, the best question we can ask is one that creates 2 groups, one that is mostly news stories and on that is mostly non-news stories.

Like all data science techniques, we need to quantify this segregation.  We do that with any of the following metrics:

- [Classification Error]
- [Entropy]
- [Gini](https://en.wikipedia.org/wiki/Gini_coefficient)

Each of these measures the _purity_ of the separtion. Classification error asks, what percent are positive in each group. The lowest error would be a separation that has 100% positive in one group and 0% in the other (completely separating news stories from non-news stories.)

When training, we want to choose the question that gives us the best _change_ in our purity measure. Given our current set of data points (articles), what question will make the largest change in purity.

At each training step, we take our current set, choose the best feature to split on (the best question to ask) based on information gain and then have two new groups. This process is repeated _recursively_ for those two groups.

Let's build a sample tree for our evergreen prediction problem.  Assume our features are
    - whether the article contains the recipe
    - the image ratio
    - the html ratio

First, we want to choose the feature the gives us the highest purity. In this case, we choose the recipe feature

![](single-node-tree.png)

Then, we take each side of the tree and repeat the process. Choosing the feature that best splits the remaining samples. 

![](depth-2-tree.png)

As you can see the best feature is different on both sides of this tree. This shows the interaction of features. If the article does not contain 'recipe' we care about the image_ratio, but otherwise we don't.

We can continue that process until we have asked as many questions as we want or our leaf nodes are completely pure.


#### Making predictions from a Decision Tree

Predictions are made in the decision tree from answering each of the questions. Once we reach a leaf node, our prediction is made by taking the majority label of the training samples that fulfill the questions. If there are 10 training samples that match our new sample, and 6 are positive, we will predict positive since 6/10 (60%) are positive.

In the sample tree, if we want to classify a new article, we proceed by first asking - does the article contain word recipe. If it doesn't, we can check does the article have a lot of images. If it does, 630 / 943 articles are evegreen - so we assign a 0.67 probability to be evergreen.  

## Decision Trees in scikit-learn (60 min)

#### Training a model in sckit-learn (Demo) 

_See notebook for code_

> Assess: Each student should evaluate the decision tree model using previous techniques in cross-validation

#### Overfitting in a Decision Tree (Practice) 

Decision trees tend to be weak models, mostly because they can memorize or overfit to a dataset.  Remember, a model is _overfit_ when it instead of picking up on general trends in the data it memorizes or bends to a few specific examples. If we simply memorized each article and it's classification we would overfit. This is akin to utilizing every word in every article as a feature.

Revisiting our predicting news article example.  We could ask the following questions
  
- Is the first word 'The'?
- Is the second word 'president'
- Is the third word 'of'
- etc.

This model is attempting to recreate the articles exactly as opposed to learning any general trend.

An uncontrainsed decision tree can learn a fairly extreme tree. ![](complex-tree.png)

We can limit this in decision trees in a few ways
  - Limiting the number of questions (nodes) a tree can have
  - Limiting the number of samples in the leaf nodes 

_See notebook for code_

#### Exercises (Independent Practice)

> Assess: Each student should adjust the given model using the `max_depth` and `min_samples_in_leaf` parameters

## Random Forests (30 min)

Random Forests are some of the most widespread classifiers used.  They are relatively simple to use (very few parameters to set and easy to avoid overfitting). 

Random Forests are an _ensemble_ or collection of decision trees.

Advantages:
- Easy to tune, built-in protection against overfitting, no regularization
- Non-linear
- Built-in interaction effects

Disadvantages:
- Slow
- Black-box
- No "coefficients", we don't know what positively or negatively impacts a website being evergreen

#### Training a Random Forest

Training a Random Forest model involves training many decision tree models.  Since decision trees overfit very easily, we use many decision trees together and randomize the way the way they are created.

1. Take a bootstrap sample of the dataset
2. Train a decision tree on the bootstrap sample
2a. For each split/feature selection, only evaluate a _limited_ number of features to find the best one.
3. Repeat this for _N_ trees

#### Predicting using a Random Forest 

Predictions from a Random Forest come from each decision tree.  Each tree makes an individual prediction. The individual predictions are combined in a majority vote.

#### Random Forest in scikit-learn (Demo)

_See notebook for code_

The key parameter to remember is `n_estimators` - the number of trees to use in the model.

#### Exercises (Independent Practice)

> Assess: Each student should adjust the given model using the `n_estimators` parameter

#### Retrieving the important aspects of the model (Demo/Code-along)

Random Forests have a good way of extracting what features are important. Unlike we Logistic Regression, we don't have coeffcients that tell us whether some input postively or negatively affects our output. But we can keep track of which inputs are most important. we do this by keeping track of the features give us the best splits.

_See notebook for code_

#### Regression with Decision Trees and Random Forests

The same models, both decision trees and random forests can be used for both classification and regression. While predictions for classification problems are made by predicting the majority class in the leaf node, in regression, predictions are made by predicting the average value of the samples in the leaf node.

## Independent Practice (25 minutes)

1. Continue adding input variables to the model that you think make be relevant
2. For each feature
  - evaluate the model for improved predictive performance using cross-validation
  - evaluate the _importance_ of the feature

3. Bonus: Like the 'recipe' feature, add in similar text features and evaluate their performance

_See notebook for code_

> Assess: Each student should improve on their original model (in AUC) either by increasing the size of the model or adding in additional features


## Conclusion (5 mins)
- Decision trees are non-linear models that can be used for classification or regression.
- Training involves using the data to decide the best questions to separate the data into our two classses and predictions are made by answering those questions
- Decision trees are typically weak models and overfit very easily
- Random forests are collections of decision trees and are much more powerful models
- While they are very good predictive models they are more often a black-box and lack the explanatory features of linear/logistic regression
