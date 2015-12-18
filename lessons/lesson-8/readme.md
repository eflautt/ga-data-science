---
title: Evaluating Model Fit
duration: 3:00
creator:
    name: Ed Podojil
    city: NYC
    dataset: iris dataset
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Evaluating Model Fit
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

todo

---

<a name="introduction-class"></a>
## Introduction: What is Classification (5 mins)

todo

<a name="independent-practice-class"></a>
## Independent Practice: Build a classifier! (20 mins)

```python
from sklearn import datasets, neighbors, metrics
import pandas as pd

iris = datasets.load_iris()
print iris.data
print iris.targets
```

On a small dataset, we can solve for an "if-else" classifier: using some basic traits of the iris data set, build a classifier! Measure it's accuracy as total correct vs total rows (150).

1. How simple could the if-else classifier be to still be _relatively_ accurate?
2. How complicated could this if-else classifier be to be _completely_ accurate?
3. **RECALL** Which if-else classifier would work better against iris data that it hasn't seen? Why is that the case?

```python
irisdf = pd.DataFrame(iris.data, names=iris.feature_names)
irisdf['target'] = iris.target
irisdf.plot('petal length (cm)', 'petal width (cm)', kind='scatter', c=irisdf.target)
print irisdf.plot('petal length (cm)', 'petal width (cm)', kind='scatter', c=irisdf.target)
print irisdf.describe()
```

```python
# starter code
def my_classifier(row):
    if row['petal length(cm)'] < 2:
        return 0
    else:
        return 1

predictions = irisdf.apply(my_classifier, axis=1)
```

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
## Independent Practice: Solving for K

One of the primary challenges of KNN is solving for k--how many neighbors do we use?

1. The **smallest** k we can use is 1: however, using only one neighbor will probably perform poorly.
2. The **largest** k we can use is n-1; that is, every _other_ point in the data set. But without weighting, this would always set it to the class with the largest sample size! (thankfully in this dataset, we will not see that).

Use the following starter code to test and evaluate the following questions:

1. How well does using 1 neighbor perform?
2. How well does using (most of, all) the other points as neighbors perform?
3. At what point, with cross validation, does k optimize accuracy?

```python
from sklearn import grid_search

params = {'n_neighbors': }# some n_list! keep in mind cross validation!}
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
