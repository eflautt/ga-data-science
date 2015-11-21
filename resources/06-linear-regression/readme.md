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

Given some value __x__, its power in explanation __m__, and a starting point __b__, explain the value __y__.

However, the power of a linear regression is that we can use linear algebra to explain _multiple_ x's together in order to explain y:

y = betas * X + alpha (+ error)

Our terminology now being:

Given a matrix __X__, their relative coefficients __beta__, and a y-intercept __alpha__, explain a dependent vector, __y__.

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

## Single Regression Analysis

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
get_linear_model_metrics(
    X,
    y,
    linear_model.LinearRegression(fit_intercept=False)
)
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

Is this a better or worse model? Why?

## Demo (We do)

We learned earlier that the the data in it's current state does not allow for the best linear regression fit. Try generating two more models using our log-transformed data to see how this transform changes our model's performance. Complete the following code to update X and y to match the log-transformed data. Complete the loop by setting the list to be one True and one False.

```python
X =
y =
loop = []
for boolean in loop:
    print 'y-intercept:', boolean
    get_linear_model_metrics(
        X,
        y,
        linear_model.LinearRegression(fit_intercept=boolean)
    )
    print
```

* Out of the four, which model performed the best?
* Out of the four, which model performed the worst?

## Multiple Regression Analysis

While in the above example one variable well explained the variance of another, more often than not, we will need multiple variables. For example, a house's price may be best measured by square feet, but a lot of other variables play a vital role: bedrooms, bathrooms, location, appliances, etc. For a linear regression, we want these variables to be largely independent of each other, but all help explain the y variable.

We'll work with bikeshare data to help showcase what this means; and to explain a concept called _multicollinearity_.

#### What is Multicollinearity

With the bike share data, let's compare three data points: actual temperature, "feel" temperature, and guest ridership. Our data is already normalized between 0 and 1, so we'll start off with the correlations and modeling.

```python
bike_data = pd.read_csv('data/bikeshare.csv')
cmap = sns.diverging_palette(220, 10, as_cmap=True)

correlations = bike_data[['temp', 'atemp', 'casual']].corr()
print correlations
print sns.heatmap(correlations, cmap=cmap)
```

The correlation matrix explains:

* both temperature fields are moderately correlated to guest ridership;
* the two temperature fields are _highly_ correlated.

Including both of these fields in a model could introduce a painpoint of _multicollinearity_, where it's more difficult for a model to determine which feature is effecting the predicted value.

We can measure this effect in the coefficients:

```python
y = bike_data['casual']
x_sets = (
    ['temp'],
    ['atemp'],
    ['temp', 'atemp'],
)

for x in x_sets:
    print ', '.join(x)
    get_linear_model_metrics(bike_data[x], y, linear_model.LinearRegression())
    print
```

```bash
temp
P Values: [ 0.]
Coefficients: [ 117.68705779]
y-intercept: -22.812739188
R-Squared: 0.21124654163

atemp
P Values: [ 0.]
Coefficients: [ 130.27875081]
y-intercept: -26.3071675481
R-Squared: 0.206188705733

temp, atemp
P Values: [ 0.  0.]
Coefficients: [ 116.34021588    1.52795677]
y-intercept: -22.8703398286
R-Squared: 0.21124723661
```

Even though the 2-variable model `temp + atemp` has a higher explanation of variance than two two variables on their own, we can see that together, their coefficients are wildly different. This can introduce error in how we explain models.

What happens if we use a second variable that isn't highly correlated with temperature, like humidity?

```bash
temp, hum
P Values: [ 0.  0.]
Coefficients: [ 112.02457031  -80.87301833]
y-intercept: 30.7273338581
R-Squared: 0.310901196913
```

While temperature's coefficient is higher, the logical output still makes sense: for guest riders we expected a positive relationship with temperature and a negative relationship with humidity, and our model suggests it as well.

Note, on a slightly related note, there can be a similar effect from a feature set that is a singular matrix, which is when there is a clear relationship in the matrix (for example, the sum of all rows = 1).

```python
weather = pd.get_dummies(bike_data.weathersit)
get_linear_model_metrics(weather[[1, 2, 3, 4]], y, linear_model.LinearRegression())
print
# drop the least significant, weather situation  = 4
get_linear_model_metrics(weather[[1, 2, 3]], y, linear_model.LinearRegression())
```

```bash
P Values: [  3.75616929e-73   3.43170021e-22   1.57718666e-55   2.46181288e-01]
Coefficients: [  4.05237297e+12   4.05237297e+12   4.05237297e+12   4.05237297e+12]
y-intercept: -4.05237297302e+12
R-Squared: 0.0233498651216

P Values: [  3.75616929e-73   3.43170021e-22   1.57718666e-55]
Coefficients: [ 37.87876398  26.92862383  13.38900634]
y-intercept: 2.66666666652
R-Squared: 0.0233906873841
```

This model makes more sense, and increased r-squared by about 60% shows this was a good choice! However at this point, we still have a lot of work to do!

## Demo (We do)

Let's complete some of this code together and visualize the correlations of all the numerical features built into the data set.

We want to:
* Add the three weather situations into our current model
* Fine two more features that are not correlated with current features, but could be strong indicators for predicting guest riders.

```python
bikemodel_data = bike_data.join() # add in the three weather situations

cmap = sns.diverging_palette(220, 10, as_cmap=True)
correlations = # what are we getting the correlations of?
print correlations
print sns.heatmap(correlations, cmap=cmap)

final_feature_set = bikemodel_data[columns_to_keep]

get_linear_model_metrics(final_feature_set, y, linear_model.LinearRegression())
```

## Independent Practice (You do)

We've completely a model together that explains casual guest riders. It's now your turn to build another model, but using a different y variable: registered riders.

#### Pay attention to:

* the distribution of riders (should we rescale the data?)
* checking correlations with variables and registered riders
* having a feature space (our matrix) with low multicollinearity
* model complexity vs explanation of variance: at what point do features in a model stop improving r-squared?
* the linear assumption -- given all feature values being 0, should we have no ridership? negative ridership? positive ridership?

#### Bonus

* Which variables would make sense to dummy (because they are categorical, not continuous)?
* What features might explain ridership but aren't included in the data set?
    * Is there a way to build these using pandas and the features available?

#### Goal

If your model has an r-squared above .4, consider this a relatively effective model for the data available. Kudos!

## Conclusion (5 mins)
- How do you dummy a categorical variable?
    - How do you avoid a singular matrix?
- What is a single linear regression?
- What makes multi-variable regressions more useful?
    - What challenges do they introduce?
