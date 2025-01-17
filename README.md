# Data Analysis Project

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Description](#description)
* [Results](#results)

## Introduction
The project aims to analyze a dataset using exploratory factor analysis. This method is designed with the aim of identifying underlying relationships between measured variables.

## Technologies
Project is created with:
* Python version: 3.7.9
* Pandas package
* Numpy package
* PySide2 package
* Seaborn package
* Matplotlib package
* Factor Analyzer package
* SciPy package
* Sklearn package
* QT Designer
	
## Setup
The only thing you need to run this project is Python 3 (version higher than 3.3).

First, you need to create a clone of the project and navigate into the top level directory. To do this, enter the following commands on your terminal: 
```
git clone https://github.com/TSMadalina/Data-Analysis-Project
cd Data-Analysis-Project
```

Create a virtual environment via the command:

```
python -m venv venv
```

This creates the folder venv/ in your current directory. It will contain the necessary libraries for running the project.
Then, activate the environment with one of the commands below:

```
# On Mac/Linux:
source venv/bin/activate
# On Windows:
call venv\scripts\activate.bat
```

Now execute the following to install the necessary packages:

```
pip install -Ur project\requirements.txt
```

After the installation is done, navigate to the project directory and run the main.py file with the command:

```
cd project
python main.py
```

Please note that the virtual environment must still be active for this to work.


## Description
The variables used in this study contain data about a randomly chosen hotel located in the capital of one of the 80 countries participating in the study and the first review of it collected from TripAdvisor.com. I would like to mention that the rating collected does not define the quality of the country in question, and, as in any other country, there are a multitude of factors that can affect this rating, such as: a dissatisfied customer; the choice of a hotel that did not meet certain criteria and that no longer exists at the moment; the period in which the review was left, etc. The analysis of the factors will be done according to variables related to the hotel and those related to the destination. For the destination analysis, I used variables such as GDP and Hofstede's cultural dimension variables.

## Results 

Heatmap KMO index |  Factor and variables correlogram
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/76962878/203347835-8aa8379b-0199-40ed-adf2-edb3b46358b9.png)  | ![image](https://user-images.githubusercontent.com/76962878/203347984-17f8687b-6c99-4ef2-821c-2f11a2129158.png)

For a more detailed analysis click [here](Project/Analiza.md).




> Source: Radojevic, T., Stanisic, N., & Stanic, N. (2016). Inside the Rating Scores: A Multilevel Analysis of the Factors Influencing Customer Satisfaction in the Hotel Industry. Cornell Hospitality Quarterly. 
Data set: Radojevic, T., Stanisic, N., & Stanic, N. (2016), Inside the Rating Scores: A Multilevel Analysis of the Factors Influencing Customer Satisfaction in the Hotel Industry., Mendeley Data, v1 
[dataset](http://dx.doi.org/10.17632/kwsrxshf9x.1) [research](https://www.researchgate.net/publication/312164283_Inside_the_Rating_Scores_A_Multilevel_Analysis_of_the_Factors_Influencing_Customer_Satisfaction_in_the_Hotel_Industry)
