---
title: Communicating Results
duration: "02:50"
creator:
    name: Ed Podojil
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Communicating Results
DS | Lesson 10

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*

- Explain the trade-offs between the precision and recall of a model while articulating the cost of false positives vs. false negatives.
- Describe the difference between visualization for presentations vs. exploratory data analysis
- Identify the components of a concise, convincing report and how they relate to specific audiences/stakeholders

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*

- Understand results from a confusion matrix, and measure true positive rate and false positive rate
- Create and interpret results from a binary classification problem
- Know what a decision line is in logistic regression

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*

- Review materials
- Be familiar with the datasets

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening) | We Built A Model |
| 10 min  | [Introduction](#intro-confusion-matrix) | Back to the Confusion Matrix |
| 15 min  | [Introduction](#intro-precision-recall) | Precision and Recall |
| 15 min  | [Demo](#demo-tradeoff) | Understanding Tradeoff |
| 15 min  | [Guided Practice](#guided-practice-cba) | Cost Benefit Analysis |
| 15 min  | [Introduction](#intro-work) | Showing Work |
| 50 min  | [Guided Practice](#guided-practice-models) | Visualizing Models Over Variables |
| 45 min  | [Independent Practice](#ind-practice-projects) | Project Practice |
| 5 min  | [Conclusion](#conclusion) | Review and Next Steps |

---

<a name="opening"></a>
## Opening: We Built A Model (5 mins)
#### We built a model! Now what?

Congrats! You've been building models. But now there is a major stepping stone between your Jupyter notebooks, some matplotlib figures, and the inevitable PowerPoint that will be presented in front of your colleagues.

Classes so far have heavily focused on two core concepts: developing consistent practice with pandas, matplotlib, and sklearn, and interpreting metrics that help evaluate the performance of models. But what does this really mean to the end user? Imagine user responses to some of the following statements:

1. The predictive model I built has an accuracy of 80%.
2. The logistic regression was optimized with L2 regularization, so you know it's good.
3. Gender was more important than age in the predictive model because it had a larger coefficient.
4. Here's the AUC chart that shows how good the model did.

How could your stakeholders respond? How do you respond back?

Recall that in the business setting, you are often the only mathematician/statistician/engineer who can interpret what you've built. Typically it is more common now for others to be at least familiar with basic data visualizations, but the expectation is there will be a lot of "hand holding," especially if your team has _never_ worked with data scientists before.

We'll focus the presentation details here around "simpler" problems (binary classification), but the logic and ideas apply to other data problems, like regressions. Before moving on to ideal ways to propose and showcase your work, let's review the some of the knowledge we've developed about classification metrics, append some more, and relate it back to the business explanation.

<a href='#review-confusion-matrix'></a>
## Review: Back to the Confusion Matrix

Let's review the confusion matrix:

![](assets/images/confusion_matrix.png)

Confusion matrices, for a binary classification problem, allow for the interpretation of correct and incorrect predictions for _each class label_. Remember, the confusion matrix is the beginning to the majority of classification metrics, and gives our predictions deeper meaning beyond an accuracy score.

**Recall** How do we calculate the following metrics?

1. Accuracy
2. True Positive Rate
3. False Positive Rate

<a href='#intro-precision-recall'></a>
## Intro: Precision and Recall

![](assets/images/precision-recall-scatter.png)

Our previous metrics primarily were designed for less biased data problems: we could be interested in both outcomes, so it was important to generalize our approach. Precision and Recall, additional metrics built off the confusion matrix, focus instead on _information retrieval_, particularly when one class label is more interesting than another. With _precision_, we're interested in producing a high amount of relevancy instead of irrelevancy; with _recall_, we're interesting in seeing how a model could return relevant data (literally, can the model _recall_ what a class label looked like).

**Recall** (pun not intended): If the metric "recall" has a goal to identify as many relevant values of a class correctly, which other metric do we know with the same calculation? (Answer: TPR! Same calculation!)

#### Breaking It Down and Math

![](assets/images/confusion_matrix_recall.png)

Truth be told, True Positive Rate and Recall are one in the same: it is the calculation of true positives over the count of all positives. Another term that is used is _sensitivity_, if looking at labeled AUC figures. These terms all have the same calculation: the count of predicted true positives over the total count of that class label. As in, imagine predicting a marble color either green or red. There are 10 of each.

If the model identifies 8 of the green marbles as green, the recall, or sensitivity, is .8. However, this says nothing about the number of _red_ marbles also identified as green.

![](assets/images/confusion_matrix_precision.png)

Precision, or the _positive predicted value_, is calculated as the count of predicted true positives over the count of all predicted to be positive. Precision focuses on relevancy.

Using the same example: if a model predicts 8 of the green marbles as green, then precision would be 1, because all marbles predicted as green were in fact green. The precision of red marbles (assuming all red marbles were correct, and 2 green were predicted as red) would be roughly 0.833: 10 / (10 + 2)

![](assets/images/precision-recall-scatter.png)

**Knowledge check**: What would be the precision and recall for the following confusion matrix ("green" being "true")?

             | predicted_green | predicted_not_green
-------------|-----------------|--------------------
is_green     | 13              | 7
is_not_green | 8               | 12


The key difference between the two is the attribution, and value, of an error: should our model be more picky in avoiding false positives (precision), or should it be more picky in false negatives (recall)? The answer will need to be determined by your data problem at hand.

<a href='#demo-tradeoff'></a>
## Demo: Understanding Tradeoff

Let's consider the following data problem: we are given a data set in order to predict or identify traits for typically late flights.

Optimizing toward precision, we could assume that every flight will be delayed. The trade off, which would be a lower recall, would be that this could create even further delays, missed flights, etc.

Optimizing toward recall, we would be specifically looking to identify the flights that will be late, the trade-off here would be lower precision (we might miss flights that would be delayed, thus causing other strain in the system).

Below includes a sample plot that shows how precision and recall are related for a model used to predict late survivors:

![](assets/images/delays-precision-recall.png)

This plot is based on choosing decision line thresholds, much like the AUC figure from the previous class. In terms of the delays model, this would be like moving the decision line for lateness from 0.01 up to 0.99, and then calculating the precision and recall at each decision.

There's a few interesting nuggets from interpreting this, compared to the benchmark (blue)

1. At a lower recall (below .2), there is a noticeable lower precision in the model.
2. Beyond .2 recall, the model outperforms the benchmark.

Depending on optimizing for recall or precision, this plot will help decide on that threshold.

<a href='#guided-practice-cba'></a>
## Guided Practice: Cost Benefit Analysis

One other tool that complements the confusion matrix when you can attach a _value_ to correctly and incorrectly predicted data is cost benefit analysis. Like the Precision-Recall trade off, there is a balancing point to the _probabilities_ of a given position in the confusion matrix, and the _cost_ or _benefit_ to that position. This approach allows you to not just add a weighting system to your confusion matrix, but also easily allows you as a data scientist to speak the language of your business stakeholders (usually, in dollars!).

Consider this marketing problem:

As a data scientist working on marketing spend, you've build a model that reduces user churn--the number of users who decide to stop paying for a product--through a marketing campaign. Your model generates a confusion matrix with the following probabilities (these probabilities are calculated as the value in that position over the sum of the sample):

    | TP: 0.2 | FP: 0.2 |
    ---------------------
    | FN: 0.1 | TN: 0.5 |

In this case:
    * The _benefit_ of a true positive is the retention of a user ($10 for the month)
    * The _cost_ of a false positive is the spend of the campaign per user ($0.05)
    * The _cost_ of a false negative (someone who could have retained if sent the campaign) is, effectively, 0 (we didn't send it... but we certainly didn't benefit!)
    * The _benefit_ of a true negative is 0: No spend on users who would have never retained.

To calculate Cost-Benefit, we'll use this following function:

`(P(TP) * B(TP)) + (P(TN) * B(TN)) + (P(FP) * C(FP)) + (C(FN) * C(FN))`

which for our marketing problem, comes out to this:

`(.2 * 10) + (.5 * 0) - (.2 * .05) - (.1 * 0)`

or $1.99 per user targeted.

#### Follow up questions:

Think about precision, recall, and cost benefit analysis with the above problem to answer the following questions:

1. How would you rephrase the business problem if your model was optimizing toward _precision_? i.e., How might the model behave differently, and what effect would if have?
2. How would you rephrase the business problem if your model was optimizing toward _recall_?
3. What would the most ideal model look like in this case?

<a href='#intro-work'></a>
## Intro: Showing Work

We've spent an inordinate amount of time with our data throughout data exploration and building a reasonable model that performs well. However, if we look back at our visuals, they are likely:

* **statistically heavy**: you've built about 1,000 histograms, but rarely do non data savvy people understand what a histogram represents.
* **overtly complicated**: pandas' `scatter_matrix()` is a useful function to quickly explore data, but it's just one example of visuals that shouldn't be shown to a project stakeholder because it's just too much to read and understand at a first pass.
* **poorly labeled**: it's very common during EDA that you're just quickly flowing through figures, and since you built them in code, you didn't bother labeling them (why bother if you're saying what x and y is in your code?).

Instead, we'll want to focus on the following ideals:

* **Simplistic**: At most, you'll want figures that either explain a variable on its own (explaining the sample or population), or that variable with the target (how that variable explains the target). If your model used a data transformation (like the natural log of a variable), visualize the original data, as log is just an extra thing to explain.
* **Tells a clear story/easily interpretable**: Any stakeholder looking at the figure should be seeing the exact same thing you're seeing. A good test for this: share the visual with others less familiar with the data, and see if they came to same conclusion as yours... and they could do it quickly. It'll help if:
* **Everything is labeled that should be**: take the extra time to clearly label your axis, title the plot, and double check your scales, especially if the figures should be comparable.

These are built on some of the following questions you should be asking yourself when building visuals for another audience:

* **Who**: Who is my target audience for this visual? Who might they share this work with after seeing it?
* **What**: What do they already know about my work on this project? What is the background in working with data? What do they want to know?
* **How**: How does this project effect this audience? How might it be used practically? How might they interpret, or misinterpret, the data?

You're encouraged to explore in more detail the various attributes of plotting, as the rest of today's class will focus less on these concepts and more on visualizing your model.

[http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html](Pandas plotting)

[http://matplotlib.org/users/text_intro.html](Text with matplotlib)

[https://github.com/WeatherGod/AnatomyOfMatplotlib](Anatomy of Matplotlib)

#### Visualizing Models Over Variables

One effective way to explain your model over particular variables is to plot the predicted variables against the most explanatory variables. For example, with logistic regression, plotting the probability of a class against a variable can help explain the range of effect on the model.

Let's use flight delay data as an example:

```python
# read in the file and generate a quick model (assume we've done the data exploration already)

import pandas as pd
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

df = pd.read_csv('../../assets/dataset/flight_delays.csv')

df = df.join(pd.get_dummies(df['DAY_OF_WEEK'], prefix='dow'))
df = df[df.DEP_DEL15.notnull()].copy()

model = lm.LogisticRegression()
features = ['dow_1', 'dow_2', 'dow_3', 'dow_4', 'dow_5', 'dow_6']
model.fit(df[features + ['CRS_DEP_TIME']], df['DEP_DEL15'])

df['probability'] = model.predict_proba(df[features + ['CRS_DEP_TIME']]).T[1]

ax = plt.subplot(111)
colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown']
for e, c in enumerate(colors):
    df[df[features[e]] == 1].plot(x='CRS_DEP_TIME', y='probability', kind='scatter', color = c, ax=ax)

ax.set(title='Probability of Delay\n Based on Day of Week and Time of Day')
```

![Plotting Probabilities](assets/images/plotting_proba.png)

A visual like this can help showcase the range of effect on delays from the both the day of week and the time of day: given this model, some days are more likely to have delays than others, and likelihood of a delay increases as the day goes on.

### Try it out

1. Adjust the model to predict using airlines instead of day of week, and time, then plot its effect on CRS_DEP_TIME=1.
2. Try plotting the inverse: pick either model and plot the effect on CRS_DEP_TIME=0.

#### Visualizing Performance Against Baseline

Another approach of visualization that, while slightly more complicated in detail, is the effect of your model against a baseline, or even better, previous models. Compared to the original audience, plots like this will also be more useful talking to your peers: other data scientists or analysts who are familiar with your project and interested in the progress you've made. For classification, we've practice plotting AUC and precision-recall plots. Consider the premise of each:

* For AUC plots, you want to explain and represent "accuracy" as having the largest area under the curve. Good models will be high to the left.
* for precision-recall plots, it'll depend on the _cost_ requirements: either a model with good recall at the cost of precision, or visa versa.

The next step: you're now comparing multiple models. So, breaking this down again:

* For AUC plots, you are interested in which model has the _largest_ area under the curve
* for precision-recall plots, based on the cost requirement, you are looking for which model has the best precision given the same recall, or the best recall given the same precision.

Below, we've plotted several models for AUC: a dummy model, and adding features into the regression.

```python
model0 = dummy.DummyClassifier()
model0.fit(df[features[1:-1]], df.DEP_DEL15)
df['probability_0'] = model0.predict_proba(df[features[1:-1]]).T[1]


model = lm.LogisticRegression()
model.fit(df[features[1:-1]], df.DEP_DEL15)
df['probability_1'] = model.predict_proba(df[features[1:-1]]).T[1]

ax = plt.subplot(111)
vals = metrics.roc_curve(df.DEP_DEL15, df.probability_0)
ax.plot(vals[0], vals[1])
vals = metrics.roc_curve(df.DEP_DEL15, df.probability_1)
ax.plot(vals[0], vals[1])

ax.set(title='Area Under the Curve for prediction delayed=1', ylabel='TRP', xlabel='FRP', xlim=(0, 1), ylim=(0, 1))
```

![](assets/images/auc_curve.png)

This plot showcases:

1. The model using data outperforms a baseline dummy model.
2. By adding other features, there's some give and take with probability as the model gets more complicated. Try adding additional features (such as time of day) and compare models.

### Try it out

1. In a similar approach, use the sklearn precision_recall_curve function to enable you to plot the precision-recall curve of the four models from above.
    * Keep in mind precision in the first array returned from the function, but in the plot, is the y-axis.
2. Explain what is occurring when the recall is below 0.2.
3. Based on this performance, is there a clear winner at different thresholds?

**bonus** Redo both the AUC and precision-recall curves but using models that have been cross validated using kfold. How do these new figures change your expectations on performance?

<a href='#ind-practice-projects'></a>
## Independent Practice: Project Practice

Using models built from the flight data problem earlier in class, work through the same problems. Your data and models should already be accessible. Your goals:

1. There are _many_ ways to manipulate this data set. Consider what is a proper "categorical" variable, and keep _only_ what is significant. You will easily have 20+ variables. Aim to have at least three visuals that clearly explain the relationship of variables you've used against the predictive survival value.
2. Generate the AUC or precision-recall curve (based on which you think makes more sense), and have a statement that defines, compared to a baseline, how your model performs, and its caveats. For example: "My model on average performs at x rate, but the features under-perform and explain less of the data at these thresholds."

Consider this as practice to approaching your own project, as the steps to presentation should be relatively similar.

<a href='#conclusion'></a>
## Conclusion: Review and Next Steps

1. What do precision and recall mean? How are they similar and different to True Positive Rate and false Positive Rate?
2. How does cost benefit analysis play a role in building models?
3. What are at least two very important details to consider when creating visuals for a project's stakeholders?
4. Why would an AUC plot work well for a data science audience, but not necessarily so for the business stakeholders of a project? What could be a more effective visualization to showcase for that group?
