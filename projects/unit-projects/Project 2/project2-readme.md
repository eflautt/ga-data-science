# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project #2: Exploratory Analysis

### PROMPT
**Context & Takeaway:**

In this project, you will implement the exploratory analysis plan developed in Project 1. This will lay the groundwork for our our first modeling exercise in Project 3.

Before completing an analysis, it is critical to understand your data. You will need to identify all the biases and variables in your model in order to accurately assess the strengths and limitations of your analysis and predictions.

Following these steps will help you better understand your dataset.

**Goal:** An iPython notebook writeup that provides a dataset overview with visualizations and statistical analysis.

---
### DELIVERABLES
**Project Requirements & Constraints**

#### iPython Notebook Exploratory Analysis
- **Breakdown:**
  - Read in your dataset
  - Determine how many samples are present and ID any missing data
  - Create a table of descriptive statistics for each of the variables (n, mean, median, standard deviation)
  - Describe the distributions of your data
  - Plot box plots for each variable
  - Create a covariance matrix
  - Determine any issues or limitations your analysis may have based on the results of the exploratory analysis

- **Submission:**
    - Instructor TBD 

- **Bonus:**
    - Replace missing values using the median replacement method
    - Log transform data to meet normality requirements
    - Advanced Option: Replace missing values using multiple imputation methods

### TIMELINE
**Deadlines & Due Dates**

| Deadline | Deliverable| Description |
|:-:|---|---|
| Week 3: Lesson 5 | Project 2  | Exploratory Data Analysis   |

---

### EVALUATION
**Guidelines & Rubric** 

Your project will be evaluated by your instructors in the following areas:

1. Parse
2. Mine
3. Refine

#### Rubric: [Link to rubric](#). 

Based on the requirements, you can earn a maximum of 9 points on this project. Your instructors will score each of your technical requirements using the scale below:

    Score | Expectations
    ----- | ------------
    **0** | _Incomplete._
    **1** | _Does not meet expectations._
    **2** | _Meets expectations, good job!_
    **3** | _Exceeds expectations, you wonderful creature, you!_

 This will serve as a helpful overall gauge of whether you met the project goals, but __the more important scores are the individual ones__ above, which can help you identify where to focus your efforts for the next project!

---
### RESOURCES
**Examples & Suggestions**

#### Dataset  
We'll be using the same dataset as UCLA's Logit Regression in R tutorial to explore logistic regression in Python. Our goal will be to identify the various factors that may influence admission into graduate school. It containes four variables- admit, gre, gpa, rank.

- 'admit' is a binary variable. It indicates whether or not a candidate was admitted admit =1) our not (admit= 0)
- 'gre' is GRE score
- 'gpa' stands for Grade Point Average
- 'rank' is the rank of an applicant's undergraduate alma mater, with 1 being the highest and 4 as the lowest

#### Starter code
For this project we will be using an iPython notebook. This notebook will use matplotlib for plotting and visualizing our data. This type of visualization is handy for prototyping and quick data analysis. We will discuss more advanced data visualizations for disseminating your work.

#### Suggested Ways to Get Started
- Read in your dataset
- Try out a few pandas commands for describing your data:
  - '''df['dataframeName'].describe(),'''
  - '''df['columnName'].sum(),'''
  - ''df['columnName'].mean(),'''
  - '''df['columnName'].count(),'''
  - '''df['columnName'].skew(),'''
  - '''df.corr()'''
- **Read the docs for Pandas.** Most of the time, there is a tutorial that you can follow, but not always, and learning to read documentation is crucial to your success as a data scientist.

#### Links to Past Projects
Look at some sample notebooks for an example of the types of visualizations you can use in your notebook.
* [Example Notebook](https://github.com/justmarkham/DAT8/blob/master/notebooks/05_pandas_visualization.ipynb)


#### Useful Resources
- [Pandas Docs](http://pandas.pydata.org/pandas-docs/stable/)
- [Useful Pandas Snippets](https://gist.github.com/bsweger/e5817488d161f37dcbd2)

---

