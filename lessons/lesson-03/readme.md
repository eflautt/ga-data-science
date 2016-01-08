---
title: Statistics Fundamentals
duration: "1:45"
creator:
    name: Amy Roberts
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Experimental Design and Pandas
Week # 2 | Lesson # 3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*

- Use NumPy and Pandas libraries to analyze datasets using basic summary statistics: mean, median, mode, max, min, quartile, inter-quartile range, variance, standard deviation, and correlation 
- Create data visualizations - including: line graphs, box plots, and histograms- to discern characteristics and trends in a dataset
- Identify a normal distribution within a dataset using summary statistics and visualization
- ID variable types and complete dummy coding by hand


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*

- Create, open and create and IPython Notebook
- Have completed python pre-work

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*

- Gather materials needed for class
- Complete Prep work required
- Prepare any specific instructions

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Lesson Objectives  |
| 10 min  | [Introduction](#introduction1)   | Laying the ground work |
| 30 min  | [Codealong](#codealong1)  | Summary statistics in Pandas |
| 10 min  | [Introduction](#introduction2)   | Is this normal? |
| 15 min  | [Demo](#demo)   | Determining the distribution of your data |
| 10 min  | [Guided Practice ](#guidedpractice2)  | Is this skewed?  |
| 20 min  | [Introduction](#introduction3) | Variable types |
| 10 min  | [Demo](#demo2)  | Classes |
| 10 min  | [Independent Practice](#practice)  | Dummy colors |
| 10 min  | [Conclusion](#conclusion)  | Review dummies and lesson objectives |
| 15 min  | [Wrap-up](#wrapup)  | Project questions and Next Project|

---
<a name="opening"></a>
## Opening (5 min)
- Review Current Lesson Objectives
   
<a name="introduction"></a>
## Intro: Laying the ground work (20 mins)
Define
1. mean
2. median
3. mode
4. max
5. min
6. quartile
7. inter-quartile range
8. variance
9. standard deviation
10. correlation 

### Mean 
> Instructor Note: Content for mean, median and mode sourced from www.yti.edu/lrc/images/math_averages.doc)

The mean of a set of values is the sum of the values divided by the number of values.  It is also called the average.

	Example:  Find the mean of 19, 13, 15, 25, and 18

		19 + 13 + 15 + 25 + 18    =    90   =   18
		_______________________	    _______
			   5		                5


### Median

The median refers to the midpoint in a series of numbers.

To find the median, arrange the numbers in order from smallest to largest.  If there is an odd number of values, the middle value is the median.  If there is an even number of values, the average of the two middle values is the median.

Example #1:  Find the median of 19, 29, 36, 15, and 20

		In order:  15,  19,  20,  29,  36  since there are 5 values (odd number), 20 is the median (middle number)

	Example #2:  Find the median of 67, 28, 92, 37, 81, 75

		In order:  28,  37,  67,  75,  81,  92   since there are 6 values (even number), we must average those two  middle numbers to get the median value

		Average:  (67 + 75) / 2  =    142/2    =    71 is the median value


### Mode

The mode of a set of values is the value that occurs most often. A set of values may have more than one mode or no mode.

	Example #1:  Find the mode of  15, 21, 26, 25, 21, 23, 28, 21
	     The mode is 21 since it occurs three times and the other values occur only once.

	Example #2:  Find the mode of 12, 15, 18, 26, 15, 9, 12, 27
	      The modes are 12 and 15 since both occur twice. 

	Example #3:  Find the mode of 4, 8, 15, 21, 23
	      There is no mode since all the values occur the same number of times.

### Concept Check: 

A.  For the following groups of numbers, calculate the mean, median and mode by hand


1. 18, 24, 17, 21, 24, 16, 29, 18		
Mean_______
Median______
Mode_______
Max _______
Min _______

Answers:
Mean = 20.875
Median = 19.5
Mode = 18, 24
Max = 29
Min = 16

2. 75, 87, 49, 68, 75, 84, 98, 92			
Mean_______
Median______
Mode_______
Max _______
Min _______

Answers:
Mean = 78.5
Median = 79.5
Mode = 75
Max = 98
Min = 49

3. 55, 47, 38, 66, 56, 64, 44, 39		
Mean_______
Median______
Mode_______
Max _______
Min _______

Answers:
Mean = 51.125
Median = 51
Mode = none
Max = 66
Min = 38


<a name="#codealong1"></a>
## Codealong: Summary statistics in Pandas (30 min)

> Instructor Notes: Have students open the [starter-code](./lab/starter-code/starter-code-3.ipynb). Solutions are available in [the solution-code](.). 

### Codealong Part 1: Basic Stats-
See the following concepts in action on "Part 1. Basic Stats" of the [starter-code]().

We will begin by using pandas to calculate the same Mean, Median, Mode, Max, Min from above.

	Methods available include: 
		.min() - Compute minimum value
		.max() - Compute maximum value
		.mean() - Compute mean value
		.median() - Compute median value
		.mode() - Compute mode value
		.count() - Count the number of observations


### Quartiles and Interquartile Range
Quartiles divide a rank-ordered data set into four equal parts. The values that divide each part are called the first, second, and third quartiles; and they are denoted by Q1, Q2, and Q3, respectively. The interquartile range (IQR) is a measure of variability, based on dividing a data set into quartiles. Let's take a look in the notebook. 

### Codealong Part 2: Box Plot
See the the following concepts in action "Part 2. Box Plot" of the lesson-3-codealong-starter-code/lesson-3-codealong-solutions.ipynb
There is a handy graph- the box-plot that gives us a nice visual of these metrics as well as the quartile and the interquaritle range. 

### Bias vs Variance 
**Error due to Bias:** The error due to bias is taken as the difference between the expected (or average) prediction of our model and the correct value which we are trying to predict. Imagine you could repeat the whole model building process more than once: each time you gather new data and run a new analysis creating a new model. Due to randomness in the underlying data sets, the resulting models will have a range of predictions. Bias measures how far off in general these models' predictions are from the correct value.  
**Error due to Variance:** The error due to variance is taken as the variability of a model prediction for a given data point. Again, imagine you can repeat the entire model building process multiple times. The variance is how much the predictions for a given point vary between different realizations of the model. 
<img(src='images/biasVsVarianceImage.png', style="width: 30%; height: 30%")>

### Standard Deviation 
In statistics, the standard deviation (SD, also represented by the Greek letter sigma, σ for the population standard deviation or s for the sample standard deviation) is a measure that is used to quantify the amount of variation or  dispersion of a set of data values. **It is the square root of the variance.**

### Standard Error
The standard error of the mean (SEM) quantifies the precision of the mean. It is a measure of how far your sample mean is likely to be from the true population mean. It is expressed in the same units as the data.

As the standard error of an estimated value generally increases with the size of the estimate, a large standard error may not necessarily result in an unreliable estimate. Therefore it is often better to compare the error in relation to the size of the estimate.

The regression line is the line that minimizes the sum of squared deviations of prediction (also called the sum of squares error). The standard error of the estimate is closely related to this quantity. 


#### Codealong Part 3
See the the following concepts in action "Part 3. Standard Deviation and Variance" of the lesson-3-codealong-starter-code/lesson-3-codealong-solutions.ipynb

To calculate the variance and SD in pandas.

	Methods include: 
		.std() - Compute Standard Deviation
		.var() - Compute variance
		.describe() - short cut that prints out count, mean, std, min, quartiles, max

### Correlation
The correlation is a quantity measuring the extent of interdependence of variable quantities. 

### Knowledge Check
1. What is the difference between bias and variance?
	- see above for the answer 
2. What is a commonly used metric that describes variance?
	- STD
3. What is the formula for this metric? 
	- square root of variance

#### Context
Often times when you are working on a project, descriptive statistics will be the first, and often times the only, step for analysis. Say you need to understand the demographics of your customer base-- descriptive stats will give you the answer. You don't need a fancy model to answer the most common business questions. In the academic setting this information will come in the form of a "table 1". 
 
 
<a name="introduction2"></a>
## Introduction: Is this normal? (10 mins)
A normal distribution is a key assumption to many models we will later be using. But what is normal? 

The graph of the normal distribution depends on two factors - the mean and the standard deviation. The mean of the distribution determines the location of the center of the graph, and the standard deviation determines the height of the graph. When the standard deviation is large, the curve is short and wide; when the standard deviation is small, the curve is tall and narrow. All normal distributions look like a symmetric, bell-shaped curve.

Two metrics are commonly used to describe your distribution- skewness and kurtosis. 

**Skewness**  
In probability theory and statistics, skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. The skewness value can be positive or negative, or even undefined. 

**Kurtosis**  
Kurtosis is a measure of whether the data are peaked or flat relative to a normal distribution.That is, data sets with high kurtosis tend to have a distinct peak near the mean, decline rather rapidly, and have heavy tails.


<a name="demo"></a>
## Demo: Determining the distribution of your data (15 mins)
Instructors should use the file "lesson-3-demo" for this section. Walk through each section in the notebook in order. 


<a name="guidedpractice2"></a>
## Guided Practice: Is this skewed? (10 mins)
Walk through images of normal, skewed, sigmod etc distributions have students stand up and vote on the types. Instructor note- Use your own work or the images in the asset folder. 

After each discuss methods of correcting the issue. 

For example: 
Skewed? discuss centering on the mean or median
Not smooth? log transformations
Sigmodial? that's a feature- use logistic regression! 

<a name="introduction3"></a>
## Variable Types (5 min)
1. continuous
2. categorical

Continous variables are things such as height, income, etc.

Categorical variables are things such as race, gender, paint colors, movie titles


<a name="demo2"></a>
## Demo: Classes (15 mins)

###Class/Dummy Variables
Let's say we have a categorical variable called "area". It is saved in our dataset as one of the following strings:  
*	"rural"  
*	"suburban"  
*	"urban"

We have to represent categorical variables numerically, but we can't simply code it as 0=rural, 1=suburban, 2=urban because that would imply an **ordered relationship** between suburban and urban (and thus urban is somehow "twice" the suburban category). We do this by converting our 1 location variable into two new variables- area_urban and area_suburban. 

####Instructor note- Draw this on the board:
Using the example above lets draw out the table of how these varibles can be represented mathmatically without implying an order. We can do this with 0s and 1s. One of our categories will be all 0s- that will be our reference category. It is often good to select your reference category to be the group with 1) with the largest sample size 2) one that will help with your interpretations of your models. (e.g., often if you are testing for a disease the reference category will be those without the disease)

Step 1: Select a reference category. Here we will choose rural as our reference. Because urban is our reference catefory we will not have to include it when we make our two new variables.

Step 2. Convert the values urban, suburban and urban to a numeric reprensentation that does not imply an order. 

Step 3. Create two new variables: area_urban and area_suburban

Why do we only need **two dummy variables, not three?** Because two dummies capture all of the information about the Area feature, and implicitly defines rural as the reference level. (In general, if you have a categorical feature with k levels, you create k-1 dummy variables.)

 | area_urban | area_suburban 
--- | --- | ---
rural | 0 | 0
suburban | 0 | 1
urban | 1 | 0 

Great! Let's look at a second example. Let's say we have a category called gender with two categories 1. male and 2. female.  
1. How many dummy variables will we have in our data set? (# of categories - 1 = 2-1 = 1)
2. We will make male our reference so male will be coded 0, and female will be coded 1

 | gender_female
--- | ---
male | 0
female | 1

We can do this in pandas with the "get_dummies" method. Let's checkit out in the demo.


<a name="practice"></a>
## Independent Practice: Dummy Colors (15 mins)
It's important to understand the concept before we use get_dummies so today we will create dummies by hand. In future classes we will use get_dummies to create these.  We will use dummy variables in almost every analysis you complete because it is rare in most fields to only have continuous variables.

Have each student draw a table like we did above on the white board or table. 
Create dummy varibales for the variable "colors" that has 6 categories- blue, red, green, purple, grey, brown. Set grey as the reference. 

Answer: 

	| color_blue | color_red | color_green | color_purple | color_brown
--- | --- | --- | --- | --- | --- 
blue | 1 | 0 | 0 | 0 | 0
red  | 0 | 1 | 0 | 0 | 0
green | 0 | 0 | 1 | 0 | 0 
purple | 0 | 0 | 0 | 1 | 0
grey | 0 | 0 | 0 | 0 | 0
brown | 0 | 0 | 0 | 0 | 1


<a name="conclusion"></a>
## Conclusion (10 mins)
- Review questions from dummy practice
- Review objectives from class 

<a name="wrapup"></a>
## Project questions and Next Project (15 mins)
- Review Unit 1 objectives
- Project 1 questions
- Introduce the next project
- Exit tickes

***

### BEFORE NEXT CLASS
|   |   |
|---|---|
| **HOMEWORK** | TBD |
| **PREWORK**  | TBD  |
| **PROJECT**  | TBD  |

### ADDITIONAL RESOURCES
- see ipython notebook
