# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Data Science Refresh


### Repo Guide

This guide is intended to help create a student-facing repository for your DS instance. This is __not__ the DS instructor curriculum; these are the student-facing materials, which include:
- Lab Startercode & Datasets
- Project Prompts & Rubrics
- Student Resources

NOTE: Instructors should **also** create a local instance of the official instructor-facing curriculum for their own use.

For instructions on how to set up a student-facing GitHub repository for your DS class, please see below.
> __IMPORTANT: Once you are done setting up your repo, please delete or overwrite the contents of this Readme!__

---

## Requirements
* [ ] **Github Usernames**: Before you get started, you should have a list of usernames for all relevant instructors, TA's, and students.
> If they don't already have one, ask them to signup (it's free). 

* [ ] **Basic Github Familiarity**: Here is a [useful tutorial](https://generalassembly.wistia.com/medias/jkrycndgrs) that will teach you how to create an account, install the Github desktop app, and start a repository.

***

## Setting Up Your Student-Facing Repo

In Data Science, we recommend using a student-facing repo to distribute project prompts/rubrics, starter/sample code, and course resources. The instructor should create a student-facing repo for their course by following these steps:

***

## Instructions

1. **Create a new repo.** Create a new repo under the [ga-students org](https://github.com/ga-students).
 > If you don't have access to "ga-students", please email [Zoe](mailto:zoes@generalassemb.ly).

2. Name your repo using the following convention: "DS-City-Instance Number" (i.e. "DS-NYC-3"). 
3. Press the "Download ZIP" button on the right. Download and unzip the .zip file to your computer. 
4. This folder is the local copy of your "DS-City-Instance" repo.
 
 **Checkpoint**: You should now have a blank "DS-City-Instance Number" folder, ready to be filled with class content!

5. Next, go back to github and navigate over to the "DS-Student-Facing-Repo."
6. Once again, press the "Download ZIP" button on the right. Download and unzip.
7. Copy all of the contents from your downloaded "DS-Student-Facing-Repo" folder into your "DS-City-Instance Number" folder.
 
 **Checkpoint**: Your local "DS-City-Instance Number" folder should now contain all the class materials from the student-facing repo. Next you'll need to publish it!

8. Complete the steps outlined in the Github familiarity video from step 1 to push your changes online. You should:
 * [ ] Initialize Git within your "DS-City-Instance" local repo using the Github desktop app or Terminal.
   * In Terminal, you would navigate to your "DS-City-Instance" folder, type `git init` and then `git add .`
 * [ ] Leave a commit message using the Github desktop app or Terminal.
   * In Terminal, you would type `git commit -m "commit message"` with your commit message in quotes.
 * [ ] Finally, commit to master using the Github desktop app or Terminal.
   * In Terminal, you would type `git push origin master`  

 **Checkpoint**: Your "DS-City-Instance" repo should now be live on GitHub, filled with all of the student facing content!

9. Now that you're ready to go, make sure all instructors and TA's have access to the repository. To do this: 
 * [ ] [Create a new team](https://github.com/orgs/ga-students/teams).
 * [ ] Give your team the same name as your repo + the word "Instructors" (i.e. "DS-NYC-3 Instructors"). 
 * [ ] Under "Repositories," add your DS-City-Instance repo by searching for its name in the "Add repositories" field.
 * [ ] Press the "Settings" button on the left and select "Admin Access" so that your instructors can make changes as needed.
 * [ ] Add instructors and TAs to the team.

10. Your team members will automatically recieve an email notification from Github letting them know they've been given access to your repo. You can also send them the link if needed:
 * [ ] Navigate to [https://github.com/ga-students](https://github.com/ga-students) in your web browser
 * [ ] Search for your repo by name in the "Find a repository..." search box
 * [ ] Click on the title for your repo. This is the permalink you can send to instructors and students. 

 **Checkpoint**: Your "DS-City-Instance" repo should now be accessible to your team of instructors and TA's. 

11. Finally, you'll need to repeat most of the process from step 10 for your students:
 * [ ] First, make sure students have created a Github account and submitted their user names. You can do this before or during the first week of class.
 * [ ] Next, create a team for students and title it with your instance (i.e. "DS-NYC-3 Students")
 * [ ] Under "Repositories," add your DS-City-Instance repo by searching for its name in the "Add repositories" field.
 * [ ] Press the "Settings" button on the left and select "Read Access". 
 > _This will keep students from accidentally deleting any of the files in the repo._

12. Before you can add students to your new group, they must first be added to the "ga-students" org.
 * [ ] _Producers will need to add students to this group because instructors may not have the necessary permissions.__ 
 * [ ] Once your students are recognized by the "ga-students" org, add them to your "DS-City-Instance Student" team.

 **Checkpoint**: Ok! Your "DS-City-Instance" repo should now be accessible by students, organized by team. They should be able to read all the files but not edit them. You're all set!

13. One last step! __Instructors should be sure to either delete or overwrite this readme file before giving students access to the repo :)__ 

***

## Benefits
- Students can now use the GitHub desktop app (or Terminal commands) to access all of the materials in the repo, including notes/links, starter code, projects, etc.

- Optionally, instructors can also choose to give students access to submit their project assignments by pull request, which makes it easy for instructors and TA's to leave comments and feedback. 

***

## Additional Resources
- Github has a ton of online resources, and the Desktop app comes with a sample tutorial.
- Both Codecademy and Codeschool offer free Git/Github related walkthroughs.

***

## Questions?
If you have any questions please send them to [the part-time courses email list](mailto:askpart-time@generalassemb.ly).


