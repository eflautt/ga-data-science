---
title: Experimental Design and Pandas
duration: "1:45"
creator:
    name: Amy Roberts, Lab/Codealong from GADS11
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Experimental Design and Pandas
Week # | Lesson #

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Define a problem and types of data
- Identify data set types
- Define the data science workflow
- Apply the data science workflow in the pandas context
- Write an IPython Notebook to import, format and clean data using the Pandas Library

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
| 10 min  | [Introduction](#introduction1)   | The why's and how's of a good question |
| 10 min  | [Demo](#demo1)  | Diagraming a high quality aim |
| 10 min  | [Lecture](#lecture1)  | Types of datasets |
| 10 min  | [Guided Practice](#guidedpractice)  | Write a research question with raw data
  |
| 5 min  | [Review](#review1)  | Section 1 Review |
| 5 min  | [Introduction](#introduction2)   | Datascience workflow steps 2. Acquire and 3. Parse |
| 10 min  | [Demo](#demo2)   | Walkthrough Acquire and Parse with Pandas |
| 30 min  | [Codealong](#codealong)  | Pandas Intro |
| 5 min  | [Introduction](#introduction3)  | Lab Walkthrough  |
| 20 min  | [Independent Practice](#lab)  | Lesson 2 lab |
| 10 min  | [Conclusion](#conclusion)  | Review lab and lesson objectives |
| 15 min  | [Wrap-up](#wrapup)  | Unit 1, project, where we're headed |

---
<a name="opening"></a>
## Opening (5 min)
- Review Current Lesson Objectives
    - Review Data Science workflow
    1. Identify
    2. Acquire
    3. Parse
    4. Mine
    5. Refine
    6. Build 
    7. Present 

  Today we will focus on steps 1-2, we will dive into steps 3-5 in the next few classes.



<a name="introduction"></a>
## Intro: The why's and how's of a good question (10 mins)

#### Why we need a good question/aim
"A problem well stated is half solved."

By having a high quality question/aim you set yourself up for success as you being your analysis. You also establish the basis for making your analysis reproducible. A clearly articulated research question not only helps other data scientists learn from, and reproduce your work, but also helps them expand on your work in the future. 

#### What is a good question? 
The goals of a high quality, reproducible question are similar to the SMART Goals Framework. 
S- specific 
M- measureable
A- attainable
R- reproducible *this step is different from smart goals*
T- timebound

1. Specific- The dataset and key variables are clearly defined. 
2. Measureable- The the type of anlysis and major assumptions are articulated. 
3. Attainable- The question you are asking is feasible for your dataset and is not likely to be biased.
4. Reproducible- Another person (or you in 6 months!) can read your state and understand exactly how the analysis is being preformed
5. Timebound- You clearly state the time period and population for which this analysis will pertain

<a name="demo1"></a>
## Demo: Diagraming an aim (5 mins)
Example aim: 
Determine the association of foods in the home with child dietary intake. Using one 24-hour recall from tbe cross-sectional NHANES 2007-2010 we will determine the factors associated with food available in the homes of American children and adolescents. We will test if reported availability of fruits, dark green vegetables, low fat milk or sugar sweetened beverages available in the home increases the likelihood that children and adolescents will meet their USDA recommended dietary intake for that food. Hypothesis: Children will be more likely to meet their recommended intake level when a food is always available in their home compared to rarely of never. (From Dr. Amy Roberts' Dissertation)

Note for each of these give one 1 example and ask the class to id others.  

1. Specific: Using **one 24-hour recall** from the cross-sectional National Health and Nutrition Examination Survey (NHANES) 2007-2010 we will determine the factors associated with food available in the homes of **American children and adolescents**. We will test if **self-reported availability of fruits, dark green vegetables, low fat milk or sugar sweetened beverages available in the home increases** the likelihood that children and adolescents will meet their **USDA recommended dietary intake** for that food. Hypothesis: Children will be **more likely to meet their recommended intake level when a food is always available in their home compared to rarely of never**.

How data was collected is indicated: 24-hour recall, self-reported

What data was collected is indicated: fruits, dark green vegetables, low fat milk or sugar sweetened beverages, always vs rarely never available

How the data will be analysised- using USDA recommendations as a gold-standard to measure the association

The specific hypothesis along with the direction of the expected association: more likely to meet their recommended intake level


2. Measureable: Determine the association of foods in the home with child dietary intake. We will test if reported availability of fruits, dark green vegetables, low fat milk or sugar sweetened beverages available in the home increases the likelihood that children and adolescents will meet their USDA recommended dietary intake for that food. 

3. Attainable: Cross-sectional data has specific limitations- one of the most common is that causal inference is typically not possible. Note that we are determining the association between two items (food available in the home and children meeting their dietary recommendations). Because we are using cross-sectional data we cannot say that having fruits and vegetables in the home causes children to meet their dietary requirments. 

4. Reproducible: By having all the specifics we indicated previously it would be straight forward to Google NHANES pull the right datasets and reproduce this work. 

5. Time Bound: Using one 24-hour recall from **NHANES 2007-2010** we will determine the factors associated with food available in the homes of **American children and adolescents**.
Trends often change over time and vary by the population or source of your data. It is important to clearly define who/what you included in your anaylsis and the time period for the analysis.


#### Context 
Depending on your setting the types of questoins you will answer may vary. The previous example is from a research setting. In a business setting you will need to clearly articulate the business objectives. Id and hhypothesize goals and criteria for success (e.g., success for the Netflix recommendation engine may be if 70% of customers over the age of 18 select a movie from the recommended queue during Q3 of 2015). Regardless of the setting it is important that you state your question following the SMART framework. 

## Why dataset types matter. 
As we saw in the attainable section above, different types of data have set limitations and strengths. As such certain types of analysis will not be possible with certain datasets. We are going to do a breif overview of the different types of datasets here. 

Cross-sectional data: All information is determined at the same time. In other words the data is all coming from the same time period. 

Things to consider: 
TEMPORALITY 

No distinction between exposure and outcome-- e.g. why in the example above we can't say that the availability of fruit in the home caused children to meet their recommendations. It is just as likely that the opposite is true. 

**Strengths**
often population based  
generalizability   
reduced cost compared to other types of data collection methods

**Weaknesses** 
separation of cause and effect may be difficult or impossible
Variables/Cases with long duration are over-represented 

Time-Series/Longitudional data: The information (data) is collected over a period of time. 

**Strengths**
Unambiguous temporal sequence – exposure precedes outcome
Multiple outcomes can be measured

**Limitations**
Expense
Takes a long time
Vulnerable to missing data 


<a name="#guidedpractice"></a>
## Guided Practice: Write a research question with raw data (10 mins)
Looking at the data from Kaggle's Titanic competition, let's write a high quality reserch question 
[data dictionary](href='https://www.kaggle.com/c/titanic/data')
Format: Think, Pair, Share

1. What type of data is this cross-sectional or longitudinal? 

cross-sectional

2. What will be measuring (hint: look back at the previous example)

The association between being a woman or a child and survival on the Titanic.

3. Write a SMART aim 

Using data from April 15, 1912, taken from  the Titanic diaster, we will determine the association of gender, age (in years) and survival. 

<a name="review1"></a>
We covered the Identify step of the data science workflow. We also explored the strengths and weaknesses of two types of data.

1. SMART analysis aims 
2. Types of a datasets

Questions? 

<a name="introduction2")></a>   |
## Datascience workflow steps 2. Acquire and 3. Parse (5 mins)
During this section we are going to walk through a the key features of steps 2 & 3 of the data science workflow. We will be working with an IPython Notebook. I'll demo the steps frist, then we will try them together. During the last part of class you will try your hand at the steps individually. 

<a name="demo2"></a>
## Demo: Walkthrough Acquire and Parse with Pandas (30 mins)

#### Acquire
You'll remember from the previous class that the aquire step is where we determine if the dataset we have it the "right" dataset for our question. One factor is what type of data is it? Cross-sectional? Longitudinal/Time Series? The next question is how well was the data collected? Does it have a ton of missing data? Was the instrument used to collect the data validated and reliable? Is this dataset aggregated? Can we use the aggregation or do we need to get it pre-aggregation?

#### Intro to data dictionaries and documentation (part of Parse step as well)
This is often our primary souce to help you judege the quality of your data and also to understand how it is coded. Your gender variable is coded 0 and 1. How do you know which is male and which is female? Your data dictionary! Is your currency varibale in dollars or euros? Data dictionary! 

Show a few examples from Kaggle pages or your own work (i.e. the Titanic basic one from above to any one of the many more elaborate ones).

This is also where you will find out info on any requirements, assumptions, and constraints of your data. Through you should never assume that the data dictionary is complete. Is it often up to you to test your assumptions. 

#### Logistics of aquiring your data 
You can access data through a variety of different methods including: 
1. Web (Google Analytics, HTML, XML)
2. File (CSV, XML, TXT, JSON)
3. Preexisting database (SQL, no-sql)

Today will be using a CSV (comma separted value) file in the lab. 

#### Parse- understanding your data
Perform exploratory surface analysis via filtering, sorting, and simple visualizations 
Describe data structure and the information being collected
Explore variables, data types via select 



<a name="codealong"></a>
## Codealong- Pandas intro (30 minutes)
See labs/lesson2_numpy_and_pandas.ipynb

<a name="introduction3"></a>
## Lab walk through (5 min)
This is lab is based on a quiz given in Roger Peng Coursera class Computing for Data Analysis. During the lab you will read in and merge two datasets "ozone" and "data". By the end of the lab you will:
1. Merge datasets
2. Check basic fetures- column names, number of observations
3. Find and drop missing values
4. Find basic stats mean, max (more on these next time!)


<a name="lab"></a>
## Lesson 2 Lab (20 min)


<a name="conclusion"></a>
## Conclusion (10 mins)
- Review questions from lab
- Review objectives from class 

<a name="wrapup"></a>
## Unit 1, project, where we're headed (15 mins)
- Review Unit 1 objectives
- Introduce the first project
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