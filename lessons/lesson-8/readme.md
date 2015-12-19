---
title: Introduction to Classification
duration: 3:00
creator:
    name: Ed Podojil
    city: NYC
    dataset: iris dataset
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to Classification
Week # | Lesson #

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Define class label and classification
- Build a K-Nearest Neighbors using the sci-kit-learn library
- Evaluate and tune model by using metrics such as classification accuracy/error

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Understand how to optimize for error in a model
- Understand the concept of iteration to solve problems
- measure basic probability

### INSTRUCTOR PREP
*Before this lesson, instructors will have to:*
- review materials
- be familiar with the datasets

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Discuss lesson objectives  |
| 10-15 mins  | [Introduction](#introduction-class) | What is Classification? |
| 30-35 mins  | [Independent Practice](#ind-practice-class)  | Basics of Classification Learning |
| 10-15 mins  | [Introduction](#introduction-knn)  | Introduction to K Nearest Neighbors |
| 20-25 mins  | [Guided Practice](#guided-practice-knn)  | Guided Practice: Implementing KNN |
| 30-35 mins  | [Independent Practice](#ind-practice-knn)  | Solving for K |
| 10-15 mins  | [Introduction](#introduction-eval)   | Additional Classification Metrics |
| 20-25 mins  | [Guided Practice](#guided-practice-eval)  | When to pick what metric? |
| 30-35 mins  | [Independent Practice](#ind-practice-eval)  | Evaluating alternative metrics for KNN |
| 5-10 mins  | [Conclusion](#conclusion)  | Review topics |

---

<a name="opening"></a>
## Opening (5 mins)

In class so far we've primarily worked with regression problems: machine learning approaches to solving or predicting, a continuous set of values. Since regressions are continuous (for example, 1 is greater than 0, and 100 is greater than 1), we've been able to use distance to measure how accurately our prediction is.

But, while predicting something like the cost of a house or number of clicks on an ad can exist within some range, other prediction problems, like if a loan is going to default or not, doesn't really have that range. It either is, or isn't!

How do we try **build** a model to predict set values, like a status, color, or gender of a baby? Do the same principals apply from working on a regression problem?

---

<a name="introduction-class"></a>
## Introduction: What is Classification (5 mins)

**Classification** is a machine learning problem for solving a set value given the knowledge we have about that value.

Many classification problems boil down to a *binary* problem. That is, it either _is_ something, or it _isn't_. For example, with patient data, one could be working on solving a treatment problem for smokers... but first we need to know if their medical history suggests, or is predictive, of the patient being a smoker or not.

Even if it doesn't seem like a binary problem, say, predicting if a pixel in a picture is red or blue, it still can boil down to a *boolean* value: with the picture example, we could change the problem to "is red" or "is not red."

Binary classification is the simplest form of classification, though a classification problem can certainly be wrapped around multiple _class labels_.

### What is a class label?

A class label is a representation of what we are trying to predict: our target. The examples of class labels from above would be:

data problem | class labels
-------------|--------------
Patient data problem | is smoker, is not smoker
pixel color | red, blue (green, orange, etc)

The easiest way to understand if our `y`, the dependent variable, is a classification problem or not, is to see if the values can be ordered given math. For example, if predicting revenue, $100MM is greater than $90MM (and more so, could be negative!), so revenue prediction sounds like a _regression_ problem. Red is not greater than or less than blue (at least, not in this context), therefore predicting this pixel is a _classification_ problem, with "red" and "blue" as the class labels.

<a name="guided-practice-class"></a>
## Guided Practice: Regression or Classification? (20 mins)

On your own, decide for each of the following situations if it is a regression problem, classification problem, or neither.

1. Using the total number of explosions in a movie, predict if the movie is by JJ Abrams or Michael Bay.
2. Determine how many tickets will be sold to a concert given who is performing, where, and the date and time.
3. Given the temperature over the last year by day, predict tomorrow's temperature outside.
4. Using data from four cell phone microphones, reduce the noisy sounds so the voice is crystal clear to the receiving phone.
5. With customer data, determine if a user will return or not in the next 7 days to an e-commerce website.

The primary difference between regression and classification is the _result_; the data used as input should resonate with what we've used in the past. In fact, writing a classifier could look a lot like control flow, a pattern in coding.

<a name="independent-practice-class"></a>
## Independent Practice: Build a classifier! (20 mins)

With our knowledge above on class labels and classification, we realize that it would be relatively straightforward to write a computer program that returns class labels based on some prior knowledge.

Our goal below is to (re) explore the iris dataset, which has 50 samples of 3 different class labels, and see if we can write a program that classifies the data. We can do this very easily with python if-else statements and some pandas functions.

Then, measure the _accuracy_ of your classifier using the math of "total correct" over "total samples."

The classifier should be able to:

1. Get one class label 100% correct: one of the irises is very easy to distinguish from the other 2.
2. Accurately predict the majority of the other two, with some error: the samples for the remaining class labels are a little intertwined, so you may need to _generalize_.

Here's some starter code to get you going:

```python
from sklearn import datasets, neighbors, metrics
import pandas as pd

iris = datasets.load_iris()
irisdf = pd.DataFrame(iris.data, names=iris.feature_names)
irisdf['target'] = iris.target
irisdf.plot('petal length (cm)', 'petal width (cm)', kind='scatter', c=irisdf.target)
print irisdf.plot('petal length (cm)', 'petal width (cm)', kind='scatter', c=irisdf.target)
print irisdf.describe()

# starter code
def my_classifier(row):
    if row['petal length(cm)'] < 2:
        return 0
    else:
        return 1

predictions = irisdf.apply(my_classifier, axis=1)

```

1. How simple could the if-else classifier be to still be _relatively_ accurate?
2. How complicated could this if-else classifier be to be _completely_ accurate? How many if-else statements would you need, or nested if-else statements, in order to get the classifier 100% accurate?
3. **RECALL** Which if-else classifier would work better against iris data that it hasn't seen? Why is that the case?

---

<a name="introduction-knn"></a>
## Introduction: What is K Nearest Neighbors? (5 mins)

K Nearest Neighbors (KNN) is a fairly straightforward algorithm:

1. For a given point, calculate the distance to all other points.
2. Given those distances, pick the k closest points.
3. Calculate the probability of each class label given those points
4. The original point is classified as the class label with the largest probability.

KNN uses distance as the class label assumption. if I picked an arbitrary marble from a table without looking but knew _where_ I picked it, I would use the surrounding marble colors to make my most educated guess of what color marble is in my hand.

This is a natural thing we do as people: if we're unfamiliar with something we are looking at, we'll think of other things that are similar, identify where the most traits are shared, and guess that the thing we don't know is _probably_ the same, or similar to, things we did know. Anecdotally: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

---

<a name="guided-practice-knn"></a>
## Guided Practice: KNN In Action

```python
from sklearn import datasets, neighbors, metrics
import pandas as pd

iris = datasets.load_iris()
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(iris.data[:,2:], iris.target)
print knn.predict(iris.data[:,2:])
print iris.target

print knn.score(iris.data[:,2:], iris.target)
```

Above we have the simplest implementation of KNN using sklearn, attempting to predict one of three iris types based the size of the iris. We use the default `n_neightors` of 5, which will remove most ties.

### What happens in ties?
For sklearn, in the case of ties, it will designate the class based on what it saw first in the training set.

We can also implement a _weight_, so that the total distance plays a more significant role. Try changing the `weights` argument in the above code and see how it effects the accuracy.

### What happens with high dimensionality?

In regressions, we could use L1 regularization when we have significantly more features that observations.

With KNN, we do _not_ have regularization, and a different problem: since KNN works with distance, higher dimensionality of data (more features) requires _significantly_ more samples in order to have the same predictive power. Consider it this way: with more dimensions, all points slowly start averaging out to be equally distant; this causes significant issues for KNN! Keep the feature space limited, and KNN can do well!

<a name="ind-practice-knn"></a>
## Guided Practice: Solving for K

One of the primary challenges of KNN is solving for k--how many neighbors do we use?

1. The **smallest** k we can use is 1: however, using only one neighbor will probably perform poorly.
2. The **largest** k we can use is n-1; that is, every _other_ point in the data set. But without weighting, this would always set it to the class with the largest sample size! (thankfully in this dataset, we will not see that).

Use the following starter code to test and evaluate the following questions:

1. How well does using 1 neighbor perform?
2. How well does using (most of, all) the other points as neighbors perform?
3. At what point, with cross validation, does k optimize accuracy?

Look at the grid_scores and contextualize the results a bit more with a figure using matplotlib, where the x-axis represents `k`, and the y-axis represents accuracy.

```python
from sklearn import grid_search

# some n_list! keep in mind cross validation!}
# recall: what's an effective way to create a numerical list in python?
params = {'n_neighbors': }

gs = grid_search.GridSearchCV(
    estimator=,
    param_grid=,
    cv=,
)
gs.fit(iris.data, iris.target)
gs.grid_scores_
```

---

<a name="intro-eval"></a>
## Introduction: Advanced Classification Metrics: Precision, Recall, AUC.

![confusion_matrix](https://github.com/podopie/DAT18NYC/raw/83dc789584a3349096988bbe14ffd7b87acef5e8/classes/img/confusion_matrix_metrics.png)

todo: writeup whole section

![auc](http://scikit-learn.org/stable/_images/plot_roc_001.png)

<a name="guided-practice-eval"></a>
## Guided Practice: How to decide which metric to use?

While AUC seems like a nice "golden standard" for evaluating binary classification, there are still advantages to using precision or recall! There will be instances where error in positives vs negative matches will be very important. Think about what should be evaluated more with the following examples.

1. A patient is given a drug that could save their life or kill them; At what point does the "success" rate outweigh the "failure" rate?
2. A newspaper company is targeting a marketing campaign for "at risk" users that may stop paying for the product soon. What is a retained customer worth in this case, and what is the cost of a client that was offered a deal but didn't take?
3. You build a spam classifier for your email system. What are the repercussions if the classifier classifies a spam as "fair" email? What about the other way around?

<a name="ind-practice-eval"></a>
## Independent Practice: evaluating KNN with alternative metrics

With the Titanic data, build a KNN classifier that accurately predicts who would have survived the accident.

**Learning Goals**:

1. Spend a few minutes determining which data would be most important to use in the prediction problem. Consider using a feature selection aide in sklearn.
2. Spend a few minutes thinking about which _metric_ makes the most sense to optimize. Why that metric?
3. Build a KNN model that solves for K. Explain why you picked this K, metric, and feature set in predicting survival.

Use the starter code included to get you going.

<a name="conclusion"></a>
## Conclusion (5-10 mins)

1. What are class labels? What does it mean to classify?
2. How is a classification problem different from a regression problem? How are they similar?
3. How does the KNN algorithm work?
4. What primary parameters are available for tuning a KNN estimator?
5. How do you define: accuracy, precision, recall, AUC?
6. How should you decide which metric to use in a classification problem?
