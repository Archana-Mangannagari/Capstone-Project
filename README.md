# Capstone-Project

## An Evaluation of Strategies Using NLP and Machine Learning To Detect Fraudulent Job Postings

This project is a part of the ADS-599B course in the Applied Data Science Program at the University of San Diego. 

-- Project Status: [Completed]


# Installation

To use this project, first clone the repo on your device using the command below:

git init

git clone https: git clone https://github.com/sindhubhattarai/Capstone-Project.git

To install the dependacies currently used for this project 
Refer to the Other Materials Folder

pip install -r requirements.txt


# Abstract

The technological reliance on social communication has impacted the job market in advertising job vacancies. Fake job listings have been a growing trend to scam job seekers for staggering time for click revenue, extorted with fake application fees, and selling personal information. To help limit the growth of fake postings, this paper proposes a methodology that uses Natural Language Processing and supervised machine learning techniques to detect whether a job posting is legitimate. Feature extraction like term frequency-inverse document frequency (TF-IDF) and Bag-of-Words (BoW) are applied to find keywords associated with fake postings. After extracting the key words, six machine learning models are applied: k-Nearest Neighbor (k-NN), logistic regression, support vector  machine, Naïve Bayes classifier, random forest classifier, and multilayer perceptron. Automatic fake post detection is a challenging problem to solve due to its statistical limitation in the real world. The primary limitation is the lack of a labeled dataset due to the lack of enough fake posts. The models consist of 18,000 records to learn from and have the challenge of imbalanced data due to only having 800 records of false reports. To compensate, multiple sampling techniques were implemented, but the best technique was using the Adaptive Synthetic ADASYN. 

# Project Introduction and Background

Fake news has existed for a very long time, nearly the same amount of time as news began to circulate during  the Gutenberg printing press that was invented in 1439 (ICFJ, 2018). However, the  term “fake news” has no singular definition that is agreed upon. Recent progress in natural language generation has raised dual-use concerns in distinguishing real from fake posts. While applications like sumarization and translation are positive, the underlying technology also might enable adversaries to generate fake posts as click bait or misguide the public. Almost 38% of adults consume news from online platforms (Mitchell, 2020). People can propagate a simple line of fake conspiracies and advertising through online platforms and manipulate the thoughts of people. Spreading fake news and click bait has become a new business in the digital world. The simple clicks  on these a digital platform can have a harmful effect for users finances, trust of doing buiness on the platform, and prone to have personal information resold.

# Problem Statement

Deception of information has traversed multiple social mediums, including the internet. Clickbait are postings that are designed to attract the attention of a user who, upon clicking on a link, is directed to a web page whose content is considerably below their expectations. The societal system and individual belief can be easily manipulated through false information. This can encourage violence, prejudices which can be harmful, systemic bias, false hopes, ignorance towards real news and misjudgement (Bhattarai, 2022). Not only general people but companies website will also be affected due to the spread of fake news and clickbait . The websites will lose the credibility of the information they provide. By applying machine learning classification to predict the chance of a fraudulent posting, candidates will have a better chance to make informed decisions to decide whether to commit to a job post.


# Contributor

## Team 9 Members:

* Sindhu Bhattarai

* Sean Torres


# Technologies 
## Languages

* Python

## Platform

* Jupyter Notebook

* Git-Hub


# Data Acquisition

https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction

Contains: 18 features 

18 thousand jobs posts are recorded with 800 of them being fake.The data consists of both textual information and meta-information about the jobs. The data set can be used to create classification models which can learn the job descriptions which are fraudulent.


# Methods Used

*	Data Mining 
*	Machine Learning
*	Programming 
*	NLP
*	Data Manipulation
*	Data Visualization
*	Data Engineering


# Approach 

## Data Preparation and Cleaning 

