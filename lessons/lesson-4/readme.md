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

### LESSON GUIDE

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Lesson Objectives  |
| 5 min  | [Introduction](#introduction1)   | Causation and correlation |
| 25 min  | [Lecture](#lecture1)  | Causality vs correlation |
| 5 min  | [Introduction](#introduction2)   | Hypothesis Testing |
| 30 min  | [Demo](#demo)   | Hypothesis testing in case study |
| 5 min  | [Introduction](#introduction3) | Validate your findings |
| 20 min  | [Demo](#demo2)  | P-values, CI in the case study|
| 35 min  | [Guided Practice](#guided-practice)  | Practice with p-values and CI|
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


<a name="#lecture1"></a>
## Lecture: Causation vs Correlation (25 min)

#### Causal Criteria
Causal criteria is one approach to assessing causal relationships, very hard (impossible?) to define universal causal criteria.

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

Bradford-Hill’s paper is still useful – but its NOT a “causal checklist”!!

Most commonly cuasality is tested through randomized controlled experiements. The goal is a counter-factual- where everything is the same EXCEPT the exposure of interest. 
Assignment of exposure can be random or non-random (think- A/B testing of a website homepage you can make it random or show a certain group a page). Temporatlity is clearly defined and you have an understanding of covariates or cofounders that may contribute to false association.

Most commonly we find an association between two vairables. This means that we observe a correlation between our varibales but we may not fully understand the causal direction or the other factors that may be influencing the association we are observing. 

#### Counfounding 
Often times, the obeservation that we observe may be influenced by another factor.
Let's start with an example. Let's say we did an analysis to understand what causes lung cancer. We find a strong association between carrying cigarette lighters and lung cancer. 

In fact we find, people who carry cigarette lighters are 2.4 times as likely to contract lung cancer as people who don’t carry lighters. 

show smoking-DAG image- Clearly we did not fully understand the relationship of our variables when attempting this analysis. 

#### Real world application
This example highlights a few things. 1) the importance of having deep subject area knowledge so that you can trust that your analysis is logical. You can show a strong association but be totally wrong as in the smoking example and many of the examples we saw at the beginging of the class. 2) That a DAG- Directed acyclic graph can be handy for thinking through the logic of your models 3) the difference between causality and association.

Though it's relatively obivous that there is a flaw in our logic here. It can be tricky when we are working on cuting edge fields or problems where the "truth" isn't readily apparent. Through out the class we will be working on helping you develop your intuition about data, so that you can spot the differences more readily. With this will come a bunch of tools to help you. But keep in mind- the analysis is only as good as your understanding of the problem and the data.

#### Knowledge Check
What is the difference between causality and an association?

<a name="introduction2"></a>
## Introduction: Hypothesis Testing (5 mins)
You'll remember from last time that we worked on descriptive statistics. How would we tell if there is a difference between our groups? How would we know if that difference was real or if our finding is simply due to chance?

For example- if we were working on sales data, how would we know if there was a difference between the buying patterns of men and women at Acme Inc? Hypothesis tesing!

#### Hypothesis testing steps
Generally speaking, you start with a null hypothesis and an alternative hypothesis (that is opposite the null). Then, you check whether the data supports rejecting the null hypothesis or failing to reject the null hypothesis. (Note that "failing to reject" the null is not the same as "accepting" the null hypothesis. The alternative hypothesis may indeed be true, except that you just don't have enough data to show that.)
As it relates to model coefficients, here is the conventional hypothesis test:
null hypothesis: There is no relationship between gender and Sales
alternative hypothesis: There is a relationship between gender and Sales 

<a name="demo"></a>
## Demo: Hypothesis Testing Case Study (30 mins)
use IPYthon Notebook demo-1.ipynb PART 1

#### Check for understanding
What is the null hypothesis? 

<a name="introduction3"></a>
## Validate your fidnings (5 mins)
How do we tell if the association we observed is statistically significant?
Statistical Significance is the likelihood that a result or relationship is caused by something other than mere random chance. Statistical hypothesis testing is traditionally employed to determine if a result is statistically significant or not.

<a name="demo2"></a>
## Demo: P-values, CI in the case study (20 mins)
use IPython Notebook demo-1.ipynb PART 2

#### Check for understanding
What does the 95% CI indicate? 
That if we repeated our analysis 100 times the point estimate we found would be there in 95% of the time. 

<a name="guided-practice"></a>
## Guided Practice (35 min)
For this exercise you will look through a variety of analyses and interpret the findings. 
Use guided-practice.ipynb

<a name="wrapup"></a>
## Project questions (15 mins)
Review projects and any questions from the guided practice.


***

### BEFORE NEXT CLASS
|   |   |
|---|---|
| **HOMEWORK** | TBD |
| **PREWORK**  | TBD  |
| **PROJECT**  | TBD  |

### ADDITIONAL RESOURCES
- see ipython notebook