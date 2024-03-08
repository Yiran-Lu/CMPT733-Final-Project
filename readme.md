# CMPT733 Final Project


#### <span style="text-decoration:underline;">Brian Zhou, Juanwei Hu, Yiran Lu, Sandy Deng</span> 


## 1. Research questions


### **List 3 <span style="text-decoration:underline;">questions</span> that you intend to answer (1 point)**

Detail each research question you intend to answer.



* What time of the year do students experience the most stress/anxiety?
* Do exams/deadlines affect student’s mental health?
* Does holidays/spring break improve student’s mental health?


## 2. Dataset utilization


### **List <span style="text-decoration:underline;">all the datasets</span> you intend to use (1 point)**



1. Kaggle Mental Health datasets
    1. [https://www.kaggle.com/datasets/thedevastator/nlp-mental-health-conversations](https://www.kaggle.com/datasets/thedevastator/nlp-mental-health-conversations)
    2. [https://www.kaggle.com/datasets/mdismielhossenabir/psychosocial-mental-health-analysis](https://www.kaggle.com/datasets/mdismielhossenabir/psychosocial-mental-health-analysis)
    3. [https://www.kaggle.com/datasets/kreeshrajani/human-stress-prediction/data?select=Stress.csv](https://www.kaggle.com/datasets/kreeshrajani/human-stress-prediction/data?select=Stress.csv)
    4. ..and more
2. Scraping relevant subreddits on Reddit.
    1. [https://www.reddit.com/r/Anxiety/](https://www.reddit.com/r/Anxiety/)
    2. https://www.reddit.com/r/mentalhealth/
3. Social media in general: Twitter/Reddit/Instagram..etc


## 3. Methodology


### **Give us a rough idea on how you plan to use the datasets to answer these questions. (2 points)**



* <span style="text-decoration:underline;">Data Collection:</span> Retrieving data from Kaggle, scraping from Reddit, utilizing Reddit API, scraping from social media
* <span style="text-decoration:underline;">Data Exploration:</span> We do need to perform EDA, as a method to remove outliers and anomalies
* <span style="text-decoration:underline;">Data Cleaning:</span> Yes, data cleaning is necessary. Scrapped data contains noise which needs to be cleaned and removed.
* <span style="text-decoration:underline;">Data Integration:</span> Data integration is necessary because we will be using scraped data and pre-made datasets.
* <span style="text-decoration:underline;">Data Analysis:</span> We intend to use machine learning and NLP to analyze our data. We plan to set a confidence interval to evaluate our analysis results.  \
<span style="text-decoration:underline;">Data Product:</span> Interactive Visualization


## 4. Expected impact


### The completion of this project is anticipated to have a significant impact on understanding the dynamics of student mental health throughout the academic year, specifically about stress, anxiety, and the effects of academic pressures versus breaks. The greatest impact of this study could be the development of a comprehensive understanding of when students are most vulnerable to stress and anxiety and the identification of potential periods of relief. We can then use these findings to better provide mental health support to students.


## 5. Potential challenges


### **Identify any anticipated obstacles and how you plan to address them. (1 point)**



1. We might encounter issues related to scraping. Social media platforms like Twitter have implemented strict limits on scraping, which we might need to find a way to get around it. If necessary, we can pay a small fee to utilize different social media’s official API to gather data.
2. Data quality might be a concern. Posts on subreddits like r/anxiety may not always be related to stress, there's also the risk of encountering off-topic posts or spam. To combat this, we might need to manually label data, or use other metrics such as upvote count to determine if the data is relevant or not.