![alt text](https://github.com/sindhubhattarai/Capstone-Project/blob/master/Image%20Folder/data_preparation.png)

## Sampling Techniques

* Random Up Sampling
* Random Down Sampling 
* ADASYN Upsampling 

## Feature Engineering techniques 

* BoW Vectorizer 
* TF-IDF Vectorizer

## Machine Learning Models 

* Logistic Regression
* Random Forest
* k-NN
* Multilayer Perceptron 
* Support Vector Machine 
* Naive Bayes 


# Conclusion

The feature extraction TF-IDF and BoW were used in tandem with the ADASYN oversampling technique to help improve accuracy for all models. The likelihood of working with imbalance data is very common with this dataset which heavily relies on oversampling techniques with feature extraction. The highest accuracy score was the support vector machine with the ADASYN algorithm and TF-IDF at 100%. Majority of the poor performance was due to the minority class causing over-fitting no matter how the data was sampled. The over-fitting also had a detriment on the scores of precision and Recall. When comparing the basic models to deep learning there was very little difference within the results. 

# Acknowledgements
The University of the Aegean | Laboratory of Information & Communication Systems Security
http://emscad.samos.aegean.gr/

# License
CC0: Public Domain


# References

Amaar, A. (2022, January 4). Detection of fake job postings by utilizing machine learning and natural language processing approaches. SpringerLink. https://link.springer.com/article/10.1007/s11063-021-10727-z?error=cookies_not_supported&code=b16269eb-5ac0-4579-8643-eaa0a3f9be9a

Bhattarai, B., Granmo, O., & Jiao, L. (2020). Explainable Tsetlin Machine Framework for Fake News Detection with Credibility Score Assessment. https://aclanthology.org/2022.lrec-1.523.pdf

Baraneetharan, E. (2022). Detection of fake job advertisements using machine learning algorithms. Journal of Artificial Intelligence, 4(3), 200–210. https://irojournals.com/aicn/V4/I3/06.pdf

Habiba, S. U., Islam, M. K., & Tasnim, F. (2021, January 7). A comparative study on fake job post prediction using different data mining techniques. 2nd International Conference on Robotics, Electrical and Signal Processing Techniques (ICREST), pp. 543-546 https://doi.org/10.1109/ICREST51555.2021.9331230

Posetti, J. & Matthews A. (2018, July 23). A short guide to the history of ‘fake news’ and disinformation: A new ICFJ learning module. International Center for Journalists. https://www.icfj.org/news/short-guide-history-fake-news-and-disinformation-new-icfj-learning-module

Mitchell, A., Gottfried, J., & Shearer, E. (2020, August 27). 1. Pathways to news. Pew Research Center’s Journalism Project. https://www.pewresearch.org/journalism/2016/07/07/pathways-to-news/

O. Nindyati and I. G. Bagus Baskara Nugraha (2019, November 20). Detecting scam in online job vacancy using Behavioral Features Extraction. https://ieeexplore.ieee.org/document/8969842

Okolie, U. C. (2017). E-recruitment: Practices, opportunities and challenges. European Journal of Business and Management,9(11). https://www.iiste.org/Journals/index.php/EJBM/article/view/36399


Qaiser, S., & Ali, R. (2018). Text mining: Use of TF-IDF to examine the relevance of words to documents. International Journal of Computer Applications. 10.5120/ijca2018917395

Turki, T. (2022, June 29). Novel hate speech detection using word cloud visualization and ensemble learning coupled with count vectorizer. MDPI. https://www.mdpi.com/2076-3417/12/13/6611

Wang, L., Han, M., Li, X., Zhang, N., & Cheng, H. (2021). Review of classification methods on unbalanced data sets. IEEE Access, 9, 64606-64628.

Zimdars, M. (2016). My “fake news list” went viral. But made-up stories are only part of the problem. Washington Post. https://www.washingtonpost.com/posteverything/wp/2016/11/18/my-fake-news-list-went-viral-but-made-up-stories-are-only-part-of-the-problem/




"# Capstone-Project" 
