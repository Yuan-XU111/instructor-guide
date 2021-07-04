#!/usr/bin/env python
# coding: utf-8

# # Set up a custom judge
# 
# ## Initiative
# 
# Sometimes, the students may be asked to solve some special questions with a limited range of expressions. For example, they may be forbidden from using the "for loop" or "while loop" or something else. In this case, some extra steps are required to be done in the design process.
# 
# Take the following picture as a simple example. It is a problem that only expects students to solve it with the "for loop" method instead of the "while loop" method.
# ![](https://github.com/Yuan-XU111/instructor-guide/blob/master/image/guide2_p1.png?raw=true)
# 
# ## Steps
# 
# ### Select the checkbox called " Customise ", which is in the "CodeRunner question type",  upon the normal problem-designing basis.
# 
# ![](https://github.com/Yuan-XU111/instructor-guide/blob/master/image/guide2_p2.png?raw=true)
# 
# Once you select the "customise" mode, as is shown in the picture above, a new frame called "template" appears, which is used to write a code to check if the student's code fulfills the requirements, and is in a mixture form of python 3 and twig. (Twig is a template language for PHP that inserts the so-called macro programming language, examples for students answer, and test cases, etc.)
# ![](https://github.com/Yuan-XU111/instructor-guide/blob/master/image/guide2_p3.png?raw=true)
# It consists of the student answer (in the first line). It assignment to a local variable containing the student answer which you are to use.It assignment to a separator variable and then for each test case the test code print of a separator. At the same time, you can also click the "Template debugging" button to help you to set up question clearly. 
# 
# ## Write code in "Template".
# ![](https://github.com/Yuan-XU111/instructor-guide/blob/master/image/guide2_p4.png?raw=true)
# 
# Here is an example that only wants students to use the "for loop" method, and the while method is prohibited. A function called visit_While is defined to find while and break the student's function.
# 
# You may modify the code due to the task you want to acheive.
# 
# ## Outcome
# If a student write a right answer, he will get:
# ![](https://github.com/Yuan-XU111/instructor-guide/blob/master/image/guide2_p5.png?raw=true)
# Otherwise, he will get:
# ![](https://github.com/Yuan-XU111/instructor-guide/blob/master/image/guide2_p6.png?raw=true)
