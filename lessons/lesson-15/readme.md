---
title: Timeseries Analysis
duration: "3:00"
creator:
    name: Arun Ahuja
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 
DS | Lesson 15

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand what timeseries data is and what is unique about it
- Perform time series analysis in Pandas including rolling_mean/median and autocorrelation

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Load data with Pandas, plotting data with Seaborn
- Understand correlation


### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Review [Final Project, pt. 3](../../projects/final-projects/03-exploratory-analysis/readme.md)
- Copy and modify the [lesson slide deck](./assets/slides/slides-15.md)
- Read through datasets and starter/solution code
- Add to the "Additional Resources" section for this lesson

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Lesson Objectives  |
| 30 min  | [Introduction](#introduction-timeseries)   | Intro to Timeseries |
| 25 min  | [Introduction](#introduction-timeanalytics)   | Intro to Timeseries Analysis |
| 60 min  | [Demo/Codealong](#code1)  | Demo/Codealong: Exploring Rossmann Drug Store Sales Data |
| 35 min  | [Independent Practice](#ind-practice)  | Timeseries Exercises |
| 20 min  | [Independent Practice/Review](#ind-practice-review)  | Review: Timeseries Exercises|
| 5 min  | [Conclusion](#conclusion)  | Review Lesson |

---
<a name="opening"></a>
## Opening (5 min)
In this class, we will discuss analyzing data that is changing over time. While most of our previous examples have assumed that our data was collected at over time, we didn't care which data points were collected earlier or later. We had made assumptions that the data was _not_ changing over time. In this class, we will discuss statistics associated with data with that is changing over time and how to measure that change. 

In this lesson we will focus on IDENTIFYing problems that are related to time series and understanding the type of questions we are interested in. Additionally, we will discuss the unique aspects of MINEing and REFINEing time series data.

<a name="introduction-timeseries"></a>
## Intro: What are (is) time series data? (20 mins)

Time series data is any data where the individual data points change over time. This would be fairly common in most business data, we expect sales to change according to the seasons and trends. You will find this property in many social phenomena as well, it's been documented that there is traditionally more crime in the summer months.

To be honest, _most_ datasets likely to have an important time component, but typically we assume that it's fairly minimal. If we are attempting to analyze salaries in an industry, it's clear that salaries shift over time and depending on the economic period. But, if we are examining the problem on a smaller scale (say 3-5 years) the effect of time on salaries is much smaller than say the industry or position.

When it is not - we often need to focus on identifying the aspects of the data that are influenced by time and those that aren't.

Typically, our time series data will be a sequence of values and we will be interested in studying the changes in this series and how related the individual values are. How much does this weeks sales effect next weeks? How much does today's stock price effect tomorrow's.

> **Check** Have the students identify time components of previous datasets used in class. For example, the `stumbleupon` dataset. This is a collection of news stories and we are predicting which are ever-lasting. One piece of this is identifying current events stories, so it's likely we will have to retrain our model over time. In a previous regressions on sports statistics or salaries, we likely could include a time component if we have many measurements over a long time horizon.

Time series analysis is useful for sales analysis, stock market trends, studying economic phenomena as well social science problems such as crime prediction.

Typically we are interested in separating the effect of time into two components:
    - trends: significant increases or decreases over time
    - seasonality: regularly repeating increases or decreases

In the following plot of fireworks injury rates from FiveThirtyEight, we can there is an overall _trend_ of fewer injuries and no seasonal pattern.

![](./assets/images/munguia-datalab-fireworks2.png)

However, many other phenomena may be entirely seasonal. If we look at the number of searches for the New Hampshire Primary, we can see that there are clear spikes in the number of searches every four years and on election years.

![](./assets/images/google-nh.png)

Similarly, searches for 'Gingerbread Houses' spike every year around the holiday season.

![](./assets/images/google-gingerbread.png)

Both of these spikes re-occur on a fixed time-scale, making them seasonal patterns. While we may see other types of regularly occurring up or down swings (for examples growth vs recession year for economic trends), seasonal patterns should repeat on a fixed timescale or _period_. Repeated patterns that are aperiodic are known as _cycles_. While identifying aperiodic cycles are important, they are often treated differently that seasonal effects. Seasonal effects are useful for there consistency, the fact that last year's (quarters, months, etc.) data is useful as a predictor.

Lastly, searches for 'iphone', have both a general trend upwards (indicating more popularity for the phone) as well as a spike in September, typically when Apple hosts its event to announce new versions
    
![](./assets/images/google-iphone.png)

Most often, we are interested in studying the _trend_ and not the seasonal fluctuations. Therefore it is important to identify whether we think a change in our time series is due to an ongoing trend or a seasonal change.

> **Check** Discuss one or two more time-series examples - identify trends and seasonal patterns. Using [Google trends](https://www.google.com/trends/) for this is a nice way to generate these.

- [](https://www.google.com/trends/explore#q=superbowl)
    - Seasonal pattern, with no real growth upward

- [](https://www.google.com/trends/explore#q=machine%20learning)
    - Strong trend upward over time

- [](https://www.google.com/trends/explore#q=neural%20networks%2C%20deep%20learning&cmpt=q&tz=Etc%2FGMT%2B5)
    - Trend downward in the use of neural networks, but upward in the use of deep learning


<a name="introduction-timeseries-analysis"></a>
## Intro: Common analysis for time series data (20 mins)

#### Moving Averages
 A _moving average_ replaces each data point with an average of _k_ consecutive data points in time. Typically this is k/2 data points prior to and following a given time point, but could also be the _k_ preceding timepoints. This is also referred to as the 'rolling' average. Our measure of average could be a median or a mean.

 The formula for a rolling _mean_ is below:

 ![](./assets/images/single_moving_avg_fit.gif)

> **Check:** What would a moving (rolling) mean indicate vs. a moving (rolling) median?

A rolling mean would average all values in the window, but can be skewed by outliers (extremely small or large values). This may be useful if we are looking to identify atypical periods or we want evaluate these odd periods. For example, we do want to reward holiday periods or more negatively view slumps or closures. The rolling median would provide the 50% percentile value for the period and perhaps more representative of a 'typical' day.

In the following plot from FiveThirtyEight, they have plotted the 30-day moving average of the Economic Uncertainty Index.

![](./assets/images/flowers-datalab-policy-2.gif)

Plotting the moving average allows us to more easily visualize trends, by smoothing out random fluctuations and removing outliers.

While this statistic weights all data evenly, it may make more sense to weight data closer to our date of interest higher. We can do this similar to taking a weighted average, and take a _weighted moving average_.

A common weighting scheme is an _exponential weighted moving average_, where we add in a _decay_ term, and give less and less weight to further data points.

To compute this value, suppose, we have value `v_1, ..., v_N`, and we want to compute a lag `k` average at time `T`. To start, we fix a decay value \alpha. Then, we recursively compute the exponential weighted moving average.

Start with: `M_0 = v_(T-k)`
Then: `M__i = (1-\alpha) * M_(i-1) + v_(T - k + 1)`
Finishing with: `M = M_T = (1-\alpha) * M_(T-1) + v_T`

#### Autocorrelation

While in previous classes we have been concerned with how correlated two variables are: height and weight, education and salary - autocorrelation is how correlated a variable is with itself. Specifically, how related are variables earlier in time with variables later in time.

![](./assets/images/autocorrelation.gif)

To compute autocorrelation, we fix a 'lag', k, which is how many timepoints earlier should we use to compute the correlation. With a lag of 1 of we compute how correlated a value is with the prior one and with a lag of 10, we compute how correlated a variable is with one 10 time points earlier.


<a name="code1"></a>
## Demo/Codealong: Exploring Rossmann Drug Store Sales Data (10 mins)
> INSTRUCTOR NOTE: The data setup and examples of Pandas functionality are in this README as well the starter/solution code notebook.

We will be using data made available by a German drugstore, Rossmann. This data contains the daily sales made at the drugstore as well as whether there was a sale or holiday affecting the sales data.

#### Loading the data

As with previous datasets, we can use Pandas to load our data.

```python
import pandas as pd

data = pd.read_csv('../assets/data/rossmann.csv', skipinitialspace=True)

```

Because we are most interested in the `Date` column that contains the date of sales for each store, we will make sure to process that as a `DateTime` type, and make that the index of our dataframe.

```python
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

data['Year'] = data.index.year
data['Month'] = data.index.month
```

This allows us to easily filter, by date as well. For example, to a particular year:

```python
data['2014']
```

or to a particular month:

```python
data['2015-05']
```

There are over a million sales data point in this dataset, so for some analysis we will focus on just one store.

```python
store1_data = data[data.Store == 1]
```

#### Plotting the sales data

As we begin to study the sales from this drugstore, we will also want to known both the time dependent elements of sales as well as whether promotions or holidays effected sales. To start, we can simply compare the average sales on those events.

To compare sales on holidays, we can compare the sales using box-plots, which allows us to compare the distribution of sales on holidays against all other days.  On state holidays the store is closed (and as a nice sanity check there are 0 sales), and on school holidays the sales are relatively similar.

```
sb.factorplot(
    x='SchoolHoliday',
    y='Sales',
    data=store1_data, 
    kind='box'
)
```

> **Check:** Have the students check if there is a difference on sales on promotion days.

We can see that there _is_ a difference in sales on promotion days.

```python
sb.factorplot(
    col='Open',
    x='Promo',
    y='Sales',
    data=store1_data, 
    kind='box'
)
```

Why is it important to separate out days where the store is closed? Because they aren't any promotions on those days either, so including them will bias your sales data on days without promotions!

We may also want to compare sales across days of the week

```python
sb.factorplot(
    col='Open',
    x='DayOfWeek',
    y='Sales',
    data=store1_data,
    kind='box',
    
)
```

Lastly, we want to identify larger-scale trends in our data. How did sales change from 2014 to 2015? Were any particularly interesting outliers in terms of sales or customer visits?

To plot the sales over time:

```python
# Filter to days store 1 was open
store1_open_data = store1_data[store1_data.Open==1]
store1_open_data[['Sales']].plot()
```

To plot the customer visits over time:

```python
store1_open_data[['Customers']].plot()
```

We can see that there are large spikes of sales and customers towards end of 2013 and 2014 leading into the first quarter of 2014 and 2015.

> **Check:** Have the students use the index filtering to filter just 2015 to zoom-in on changes over time. This should make it easier to identify the holiday sales bump.

```python
store1_data_2015 = store1_data['2015']
store1_data_2015[
    store1_data_2015.Open==1
][['Sales']].plot()
```

#### Computing Autocorrelation

To measure how much the sales are correlated with each other, we want to compute the _autocorrelation_ of the 'Sales' column.. In pandas we do this we with the `autocorr` function

`autocorr` takes one argument, the `lag` which is how many data points prior should be used to compute the correlation. If we set the `lag` to 1, we compute the correlation between every point and the point directly preceding it, while setting `lag` to 10, computes the correlation between every point and the point 10 days earlier

```python
data['Sales'].resample('D', how='mean').autocorr(lag=1)
```

As with correlation between different variables, as this number moves closer to 1 the data is more correlated.

> **Check:** What does the autocorrelation values of Sales and Customers imply about our data?

> Instructor's Note: Here we are looking for a discussion of the dependence of a certain value, sales, on a previous day's sales. There seems be some dependence day to day, but also year to year.


#### Aggregates of sales over time

If we want to investigate trends over time in sales, as always, we will start by computing simple aggregates.  What we want to know is, what were the mean and median sales in each year and each month?

In Pandas, this is performed using the `resample` command, which is very similar to the `groupby` command. It allows us to group over different time intervals.

We can use `data.resample` and provide as arguments:
    - a level on which to roll-up to, 'D' for day, 'W' for week, 'M' for month, 'A' for year
    - and what aggregation to perform: 'mean', 'median', 'sum', etc.

```python
data[['Sales']].resample('A', how=['median', 'mean'])

data[['Sales']].resample('M', how=['median', 'mean'])
```

Here we can see again that December 2013 and 2014 were the highest average sale months.

While identifying the monthly averages are useful, we often want to compare the sales data of a date to a smaller window. To understand holidays sales we want not want to compare the sales data of late December with the entire month, but perhaps a few days surrounding it. We can do this using rolling averages.

In pandas we can compute rolling average using the `pd.rolling_mean` or `pd.rolling_median` functions.

```python
pd.rolling_mean(data[['Sales']], window=3, center=True, freq='D')
```

This computes a rolling mean of sales using the sales on each day, the day preceding and the day following (window = 3, center=True).


`rolling_mean` (as well as `rolling_median`) takes three important the parameters:
    - the first is the series to aggregate
    - `window` is the number of days to include in the average
    - `center` is whether the window should be centered on the date or use data prior to that date
    - `freq` is on what level to roll-up the averages to (as used in `resample`). Either `D` for day, `M` for month or `A` for year, etc.

We can use our index filtering to just look at 2015.

```python
pd.rolling_mean(data[['Sales']], window=3, center=True, freq='D')['2015']
```

Instead of plotting the full timeseries, we can plot the rolling mean instead, which smooths random changes in sales as well as removing outliers, helping us identify larger trends.

```python
pd.rolling_mean(data[['Sales']], window=10, center=True, freq='D').plot()
```

As we discussed earlier, this averages all values in the window evenly, while we might want to weight closer values more. For example, for a centered weighted average of 10 days, we want to put for emphasis on +/- 1 day versus +/- days. One option to do that is the `ewma` function or `exponential weighted moving average` function.

```python
pd.ewma(data['Sales'], span=10)
```

> **Check:** Have the student discuss the differences in the plot between the 10-day moving average and the 10 day exponentially weighted moving average.

#### Pandas Window functions

Pandas `rolling_mean` and `rolling_median` are only two examples of Pandas window function capabilities. Window functions are operate on a set of N consecutive rows (a window) and produce an output.

In addition to `rolling_mean` and `rolling_median`, there are `rolling_sum`, `rolling_min`, `rolling_max`, and many more.

Another common one is `diff`, which takes the difference over time. `pd.diff` takes one arugment, `periods`, which is how many rows prior to use for the difference.

For example, if we want to compute the difference in sales, day by day, we could compute.

```python
data['Sales'].diff(periods=1)
```

However, if wanted to compare the same day the prior week, we could set `periods=7`

```python
data['Sales'].diff(periods=7)
``` 

This would compute the difference in sales, from every day to the same day in previous week. Difference functions allow us to identify seasonal changes as we see repeated up or downswings.

In the following plot of the month to month change (`diff`) in jobs from FiveThiryEight helps identify the seasonal component of the number of retail jobs. 

![](./assets/images/casselman-datalab-wsj2.png)

#### Pandas Expanding Functions

In addition to the set of `rolling_*` functions, Pandas also provides a similar collection of `expanding_*` functions, which, instead of using a window of N values, use all values up until that time.

For example, 

```python
pd.expanding_mean(data['Sales'], freq='d')
```

computes the average sales, from the first date _until_ the date specified. Meanwhile,

```python
pd.expanding_sum(data['Sales'], freq='d')
```

computes the sum of average sales per store up until that date.


<a name="ind-practice"></a>
> INSTRUCTOR NOTE: The solution code for these are below as well in the [solution code notebook]().

1. Plot the distribution of sales by month and compare the effect of promotions
2. Are sales more correlated with the prior date, a similar date last year, or a similar date last month?
3. Plot the 15 day rolling mean of customers in the stores
4. Identify the date with largest drop in sales from the same date in the previous month
5. Compute the total sales up until Dec. 2014
6. When were the largest differences between 15-day moving/rolling averages?
HINT: Using `rolling_mean` and `diff`


<a name="ind-practice-review"></a>

1. Plot the distribution of sales by month and compare the effect of promotions

```python
sb.factorplot(
    col='Open',
    hue='Promo',
    x='Month',
    y='Sales',
    data=store1_data, 
    kind='box'
)
```

2. Are sales more correlated with the prior date, a similar date last year, or a similar date last month?

```python
# Compare the following:
average_daily_sales = data[['Sales', 'Open']].resample('D', how='mean')

average_daily_sales['Sales'].autocorr(lag=1)

average_daily_sales['Sales'].autocorr(lag=30)

average_daily_sales['Sales'].autocorr(lag=365)
```

3. Plot the 15 day rolling mean of customers in the stores

```python
pd.rolling_mean(data[['Sales']], window=15, freq='D').plot()
```

4. Identify the date with largest drop in sales from the same date in the previous month

```python
average_daily_sales = data[['Sales', 'Open']].resample('D', how='mean')
average_daily_sales['DiffVsLastWeek'] = average_daily_sales[['Sales']].diff(periods=7)

average_daily_sales.sort(['DiffVsLastWeek']).head
```

Unsurprisingly, this day is Dec. 25 and Dec. 26 in 2014 and 2015. When the store is closed and there are many sales in the preceding week. How, about when the store is open?

```python
average_daily_sales[average_daily_sales.Open == 1].sort(['DiffVsLastWeek'])
```

The top values are Dec. 24 and then 2013-12-09 and 2013-10-14 where on average sales were 4k lower than the same day in the previous week.


5. Compute the total sales up until Dec. 2014

```python
total_daily_sales = data[['Sales']].resample('D', how='sum')
pd.expanding_sum(total_daily_sales)['2014-12']
```

Note that this is **NOT**

```python
pd.expanding_sum(data['Sales'], freq='D')
```
 
since we do not, want to first average over stores.

6. When were the largest differences between 15-day moving/rolling averages?
HINT: Using `rolling_mean` and `diff`

```python
pd.rolling_mean(data[['Sales']], window=15, freq='D').diff(1).sort('Sales')
```

Unsurprisingly, they occur at the beginning of every year after the holiday season.


<a name="conclusion"></a>
## Conclusion (5 mins)
- We will use time series analysis to identify changes in values over time
- We want to identify whether changes are true trends or seasonal changes
- Rolling means give us a local statistic of an average in time, smoothing out random fluctuations and removing outliers
- Autocorrelations are a measure of how much a data point is dependent on previous data points

***

### BEFORE NEXT CLASS
|   |   |
|---|---|
| Upcoming Projects | [Final Project, Part 3](../../projects/final-projects/03-exploratory-analysis/readme.md)

### ADDITIONAL RESOURCES

- a
- b
- c
