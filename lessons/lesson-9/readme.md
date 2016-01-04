---
title: Logistic Regression
duration: 3:00
creator:
    name: Ed Podojil
    city: NYC
    dataset: tbd
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Evaluating Model Fit
Week # | Lesson #

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Build a Logistic regression classification model using the sci-kit learn library
- Describe the sigmoid function, odds, and odds ratios as well as how they relate to logistic regression
- Evaluate a model using metrics, such as: classification accuracy/error, confusion matrix, ROC / AOC curves, and loss functions

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Implement a linear model (LinearRegression) with sklearn
- Understand what is a coefficient
- Recall metrics accuracy and misclassification
- Recall the differences between L1 and L2 regularization

### INSTRUCTOR PREP
*Before this lesson, instructors will have to:*
- review materials
- be familiar with the datasets

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening) | Discuss lesson objectives, Reviewing Probability |
| 10-15 mins | [Introduction](#introduction) | Intro to Logistic Regression |
| 10-15 mins | [Demo](#demo)  |  |
| 20-25 mins | [Guided Practice](#guided-practice)  | |
| 10-15 mins | [Introduction](#introduction) | |
| 10-15 mins | [Demo](#demo)  |  |
| 20-25 mins | [Guided Practice](#guided-practice) | |
| 10-15 mins | [Introduction](#introduction-eval) | Intro to additional classification metrics and the confusion matrix |
| 10-15 mins | [Guided Practice](#guided-practice-eval) | Determining proper metrics given classification problems |
| 30-35 mins | [Independent Practice](#ind-practice-eval)  | Optimizing a logistic regression using new metrics  |
| 5-10 mins | [Conclusion](#conclusion) | Wrapup |

# todo, logistic regression section

<a name="intro-eval"></a>
## Introduction: Advanced Classification Metrics: Precision, Recall, AUC.

Accuracy is only one of several metrics used when solving for a classification problem. It is best defined as `total predicted correct / total data set`. But accuracy alone isn't always usable: for example, if we know a prediction is 75% accurate, accuracy does not provide _any_ insight into why the 25% was wrong: was it wrong equally across all class labels? Did it just guess one class label for all predictions and 25% of the data was just the other label? It's important to look at other metrics to fully understand the problem.

![confusion_matrix](https://github.com/podopie/DAT18NYC/raw/83dc789584a3349096988bbe14ffd7b87acef5e8/classes/img/confusion_matrix_metrics.png)

We can split up the accuracy of each label by using _true positive rate_ and _false positive rate_.

**True Positive Rate (TPR)**: Out of all of the target class label, how many were accurately predicted to belong to that class?

**False Positive Rate (TPR)**: The inverse of TPR: out of all not belonging to a class label, how many were predicted as the target class label?

A very good classifier would have a true positive rate approaching 1, and a false positive rate approaching 0. In a binary problem (say, predicting if someone smokes or not), It would accurately predict all of the smokers as smokers, and not predict any of the nonsmokers as smokers.

Logically, we still like single numbers for optimizing, so we can use a metric called Area Under the Curve (AUC), which summarizes the impact of TPR and FPR in once single value. This is also called the Receiver Operating Characteristic (ROC). ROC/AUC is a measure of area under a curve that is described by the TPR and FPR.

![auc](http://scikit-learn.org/stable/_images/plot_roc_001.png)

Using the logic of TPR and FPR above:

1. If we have a TPR of 1 (all positives are marked positive) and an FPR of 0 (all negatives are not marked positive), we'd have an AUC of 1. This means everything was accurately predicted.
2. If we have a TPR of 0 (all positives are not marked positive) and an FPR of 0 (all negatives are marked positive), we'd have an AUC of 0. This means nothing was predicted accurately.
3. An AUC of .5 would suggest, somewhat, randomness, and is an excellent benchmark to use for prediction (is my AUC above .5?)

Keep in mind that sklearn has all of these metrics on [one handy page](http://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics).

<a name="guided-practice-eval"></a>
## Guided Practice: How to decide which metric to use?

While AUC seems like a nice "golden standard" for evaluating binary classification, it could be _further_ improved, dependent on your classification problem. There will be instances where error in positives vs negative matches will be very important.

For each of the following examples:

* Write a confusion matrix (like above: true positive, false positive, true negative, false negative) and decide what each square represents for the example
* Define the _benefit_ of a true positive and true negative
* Define the _cost_ of a false positive and false negative
* Determine: at what point does the cost of a failure outweigh the benefit of a success? This would help you decide how to optimize TPR, FPR, and AUC.

1. A test is developed for determining if a patient has cancer or not
2. A newspaper company is targeting a marketing campaign for "at risk" users that may stop paying for the product soon.
3. You build a spam classifier for your email system.

<a name="ind-practice-eval"></a>
## Independent Practice: evaluating KNN with alternative metrics

[Kaggle's common online exercise](https://www.kaggle.com/c/titanic) is exploring survival data from the Titanic.

**Learning Goals**:

1. Spend a few minutes determining which data would be most important to use in the prediction problem. You may need to create new features based on the data available. Consider using a feature selection aide in sklearn. But a worst case scenario; identify one or two strong features that would be useful to include in the model.
2. Spend 1-2 minutes considering which _metric_ makes the most sense to optimize. Accuracy? FPR or TPR? AUC? Given the business problem (understanding survival rate aboard the Titanic), why should you use this metric?
3. Build a KNN model that solves for K. Be prepared to explain why you picked this K, metric, and feature set in predicting survival using the tools necessary (such as a fit chart).

Use the starter code included to get you going.