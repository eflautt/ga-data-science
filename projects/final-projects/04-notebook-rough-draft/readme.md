# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Final Project, Part 4: Modeling Performance

### PROMPT
**Context & Takeaway:**

Our goal for this project is to develop a working draft that could be shared amongst your peers. Similar to any other technical project, it should surface your work and approach in a human readable format. Your project should push the reader to ask for more insightful questions, and avoid issues like, "what does this line of code do?" 

From a presentation perspective, think about the machine learning applications of your data. Use your model to display correlations, feature importance, and unexplained variance. Document your research with a summary, explaining your modeling approach as well as the strengths and weaknesses of any variables in the process. 

You should provide insight into your analysis, using best practices like cross validation or any applicable prediction metrics (ex: MSE for regression; Accuracy/AUC for classification). Remember, there are many metrics to choose from, so be sure to explain why the one you've used is reasonable for your problem. 

Look at how your model performs compared to a dummy model, and articulate the benefit gained by using your specific model to solve this problem. Finally, build visualizations that explain outliers and the relationships of your predicted parameter and independent variables. You might also identify areas where new data could help improve the model in the future.

**Goal:**  An iPython notebook with a “report” of your models

---

### DELIVERABLES
**Project Requirements & Constraints**

#### iPython Report Draft

- **Breakdown:**
  - A Jupyter Notebook with code, visualizations, and markdown
  - The summary will effectively summarize your work from your exploratory data analysis. 
    - Be brief! And keep in mind that your audience may not be familiar with your work!
  - Source code that does not get in the way of your notebook deliverable. Move helper functions into a python module and include this module as part of your project deliverable. Consider it like an appendix piece, though unlike an appendix, it'll be necessary for your project to function.
  - Visualizations that showcase the relationship between your y and at least your two strongest variables as determined by some scoring measure (p values and coefficients, gini/entropy, for example)

- **Submission:**	
  - TBD by instructor.

- **Bonus:**
    - Many modeling approaches are all about fine-tuning the algorithm parameters and trying to find some value. Show how you optimized this value, and the cost/benefit of doing so.


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

1. Mine
2. Refine
3. Build

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

#### Project Tips
- This deliverable combines unit Projects 3 and 4 from earlier in the course; however, now you will be using your own data. Refer to any resources and feedback provided during those projects.

#### Links to Past Projects
- You can find previous General Assembly Presentations and Notebooks at the [GA Gallery](https://gallery.generalassemb.ly/DS?metro=).

#### Suggested Ways to Get Started
- Two common ways to start models:
    -  "Kitchen Sink Strategy": throw all the variables in and subtract them out, one by one.
    -  "Single Variable Strategy": start with the most important variable and slowly add in while paying attention to performance)
        - It will be worth exploring both to understand your data and problem. How slow is building and predicting the model with all the variables? How much improvement is made with each variable added?
- Recall that your variables maybe need transformation in order to be most useful.
- Algorithms have different requirements (say, random forest vs logistic regression), and one may work better for your data than another.
- Strike a balance between writing, code, and visual aids. Your notebook should feel like a blogpost with some code in it. Force yourself to write and visualize more than you think!

### Useful Resources
- [SKLearn's documentation on metrics](http://scikit-learn.org/stable/modules/classes.html)
- [SKLearn's model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html)

---
