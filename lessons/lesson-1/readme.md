---
title: What is Data Science?
duration: "2:50"
creator:
    name: Amy Roberts 
    city: NYC
---

# Welcome to Data Science 

### Objectives
*After this lesson, students will be able to:*

- Describe the roles of GA staff and students to create a successful learning environment for data science 
- Define data science and the data science workflow
- Apply data science workflow to get to know the class
- Setup your data science development environment and review python basics

### Preparation
*Before this lesson, students should already be able to:*

- Define basic data types used in object-oriented programming
- Recall the Python syntax for lists, dictionaries, and functions
- Create files and navigate directories using the command line interface (for your specific environment)


## Welcome to GA! - Intro (20 mins) 
(See: Day 1 deck from production team)

#### GA is a special learning environment 
- Introduce the instructors, EIRs, Producers
- GA is a global community of individuals empowered to persure the work we love.
- GA Resources- discounts, community events, hub, office hours
- GA feedback loop- exit tickets, mid-course feedback, final feedback

#### Road to Success 
- Emotional cycle of change
- Student learning responsiblity 
- GA graduation requirements
- After GA- build network, find oppurtunities, community, perks
- Q/A


## What is Data Science/ML- Intro (20 mins)
- A set of tools and techniques used to extract useful informaiton from data
- A interdisciplinary, problem-solving oriented subject
- Application of scientific techniques to practical problems

[Data Science venn diagram](src='http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram')


#### Who uses Data Science
- Netflix movie recommendation example
- Amazon "you may also like" example
- Five Thrity Eight- election and sports coverage
- Draft Kings- using data science to predict daily bets
- Google translate and search results
- Ask students if they know of any other examples

#### What are the roles in Data Science?

**Roles:** 
* Data Developer
* Data Researcher
* Data Creative
* Data Businessperson

![Data Science Roles](assets/DataScienceRoles1.jpg)


**Skills:** 
* Business
* ML/Big Data
* Math
* Programming
* Stats

![Data Science Skills](assets/datasci-skills.jpg)

**Break down of skills by role**

![Data Science Skills by Role](assets/datasci-skills-by-role.jpg)

## Baseline Data Science Quiz - 10 Min 
#### Quiz (7 min)
(use a tool such as socrative to allow for real-time interactive results)

1. True or False: Gender (coded: male= 0 female= 1) is a continuous variable
2. 2. Looking at Table.png- BMI is the _____
	* Outcome
	* Predictor
	* Covariate
3. Draw a normal distribution.
4. True/False Linear regression is an unsupervised learning algorithm.
5. What is a hypothesis test? 

### Discuss Results (3 min)

## Data Science Work Flow - Introduction (25 mins)
#### Overview of Steps: 
Throughout the class and for the our projects we will be following a general workflow. This workflow will help you produce reliable and reproducible results.
- Reliable: Findings are accurate
- Reproducible: Others can follow your steps and get the same results. 

The Steps:  
1. Indentify
2. Acquire
3. Parse
4. Mine
5. Refine
6. Build
7. Present

#### Walk through with the Futurama example from Project 1 
##### IDENTIFY: Understand the problem:
Using Planet Express customer data from January 3001-3005, determine how likely previous customers are to request a repeat delivery using demographic information (profession, company size, location) and previous delivery data (days since last delivery, number of total deliveries)

- Identify business/product objectives:
	- Are previous customers are to request a repeat delivery?
- Identify and hypothesize goals and criteria for success:
	- What factors are likely to influence a customer's decision to be reuse Planet Express for Delivery? 
- Create a set of questions for identifying correct data set


##### ACQUIRE: Obtain the data
Ideal data vs. data that is available.
Often times we start by identifing the ideal data we would want for a project. 
During the aquistion phase we will learn about the limitations of the types of data that are available. We have to decide if the limitaions will inhibit our ability to answer our question of interst or if we will can work with what we have to find a resonable and reliable answer. 

Data for this example: demographic information (profession, company size, location) and previous delivery data (days since last delivery, number of total deliveries)

Questions we may ask include:  
- Identifying the “right” data set(s)
- Is there enough data?
- Does it appropriately align with the question/problem statement?
- Can the dataset be trusted?  How was it collected?
- Is this dataset aggregated? Can we use the aggregation or do we need to get it pre-aggregation?
- Assess resources, requirements, assumptions, and constraints 
- Import data from the web (Google Analytics, HTML, XML)
- Import data from a file (CSV, XML, TXT, JSON)
- Import data from a preexisting database (SQL)
- Set up local or remote data structure 
- Determine most appropriate tools to work with data 
- Tool follows the format, size of the dataset 

##### PARSE: Understand the data 
Many times we are given secondary data- or data that was collected previously. In these cases we have to learn as much as possible about our data using tools such a data dictionary and source documentation on how the data was gathered. 

Example data dictionary: 

