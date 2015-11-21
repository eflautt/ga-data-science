---
title: Intro to Regression Analysis
duration: 2:30
creator:
    name: Ed Podojil
    city: NYC
    dataset: animal weights and sleeping habit
    dataset: citibike ridership and weather data
---

# Building Models with ActiveRecord & Migrations

### Objectives
*After this lesson, students will be able to:*

- Define data modeling and linear regression
- Differentiate between categorical and continuous variables
- Build a linear regression model using a dataset that meets the linearity assumption using the sci-kit learn library

### Preparation
*Before this lesson, students should already be able to:*

- Effectively show correlations between an independent variable `x` and a dependent variable `y`
- Be familiar with the `get_dummies` function in pandas
- Understand the difference between vectors, matrices, Series, and DataFrames
- Understand the concepts of outliers and distance.
- Be able to interpret p values and confidence intervals

### Instructor Preparation
*Before this lesson, instructors will have to:*

- review materials
- be familiar with the datasets

## Section Title (I do)

#### It starts with a simple correlation

A linear regression is an explanation of a continuous variable given a series of independent variables. In it's simplest form, a linear regression would remind us of a basic algebraic function: a line of best fit:

y = mx + b

That is:

_Given some value __x__, its power in explanation __m__, and a starting point __b__, explain the value __y__._

However, the power of a linear regression is that we can use linear algebra to explain _multiple_ x's together in order to explain y:

y = betas * X + alpha (+ error)

Our terminology now being:

_Given a matrix __X__, their relative coefficients __beta__, and a y-intercept __alpha__, explain a dependent vector, __y__._

A linear regression succeeds best when:

* The data is normally distributed (both xs and y!)
* The Xs significantly explain y (have low p-values)
* The Xs are independent of eachother (low multicollinearity)
* The resulting values passes linear assumptions

#### Regressions work best when everything is normal

When using linear regressions, data works best as normal distributions. Linear regressions have linear solutions--we want this linear solution to explain the majority, "normal" part of our data; not outliers!

For example, let's look at explaining the relationship between an animal's body weight, and their brain weight.

```python
# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# read in the mammal dataset, and drop missing data.
mammals = pd.read_csv('../data/msleep.csv')
mammals = mammals[mammals.brainwt.notnull()].copy()
# create a matplotlib figure
plt.figure()
# generate a scatterplot inside the figure
plt.plot(mammals.bodywt, mammals.brainwt, '.')
# show the plot
plt.show()
```

In the plot, it's apparent that there is a relationship between the two values, but as it stands, it's not a linear solution. Using the seaborn library, we can plot the linear regression fit with these two variables:

```python
# generate a plot of a single variable linear model of brain weight given body weight.
sns.lmplot('bodywt', 'brainwt', mammals)
```

Notice:

1. The `lmplot()` function returns a straight line. That is because it is a linear solution.
2. The linear solution does explain a portion of the data well, but because both bodywt and brainwt are log-log distributions, outliers effect the weight of the solution poorly. We can see this from the wide and inconsistent confidence intervals that seaborn's lmplot generates.

Because both values are a log-log distribution, some math properties allow us to transform them into normal distributions. Then, we can solve for the linear regression!

```python
# create a new data set that converts all numeric variables into log10
log_mammals = mammals[['bodywt', 'brainwt']].apply(np.log10)

sns.lmplot('bodywt', 'brainwt', log_mammals)
```

Does this explain the animal's brain weight better or worse than the original data?

Even though we changed the way the data was shaped, this is still a _linear_ result: it's just linear in the log10 of the data, instead of in the data's natural state.

#### Single Regression Analysis

#### Significance is key

With the sklearn library, we can generate an sklearn model object and explore important evaluation values for linear regression.

```python
# import sklearn
from sklearn import feature_selection, linear_model

def get_linear_model_metrics(X, y, algo):
    # get the pvalue of X given y
    pvals = feature_selection.f_regression(X, y)[1]
    # start with an empty linear regression object
    # .fit() runs the linear regression function on X and y
    algo.fit(X,y)

    # print the necessary values
    print 'P Values:', pvals
    print 'Coefficients:', algo.coef_
    print 'y-intercept:', algo.intercept_
    print 'R-Squared:', algo.score(X,y)
    # keep the model
    return algo

X = mammals[['bodywt']]
y = mammals['brainwt']
get_linear_model_metrics(X, y, linear_model.LinearRegression())

```

```bash
P Values: [  9.15540205e-26]
Coefficients: [ 0.00096395]
y-intercept: 0.0859173102936
R-Squared: 0.871949198087
```

Our output tells us:

* The relationship between bodywt and brainwt isn't random (p value approaching 0)
* The model explains, roughly, 87% of the variance of the dataset (the largest errors being in the large brain and body sizes)
* With this current model, brainwt is _roughly_ bodywt * 0.00096395

#### Evaluating Fit, Evaluating Sense

Although we know there is a _better_ solution to the model, we should evaluate some other sense things first. For example, given this model, what is an animal's brainwt if their bodywt is 0?

__0.0859...__

What would we expect an animal's brainwt to be if their bodywt is 0?

With linear modeling we call this part of the __linear assumption__. Consider it a test to the model. If an animal's body weights nothing, we expect their brain to be nonexistent. That given, we can improve the model by telling sklearn's LinearRegression object we do not want to fit a y intercept.

```python
get_linear_model_metrics(X, y, linear_model.LinearRegression(fit_intercept=False))
```

```bash
P Values: [  9.15540205e-26]
Coefficients: [ 0.00098291]
y-intercept: 0.0
R-Squared: 0.864418807451
```

* Now, the model fits where brainwt = 0, bodywt = 0.
* Because we start at 0, the large outliers have a greater effect, so the coefficient has increased.
* Fitting the this linear assumption also explains slightly less of the variance.

Is this a better, or worse model? Why?

## Demo (We do)

We learned earlier that the the data in it's current state does not allow for the best linear regression fit. Try generating two more models using our log-transformed data to see how this transform changes our model's performance. Complete the following code to update X and y to match the log-transformed data. Complete the loop by setting the list to be one True and one False.

```python
X =
y =
loop = []
for boolean in loop:
    print 'y-intercept:', boolean
    get_linear_model_metrics(X, y, linear_model.LinearRegression(fit_intercept=boolean))
    print
```

* Out of the four, which model performed the best?
* Out of the four, which model performed the worst?

## Multiple Regression Analysis

- work through citibike data

#### What is Multicollinearity

- correlation plots
- atemp vs temp
- anything else correlated?

## Demo (We do)

- show how coefficients are effected by multicollinearity
- explore other combinations of features where they are highly correlated with each other

## Independent Practice (You do)

- build a model that predicts citibike ridership that
    * uses statistically significant features
    * passes the linear assumption (what would be the assumption here?)
    * well explains the variance in the dataset (r-squared)
    * has a feature space with low multicollinearity

## Conclusion
