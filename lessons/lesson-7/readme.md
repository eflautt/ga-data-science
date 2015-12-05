---
title: Evaluating Model Fit
duration: 3:00
creator:
    name: Ed Podojil
    city: NYC
    dataset: citibike ridership and weather data
---

# Evaluating Model Fit

### LEARNING OBJECTIVES
*After this lesson, students will be able to:*

- Define regularization, bias, and error metrics for regression problems
- Evaluate model fit by using loss functions including mean absolute error, mean squared error, root mean squared error
- Select regression methods based on fit and complexity

### STUDENT PRE-WORK
*Before this lesson, students should already be able to:*

- Understand goodness of fit (r-squared)
- Measure statistical significance of features
- Recall what a _residual_ is
- Implement an sklearn estimator to predict a target variable

### INSTRUCTOR PREP
*Before this lesson, instructors will have to:*

- review materials
- be familiar with the datasets

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | a  |
| 10-15 mins  | [Introduction](#introduction-cv)  | Reviewing concepts of error for regression models and cross validation  |
| 10-15 mins  | [Demo](#demo-cv)  | demo using cross validation |
| 20-25 mins  | [Guided Practice](#guided-practice-cv)  | Cross Validation in sklearn  |
| 10-15 mins  | [Introduction](#introduction-reg)   | what are lasso and ridge doing differently? |
| 10-15 mins  | [Demo](#demo-reg)  | Zeroing coefficients using alpha |
| 20-25 mins  | [Guided Practice](#guided-practice-reg)  | Solving for alpha using a grid search  |
| 10-15 mins  | [Introduction](#introduction-sgd)  | Using Gradient Descent to minimize error |
| 10-15 mins  | [Demo](#demo-sgd)  | Application of Stochastic Gradient Descent |
| 30-35 mins  | [Independent Practice](#ind-practice)  | Application of above techniques to create a generalized and improved model of the bikeshare casual riders data  |
| 5-10 mins  | [Conclusion](#conclusion)  | review topics |

<a name="opening"></a>
## Opening (5 mins)

<a name="introduction-cv"></a>
## Introduction: Linear Models and Error (15 mins)

#### Recalling: What's residual error?

In the last class, we reviewed one expectation of linear models: that the residual error be normal (with hopefully the median being close to 0!).

`y = betas * x + alpha + epsilon` <- epsilon == error

![](residual error histogram)

Obviously, residual error for each value, while effective at understanding where your error lies, is not an effective summary metric. Instead, we'll use some mean of the error as a scaler interpretation to the error in the model.

#### Mean Squared Error (MSE)

For squared error, we will:

1. Calculate the difference between each target y and the model's predicted value y hat (this is how we determine the _residual_)
2. Square each residual.
3. Take the mean of the squared residual error.

sklearn's metrics module includes a mean_squared_error function. Sklearn's metrics module will be home to evaluating the performance of majority of our models:

```python
from sklearn import metrics
metrics.mean_squared_error(y, model.predict(X))
```

#### How do we minimize error?

The regression we've been using in class is called "ordinary least squares," which literally means given a matrix X, solve for the _least_ amount of squared error for y. However, this approach assumes that the sample X is representative of the population; that is, the sample is _unbiased_. For example, let's compare these two random models:

```python
import numpy as np
import pandas as pd
from sklearn import linear_model

df = pd.DataFrame({'x': range(100), 'y': range(100)})
biased_df  = df.copy()
biased_df.loc[:20, 'x'] = 1
biased_df.loc[:20, 'y'] = 1

def append_jitter(series):
    jitter = np.random.random_sample(size=100)
    return series + jitter

df['x'] = append_jitter(df.x)
df['y'] = append_jitter(df.y)

biased_df['x'] = append_jitter(biased_df.x)
biased_df['y'] = append_jitter(biased_df.y)

## fit
lm = linear_model.LinearRegression().fit(df[['x']], df['y'])
print metrics.mean_squared_error(df['y'], lm.predict(df[['x']]))

## biased fit
lm = linear_model.LinearRegression().fit(biased_df[['x']], biased_df['y'])
print metrics.mean_squared_error(df['y'], lm.predict(df[['x']]))
```

In the biased sample, one member of the sample is oversampled, which introduces error. This would be similar to building a model that predicts hourly guest bike share riders, but the prediction is built off a biased data set; perhaps it only looks at one neighborhood, or it only uses data from the afternoon. As data scientists, it is in our best interest to pragmatically account for biased error for _generalized_ error; that is, we'd prefer if the error was distributed more evenly across the model.

<a name="demo-cv"></a>
## Demo: Cross Validation (20 minutes)

One approach data scientists use to account for bias is cross validation. The basic idea of cross validation is to generate several models based on different cross sections of the data, measure performance of each, and then take the mean performance.

One of the most common cross validation techniques is k-fold: split the data into _k_ groups, _train_ the data on all segments except one, and then _test_ the performance on the remaining set. If k equals five, then that means we generate five different models.

What happens to mean squared error if we use 5 fold validation to _generalize_ the error?

```python
from sklearn import cross_validation
wd = '../../datasets/'
bikeshare = pd.read_csv(wd + 'bikeshare/bikeshare.csv')
weather = pd.get_dummies(bikeshare.weathersit, prefix='weather')
modeldata = bikeshare[['temp', 'hum']].join(weather[['weather_1', 'weather_2', 'weather_3']])
y = bikeshare.casual

kf = cross_validation.KFold(len(modeldata), n_folds=5, shuffle=True)
scores = []
for train_index, test_index in kf:
    lm = linear_model.LinearRegression().fit(modeldata.iloc[train_index], y.iloc[train_index])
    scores.append(metrics.mean_squared_error(y.iloc[test_index], lm.predict(modeldata.iloc[test_index])))

print np.mean(scores)

# this score will be lower, but we're trading off bias error for generalized error
lm = linear_model.LinearRegression().fit(modeldata, y)
print metrics.mean_squared_error(y, lm.predict(modeldata))
```

While it's apparent that the cross validated approach here generated more error, which of the two approaches do we think would predict more accurately on **new**data: the single model, or the cross validated, average one?

<a name="guided-practice-cv"></a>
## Guided Practice: cross validation with linear regression (20 mins)

Apply the following code through a loop of numbers 2 to 50 and find answers to these questions: `range(2, 51, 2)`

1. What does shuffle=True do?
2. When shuffle=False, at what point does cross validation no longer seem to help the model?

```python
kf = cross_validation.KFold(len(modeldata), n_folds=i)
scores = []
for train_index, test_index in kf:
    lm = linear_model.LinearRegression().fit(modeldata.iloc[train_index], y.iloc[train_index])
    scores.append(metrics.mean_squared_error(y.iloc[test_index], lm.predict(modeldata.iloc[test_index])))
```

<a name="introduction-reg"></a>
## Regularization and Cross Validation (15 mins)

#### What's Regularization? Why do we use it?

_Regularization_ is an additive approach to protect models against _overfitting_, or being potentially biased and overconfident. In regressions, regularization becomes an additional weight to coefficients, which is either added (L1) or squared then added (L2). These are also known as Lasso and Ridge Regressions, which we toyed with as practice last class. As good practice, we should use Lasso (L1) when we have a higher number of features (k) than we have observations (n), and use Ridge (L2) in about all other cases.

#### Where Regularization Makes Sense

Consider this: what happens to MSE if we just directly use a Lasso or Ridge Regression?

```python
lm = linear_model.LinearRegression().fit(modeldata, y)
print metrics.mean_squared_error(y, lm.predict(modeldata))
lm = linear_model.Lasso().fit(modeldata, y)
print metrics.mean_squared_error(y, lm.predict(modeldata))
lm = linear_model.Ridge().fit(modeldata, y)
print metrics.mean_squared_error(y, lm.predict(modeldata))
```

```bash
1672.58110765 # OLS
1725.41581608 # L1
1672.60490113 # L2
```

In this example; L1 (lasso) massively increases our error (likely from not fitting to the L1 criteria), and L2 also increases the error. What gives?

Regularization, like any important optimization function, will be more important during _cross validation_. In particular, we will optimize the regularization weight parameter _through_ cross validation.

<a name="demo-reg"></a>
## Demo: Understanding Regularization Effects (15 mins)

Let's test a variety of alpha weights for Ridge Regression on the bikeshare data (why are we using Ridge Regression?).

```python
alphas = np.logspace(-10, 10, 21)
for a in alphas:
    print 'Alpha:', a
    lm = linear_model.Ridge(alpha=a)
    lm.fit(modeldata, y)
    print lm.coef_
    print metrics.mean_squared_error(y, lm.predict(modeldata))
```

1. What happens to the weights of the coefficients as alpha increases?
2. What happens to the error as alpha increases

**Bonus** Try plotting!

#### Make this easier! Introducing: Grid Search

We can tell sklearn to try all of these alphas in less code using a _grid search_. Grid search sounds exactly like what it means: telling the computer to exhaustively search through all options to find the best solution.

```python
from sklearn import grid_search
gs = grid_search.GridSearchCV(
    estimator=linear_model.Ridge(),
    param_grid={'alpha': alphas},
    scoring='mean_squared_error')

gs.fit(modeldata, y)

print -gs.best_score_
print gs.best_estimator_
print gs.grid_scores_
```

<a name="guided-practice-reg"></a>
## Guided Practice: grid search cv, solving for alpha (25 mins)

Use similar code from above, but now:

1. Introduce cross validation into the grid search. This is accessible from the `cv` argument.
2. Addto the param_grid dictionary fit_intercept = True and False.
3. Re-investigate the best score, best estimator, and grid scores attributes as a result of the grid search.

<a name="introduction-gds"></a>
## Minimizing Loss Through Gradient Descent (15 mins)

One last approach to minimizing error is Gradient Descent. The concept behind Gradient Descent could be explained in the following steps:

1. A random linear solution is provided as a starting point (usually a "flat" line or solution)
2. The solver then attempts to find a next step: we take a step in any direction and measure each performance.
3. If the solver finds a better solution (optimizing toward a metric such as mean squared error), this is the new starting point.
4. Repeat these steps until the performance is optimized and no "next steps" perform better. The size of the steps will shrink over time.

Gradient Descent is very similar to traversal or dynamic programming, programming concepts that by design work through iteration.

#### Stepping away from the data and getting the concept right

Walk through this code, which suggests a similar pattern to how gradient descent behaves:

```python
num_to_approach, start, steps, optimized = 6.2, 0., [-1, 1], False
while not optimized:
    current_distance = num_to_approach - start
    got_better = False
    next_steps = [start + i for i in steps]
    for n in next_steps:
        distance = np.abs(num_to_approach - n)
        if distance < current_distance:
            got_better = True
            print distance, 'is better than', current_distance
            current_distance = distance
            start = n
    if got_better:
        print 'found better solution! using', current_distance
        a += 1
    else:
        optimized = True
        print start, 'is closest to', num_to_approach

```

1. What is the code doing?
2. What could go wrong?

One particular challenge with gradient descent is that it could potentially solve for a _local_ minimum of error, instead of a _global_ minimum.

##### an anecdote

You can think of this like trying to get directions to grandmother's house (over the river and through the woods). Gradient Descent might accidentally say "I got close to her house, but can't get over the river, so this is the best I can do," thus minimizing for a _local_ minimum distance; however the _global_ minimum would have been to step away from the river first and find the bridge, then go over the river and actually get much closer to the house.

<a name="demo-gds"></a>
## Demo: Application of Gradient Descent (15 mins)

Gradient Descent works best when:

1. We are working with a large data set. Because smaller sets are more prone to error, and proneness to error could be steps in the wrong direction.
2. data is severely cleaned up and normalized (such as the bikeshare data set).

Gradient descent's advantages are huge: with a very large data set, OLS will take significantly longer to solve (computationally). We may not notice it as much on the smaller data sets in class, but in a live system with millions of data points, gradient descent is vastly superior. You'll particularly see this with the regressors `partial_fit()` function.

Like Ridge and Lasso regression, we can penalize (add in weights) to the gradient descent solver.

```python
lm = linear_model.SGDRegressor()
lm.fit(modeldata, y)
print lm.score(modeldata, y)
print metrics.mean_squared_error(y, lm.predict(modeldata))
```

Untuned, how well did gradient descent perform compared to OLS?

<a name="ind-practice"></a>
## On your Own (30 mins)

Explore the Gradient Descent regressor object, and build a grid search using the stochastic gradient descent estimator for the bikeshare data set. Continue with either the model you evaluated last class or the simpler one from today. In particular:

1. Explore the penalties of L2 and elastic net (Which is a combination of l1 and l2).
2. Solve to optimize alpha.
3. Ensure you are using kfold cross validation with the grid search.

<a name="conclusion"></a>
## Conclusion (5 mins)