Variable | Description | Type of Variable
---| ---| ---
Profession |Title of the account owner  | categorical
Company Size | 1- small, 2- medium, 3- large| categorical
Location | planet of the company | categorical 
Days Since Last Delivery | integer | continuous
Number of Deliveries | integer | continuous

**Common questions include:**  
- Read any documentation provided with the data (e.g. data dictionary above)
- Perform exploratory surface analysis via filtering, sorting, and simple visualizations 
- Describe data structure and the information being collected
- Explore variables, data types via select 
- Assess preliminary outliers, trends 
- Verify the quality of the data (feedback loop -> 1)

##### MINE: Prepare, structure, and clean the data  
Often times the our data will need to be cleaned prior preforming the analysis: 

Common steps include:
- Sample the data, determine sampling methodology 
- Iterate and explore outliers, null values via select 
- Intro qualitative vs quantitative data
- Format and clean data in Python (dates, number signs, formatting)
- Define how to appropriately address missing values (cleaning)
- Categorization, manipulation, slicing, format, integrate data
- Format and combining different data points, separate columns, etc. 
- Determine most appropriate aggregations, cleaning, etc. methods
- Create necessary derived columns from the data (new data)

##### REFINE: Exploratory data analysis 
An example of a basic statistics you may check: 

Mean (STD) or frequency counts 

Variable | Mean (STD) or Frequency (%)
---| ---
Number of Deliveries | 50.0 (10)
Earth | 50 (10%)
Amphibios 9 | 100 (20%)
Bogad | 100 (20%)
Colgate 8| 100 (20%) 
Other| 150 (30%)

These descriptive stats allow us to: 

- Identify trends and outliers
- Decide how to deal with outliers - excluding, filtering, and communication
- Apply descriptive and inferential statistics
- Determine initial visualization techniques
- Document and capture knowledge
- Choose visualization techniques for different data types
- Transform data

##### BUILD: Create a data model
We select a model based on the outcome we are intersted in and the assumptions of the model we are using. An example of a model statment may be: 

- We completed a logistic regression using Statsmodels v. XX. We calculated the probability of a customer placing another order with Planet Express.  

In this case we are using a logistic model because this we are determine the probability that a customer may place a return order, which at its heart is a classifcation problem. 

The steps for model building are:  
- Select appropriate model 
- Build model
- Evaluate and refine model
- Predict outcomes, action items 

##### PRESENT: Communicate the results of your analysis  
Presentation is a critical part of your analysis. It doesn't matter how brillant your model is or how illuminating your findings are, if you are not able to effectively communicate your results then it will not be used. 

The most simple form of communication may include a simple sentence that discribes your results: 

- Customers from large companies had 2.0 (CI 1.9, 2.1) the odds of of placing another order with Planet Express compared to customers from small companies. 

While presentations can also be far more complex and exciting, like the embedded maps provided by the NYTimes. 

It is also important to practice your presentation. Find out what questions people have and refine your presentation to clarify any confusing points. A key factor in this is understanding your audience. You would create vastly different presentations for fellow data scientists than you would for executives who are trying to make a business decision. 

Key factors of a good presentation include:  
- Summarize findings with narrative, storytelling techniques 
- Refine visualization for broader comprehension
- Present limitations, assumptions
- Determine degree of disclosure /integrity of analysis
- What should I disclose to stakeholders as part of your analysis?
- Concrete steps for testing evaluating the effectiveness of your presen

##### A Note About Iteration
Iteration is an important part of the Data Science Workflow. At every point in the process, you may find yourself repeating or going back and re-doing elements in order to better understand your data, clarify your model, and refine your presentation.

For example, after presenting your findings, you may want to:

- Identify follow up problems and questions for future analysis
- Create a visually effective summary / report
- Consider different stakeholders, their needs, and how your report might change
- Identify the limitations of your analysis
- Identify relationships between visualizations

## Short version Data Science Work Flow- Application (25 mins)
Use three of the steps from the data science work flow (identify, acquire, present) to get to know your classmates!

Students should get into 4 groups- spaced at the whiteboards around the room. 

#### IDENTIFY: Understand the problem 
Have each group develop 1 research question that they would like to know about the class and make a hypothesis (don't share with class yet)
Examples:
- Current favorite tool for working with data? 
- What can you help your classmates with when it comes to data analysis? 
- What you most excited about learning?

#### ACQUIRE: Obtain the data 
Have students rotate through the groups to "collect the data" (suggest students make a easy visual way for the other students to write their answers, or select an option quickly to keep the time on this down)
Record raw data on white boards.

#### PRESENT: Communicate the results of your analysis  
- Summarize findings with narrative
- Provide a basic visualization for broader comprehension on white board
- Have one student present for the group


## Dev environment setup (65 min)
* Brief intro to the tools we will use as a data sciencist- (detailed overview in lesson 2) 
* Workshop to help with environment set up 
* IPython Notebook to test set and complete Python Review

## Conclusion (5 mins)
- What is data science?
- What is the data science workflow?
- How can you have a successfull learning experience at GA?
