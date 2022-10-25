# Data Analysis Project

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Description](#description)
* [Results](#results)

## Introduction
The project aims to analyse a dataset using exploratory factor analysis. This method is designed with the aim of identifying underlying relationships between measured variables.

## Technologies
Project is created with:
* Python version: 3.7.9
* Pandas package
* Numpy package
* PySide2 package
* Seaborn package
* Matplotlib library
* Factor Analyzer package
* SciPy statistical functions
* Sklearn.preprocessing package
* QT Designer
	
## Setup
To run this project, please enter the following commands on your terminal:

```
git clone https://github.com/TSMadalina/Data-Analysis-Project
cd Data-Analysis-Project
```

## Description
The variables used in this study contain data about a randomly chosen hotel located in the capital of one of the 80 countries participating in the study and the first review of it collected from TripAdvisor.com. I would like to mention that the rating collected does not define the quality of the country in question, and, as in any other country, there are a multitude of factors that can affect this rating, such as: a dissatisfied customer; the choice of a hotel that did not meet certain criteria and that no longer exists at the moment; the period in which the review was left, etc. The analysis of the factors will be done according to variables related to the hotel and those related to the destination. For the destination analysis, I used variables such as GDP and Hofstede's cultural dimension variables.

## Results 

Heatmap KMO index |  Factor and variables correlogram
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/76962878/190694547-44afdad8-0a1f-42f6-893b-119e24dd443e.png)  | ![image](https://user-images.githubusercontent.com/76962878/190698093-11637218-6c89-4a89-a576-9ee1a3527f3b.png)

For a more detailed analysis click [here](Project/Analiza.md).




> Source: Radojevic, T., Stanisic, N., & Stanic, N. (2016). Inside the Rating Scores: A Multilevel Analysis of the Factors Influencing Customer Satisfaction in the Hotel Industry. Cornell Hospitality Quarterly. 
Data set: Radojevic, T., Stanisic, N., & Stanic, N. (2016), Inside the Rating Scores: A Multilevel Analysis of the Factors Influencing Customer Satisfaction in the Hotel Industry., Mendeley Data, v1 
[dataset](http://dx.doi.org/10.17632/kwsrxshf9x.1) [research](https://www.researchgate.net/publication/312164283_Inside_the_Rating_Scores_A_Multilevel_Analysis_of_the_Factors_Influencing_Customer_Satisfaction_in_the_Hotel_Industry)
