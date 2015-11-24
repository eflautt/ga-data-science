# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project #2: Exploratory analysis (without models)

#### Overview
In this second project you will implement the exploratory analysis plan your developed in the first project. This will lay the groundwork for our our first modeling exercise in project 3. Before completing any analysis it is critical to understand your data. In order to accurately identify biases, limitations of your analysis and the strengths of your predictions you must understand each variable in your model. This steps will help you understand your dataset. 

---
#### Requirements
- Read in your dataset
- Determine how many samples are present and id any missing data
- Create a table of discriptive statistics for each of the variables (n, mean, median, standard deviation)
- Describe the distributions of your data 
- Plot box plots for each variable 
- Create a covariance matrix 
- Determine any issues or limitations your analysis may have based on the results of the exploratory analysis 


**Bonus:**

- Replace missing values using median replacement method
- Log transform data to meet normality requirements
- Advanced- Repleace missing values using multiple imputation methods

---

#### Necessary Deliverables

- Completed IPython Notebook

---
#### Dataset  
We'll be using the same dataset as UCLA's Logit Regression in R tutorial to explore logistic regression in Python. Our goal will be to identify the various factors that may influence admission into graduate school. It containes four variables- admit, gre, gpa, rank. 

admit- is a binary variable. It indicates whether or not a candidate was admitted admit =1) our not (admit= 0)

gre- gre score

gpa- grade point average 

rank- rank of an applicant's undergraduate alma mater with 1 being a high rank and 4 being the lowest rank


#### Starter code

For this project we will be using an IPython notebook. This notebook will use matplotlib for plotting and visualizing our data. This type of visualization is handy for prototyping and quick data analysis. We will discuss more advanced data visualizations for disseminating your work. 

#### Suggested Ways to Get Started

- Read in your dataset
- Try out a few pandas commands for describing your data. 
df['dataframeName'].describe(), df['columnName'].sum(), df['columnName'].mean(), df['columnName'].count(), df['columnName'].skew(), df.corr()
- Read the docs for Pandas.** Most of the time, there is a tutorial that you can follow, but not always, and learning to read documentation is crucial to your success as a data scientist

---

### Useful Resources

- A link to [Pandas Docs](http://pandas.pydata.org/pandas-docs/stable/)
- Extra relevant [Useful Pandas Snippets](https://gist.github.com/bsweger/e5817488d161f37dcbd2)

---

#### Deliverable
Checkout this example notebook for an example of the types of visualizations we will look for in your notebook. 

![Example Notebook](https://cloud.githubusercontent.com/assets/25366/8370438/dd651c2c-1b7c-11e5-8638-c99e2f6c7c61.png)

#### Project Feedback + Evaluation


Based on the requirements you can earn a maximum of 3 points on this project. Your instructors will score each of your technical requirements using the scale below:

    Score | Expectations
    ----- | ------------
    **0** | _Incomplete._
    **1** | _Does not meet expectations._
    **2** | _Meets expectations, good job!_
    **3** | _Exceeds expectations, you wonderful creature, you!_

 This will serve as a helpful overall gauge of whether you met the project goals, but __the more important scores are the individual ones__ above, which can help you identify where to focus your efforts for the next project!
