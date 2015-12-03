# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Final Project, Part 4: Modeling Performance

### PROMPT
**Context & Takeaway:**

Our goals for this project is to develop a working piece that would be shared amongst your peers. Similar to any other technical project, it should surface your work and approach in a human readable format, treating it as well documented work. Think about how your project pushes the reader to ask for more insightful questions, and how it avoids questions like "what does this line of code do?"

From a presentation perspective, this is an exercise to the machine learning application of your data. Then, use this model to display correlations, feature importance, and unexplained variance.

**Goal:** Exploratory dataset analysis 

---

#### Requirements
* Document your research with a summary
* Explain the approach behind the modeling process and the strengths and weaknesses of variables in the process
* Provide insight behind the modeling process and your performance, using cross validation best practices and prediction metrics for your problem (ex, MSE for regression; Accuracy/AUC for classification)
    - There are so many metrics to choose from, be sure the one you use is reasonable for the problem. For example, explain why you might optimize toward recall instead of AUC.
    - Explain how your model performs compared to a dummy model, and the benefit one gains by using your model to solve this problem.
* Build visualizations that best explain outliers and the relationships of your predicted parameter and independent variables.
* Identify areas where new data could help improve the model significantly.

### DELIVERABLES
**Project Requirements & Constraints**

#### Deliverable Title
- **Breakdown:** Breakdown of deliverable requirements:
  - A Jupyter Notebook with code, visualizations, and markdown
  - The summary will effectively summarize your work from your exploratory data analysis. Be brief, but keep in mind an audience that may be unfamiliar with your project and work.
  - Source code that does not get in the way of your notebook deliverable. Move helper functions into a python module and include this module as part of your project deliverable. Consider it like an appendix piece, though unlike an appendix, it'll be necessary for your project to function.
  - Visualizations that showcase the relationship between your y and at least your two strongest variables as determined by some scoring measure (p values and coefficients, gini/entropy, for example)



**Bonus:**
- Many modeling approaches are all about fine-tuning the algorithm parameters and trying to find some value. Show how you optimized this value, and the cost/benefit of doing so?


### TIMELINE
**Deadlines & Due Dates**

| Deadline | Deliverable| Description |
|:-:|---|---|
| Week 4: Lesson 8 | Lightning Presentation  | Present 3 Problem Statements   |
| Week 7: Lesson 14 | Experiment Writeup  |  Research Design Problem Statement & Outline   |
| Week 8: Lesson 16 | Exploratory Analysis  | Dataset Approval and Exploratory Analysis   |
| Week 9: Lesson 18 | Notebook Draft  |  iPython Notebook & Model Draft  |
| Week 10: Lesson 20 | Presentation  | Present Your Final Report   |

---

### EVALUATION
**Guidelines & Rubric** 
Your project will be evaluated by your instructors in the following areas:

1. Identify
2. Acquire
3. Present

**Rubric**: [Link to rubric](#). Based on the requirements, you can earn a maximum of 9 points on this project. Your instructors will score each of your requirements using the scale below:

    Score | Expectations
    ----- | ------------
    **0** | _Incomplete._
    **1** | _Does not meet expectations._
    **2** | _Meets expectations, good job!_
    **3** | _Exceeds expectations, you wonderful creature, you!_

While the overall rubric will serve as a helpful gauge of whether you met project goals, your __specific scores are more important__ since they can help you identify where to focus your efforts in the future!

---

### RESOURCES
**Examples & Suggestions**

#### Starter code
This deliverable will be a combination of the 3rd and 4th class project (modeling and executive summary), but for your personal project. Refer to those resources and feedback provided.

You can find previous General Assembly Presentations and Notebooks at the (GA Gallery)[https://gallery.generalassemb.ly/DS?metro=]

#### Suggested Ways to Get Started

- Two common ways to start models:
    -  the kitchen sink strategy: throw all the variables in and subtract out
    -  single variable strategy (start with the most important variable and slowly add in while paying attention to performance)
    -  it will be worth exploring both to best understand your data and problem. How slow is building and predicting the model with all the variables? How much improvement is made with each variable added?
- Recall that your variables maybe need transformation in order to be most useful.
- Recall that the algorithm used (say, random forest over logistic regression) have different requirements, so one make work better for your data than another.
- Strike a balance between your writing, code, and visual aide. This notebook should feel like a blogpost with some code in it. Force yourself to write and visualize more than you think; it's easier to edit and cut back than to find ways to add more.

### Useful Resources

- [SKLearn's documentation on metrics](http://scikit-learn.org/stable/modules/classes.html)
- [SKLearn's model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html)

---
