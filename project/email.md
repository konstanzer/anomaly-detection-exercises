Hello Zach,

I looked at that student logs data. I was successful in finding some answers using a combination of visualizations and z-scores. I've attached as a summary slide as both a png file and a powerpoint. In the slide, I chose an objective focusing on student interaction with curriculum with the long-term goal of increasing student engagement. Of course, you may tailor this objective as you see fit. As for the original questions, these are my best guesses. 

1. Which lessons appear to attract the most traffic consistently across cohorts (per program)?
Data science: 1. Fundamentals, 2. Classification, 3. Regression
Web development (Java + PHP): 1. Javascript-I, 2. Spring, 3. HTML-CSS
2. Which lessons are least accessed?
Data science: 1. Acquire, 2. Dataframes, 3. Distributed-ML
Web development (Java + PHP): 1. JSP+JSTL, 2. Fundamentals, 3. Web design
3. Is there a cohort that referred to a lesson significantly more than other cohorts?
Java: Oberon: Javascript-I, Java-I, Neptune: HTML-CSS, Marco: jQuery, Niagara: Spring, Appendix
PHP: Franklin: Java-III, Javascript-II, Hampton: Prework, Java-I, Java-II
4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
Data science: 1. Fundamentals, 2. Classification
Web development (Java + PHP): 1. Spring, 2. Javascript-I
5. Is there any suspicious activity like scraping? Who are the illicit users/bots accessing the curriculum?
192.171.117.210 is abnormally active throughout log but I suspect it's an admin
12.106.208.194 accessed material 3,300 times in three weeks, March 2020

My notebook is available here:
https://github.com/konstanzer/anomaly-detection-exercises/blob/master/project/curriculum-logs.ipynb
Prepare and acquire files can also be found in the repo. I spent a lot of time isolating the home directory in the path to reprsent actual lessons. Maybe this cleaning work will be of some use to you.

Good luck with your presentation.

From,

Steven