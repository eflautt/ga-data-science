---
title: Statistics Fundamentals
duration: "1:45"
creator:
    name: Amy Roberts
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Statistics Part 2
Week # 2 | Lesson # 4

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
-  Explain the difference between causation vs. correlation
- Test a hypothesis within a sample case study
- Validate your findings using statistical analysis (p-values, confidence intervals)

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
	- Explain the difference between variance and bias  
	- Use descriptive stats to understand your data

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Gather materials needed for class
- Complete Prep work required
- Prepare any specific instructions

### Data Source
Today we will use adverstising data from an example in the 
An Introduction to Statistical Learning by Gareth James.

http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv

Instructor note- this is used in the demo and can downloaded directly from the website by running that cell of the notebook. No other files are needed. 

### LESSON GUIDE

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Lesson Objectives  |
| 5 min  | [Introduction](#introduction1)   | Causation and correlation |
| 25 min  | [Lecture](#lecture1)  | Causality vs correlation |
| 15 min  | [Guided Practice](#guided-practice)  | Confounding and DAGs |
| 5 min  | [Introduction](#introduction2)   | Hypothesis Testing |
| 30 min  | [Demo](#demo)   | Hypothesis testing in case study |
| 5 min  | [Introduction](#introduction3) | Validate your findings |
| 20 min  | [Demo](#demo2)  | P-values, CI in the case study|
| 35 min  | [Independent Practice](#independent-practice)  | Practice with p-values and CI|
| 15 min  | [Wrap-up](#wrapup)  | Review Guided Practice|


---
<a name="opening"></a>
## Opening (5 min)
- Review Current Lesson Objectives
   
<a name="introduction"></a>
## Intro: Causation and Correlations (5 mins)
If an association is observed, the first question asked must always be… is it real. 
Just think of all the times you've seen press about foods being good for you then being terrible for you. Why is this? The first reason could simiply be sensational headlines. But the other issue is having robust data analysis and a deep understanding of the difference between causation and correlation. 
(See images in assets)

Understanding the difference between causation and correlation is critical both at the beginning of our workflow for the 1. identify and 2. aquire stages, when we make sure that we fully article our question and use the right data to answer it, by including any potential confounders. Additionally, this topic comes back for the final step in our datascience work flow when we present the results- it is imporant that we present our findings in a way that doesn't overstate what our model actually measured. (e.g. saying caused when we really measured and association)

<a name="#lecture1"></a>
## Lecture: Causation vs Correlation (10 min)

#### Causal Criteria
Causal criteria is one approach to assessing causal relationships, very hard (impossible?) to define universal causal criteria.

One such attempt that is commonly used in the medical/health sciences field is based on the work by a Bradford Hill. He developed a list of "tests" that an analysis much pass inorder to indicate that there is a causal relationship. 

Causality requirements according to Bradford Hill
1. Strength of association
2. Consistency
3. Specificity
4. Temporality
5. Biological gradient
6. Plausibility
7. Coherence
8. Experiment
9. Analogy

Bradford-Hill’s paper is useful (e.g., understanding that your predictor/exposure came before the outcome- for smoking to cause cancer, one must have started smoking prior to getting cancer). 

But its NOT a “causal checklist" for causality, depending on you field you may never need to focus on causality.

Most commonly we find an association between two vairables. This means that we observe a correlation between our varibales but we may not fully understand the causal direction or the other factors that may be influencing the association we are observing. 

#### Knowledge Check
What is the difference between causality and an association?

<a name="#guided-practice"></a>
## Guided Practice: Confounding and DAGs (15 min)
#### Counfounding 
Often times, the obeservation that we observe may be influenced by another factor.
Let's start with an example. Let's say we did an analysis to understand what causes lung cancer. We find a strong association between carrying cigarette lighters and lung cancer. 

In fact we find, people who carry cigarette lighters are 2.4 times as likely to contract lung cancer as people who don’t carry lighters. 

show smoking-DAG image- Clearly we did not fully understand the relationship of our variables when attempting this analysis. 

A tool that is handy to help determine what variables are most important for your model can be a DAG- Directed Acyclic Diagram. 

It always includes at least one expsoure/predictor and one outcome. 
For example: 
TV Ads --> Sales

Here the exposure/predictor is TV ads and it is associated with an outcome, sales. We can see this arrow leading from tv to sales.

What other factors may increase sales of a hover board? Radio Ads? 

the DAG would then look something like 

TV Ads --> Sales <-- Google Ads

### Think, Pair, Share
Let's say we want to evaluate which type of ad is associated with higher sales. 

Have the students draw on their table/board the basic DAG above. Take 2 min and think about other things that may predict sales. 

Take 1 min to chat with other students about the predictors you've thought of. 

Share one or two examples. 

Instructor Note- Look for a student who brought up seasonality (or similar) have them share. Use this a jump off point to go back to confounding. 

Great- so let's take a look at the association between TV Ads and Sales by taking into account seaonality. 

On a DAG it would look something like (a triangle with:  TV--> Sales and seasonality --> TV Ads and seasonality --> Sales and a 2nd DAG swaping out TV with Google ads). 

If we compare TV ads and Google Ads but didn't take into account that the TV ads where run in Nov/December before biggest gift giving season. While the Google ads where run during Feb and March, when sales always drop. We may incorrectly assume that Google Ads are not as effective as TV ads. This is an example of bias and confounding. 


#### Real world application
This example highlights a few things. 1) the importance of having deep subject area knowledge so that you can trust that your analysis is logical. You can show a strong association but be totally wrong as in the smoking example and many of the examples we saw at the beginging of the class. 2) That a DAG- Directed acyclic graph can be handy for thinking through the logic of your models 3) the difference between causality and association.

Though it's relatively obivous that there is a flaw in our logic here. It can be tricky when we are working on cuting edge fields or problems where the "truth" isn't readily apparent. Through out the class we will be working on helping you develop your intuition about data, so that you can spot the differences more readily. With this will come a bunch of tools to help you. But keep in mind- the analysis is only as good as your understanding of the problem and the data.



<a name="introduction2"></a>
## Introduction: Hypothesis Testing (5 mins)
You'll remember from last time that we worked on descriptive statistics. How would we tell if there is a difference between our groups? How would we know if that difference was real or if our finding is simply due to chance? These are the questions we often tackle when we are building out our models in the Model Building step of our workflow. 

For example- if we were working on sales data, how would we know if there was a difference between the buying patterns of men and women at Acme Inc? Hypothesis tesing!

#### Hypothesis testing steps
Generally speaking, you start with a null hypothesis and an alternative hypothesis (that is opposite the null). Then, you check whether the data supports rejecting the null hypothesis or failing to reject the null hypothesis. (Note that "failing to reject" the null is not the same as "accepting" the null hypothesis. The alternative hypothesis may indeed be true, except that you just don't have enough data to show that.) We make this distinction because it is important to only state what your data and analysis can truly represent and to avoid overstating the findings.

Here is an example of a conventional hypothesis test:
null hypothesis: There is no relationship between gender and Sales
alternative hypothesis: There is a relationship between gender and Sales 

Let's dive into this more with the demo. 

<a name="demo"></a>
## Demo: Hypothesis Testing Case Study (30 mins)
Instructor note- walk through the demo with students. Through out the demo there are certain sections marked student questions. Give the students time to answer the questions individually or as a small group (2 min or so per question) then share with the class and discuss before moving on to the next question. Discuss at each question and clear up any misconceptions. Answers are in the solution code. 

use IPython Notebook demo-1.ipynb PART 1

#### Final Check for understanding
What is the null hypothesis? 

<a name="introduction3"></a>
## Validate your fidnings (5 mins)
How do we tell if the association we observed is statistically significant?
Statistical Significance is the likelihood that a result or relationship is caused by something other than mere random chance. Statistical hypothesis testing is traditionally employed to determine if a result is statistically significant or not. 

Typically we use a cutpoint of 5%. In other words, we say that something is statistically significant if there is a less than 5% chance that our finding was do to chance alone. When data scientists present results and say we found a significant result- it is almost always using these critria. Let's dive into them further to understand p-values and confidence intervals. 

<a name="demo2"></a>
## Demo: P-values, CI in the case study (20 mins)
use IPython Notebook demo-1.ipynb PART 2
Instructors note- same as demo part1

#### Check for understanding
What does the 95% CI indicate? 
That if we repeated our analysis 100 times the point estimate we found would be there in 95% of the time. 

<a name="independent-practice"></a>
## Guided Practice (35 min)
For this exercise you will look through a variety of analyses and interpret the findings. You will be presented a series of outputs (very similar to the ones we will generate our selves when we start regression) and tables (from a published analysis). For this lab you will be asked to read these outputs and tables and determine if the findings were statiscally significant or not. You will also get practice looking at the output and understanding how the model was built (idying- predictor/exposure vs outcome)

Use independent-practice.ipynb

<a name="wrapup"></a>
## Project questions (15 mins)
Go over the solution to each question in the independent practice with class and clarify any confusing points or remaining questions. 


***

### BEFORE NEXT CLASS
|   |   |
|---|---|
| **HOMEWORK** | TBD |
| **PREWORK**  | TBD  |
| **PROJECT**  | TBD  |

### ADDITIONAL RESOURCES
- see ipython notebook