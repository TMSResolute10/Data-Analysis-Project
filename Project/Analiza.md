## Study description

The dataset of the following study was extracted over a long period of time, but for the sake of simplicity, the majority of the factors are from 2010. The variables give information about a randomly selected hotel located in the capital of one of the 80 countries taking part in the study, as well as the first review of the hotel obtained from TripAdvisor.com. I would like to emphasize that the rating collected does not define the quality of the country in question, and that, as in any other country, a variety of factors can influence this rating, such as: a dissatisfied customer; the hotel chosen did not meet certain criteria and no longer exists at the moment; the period in which the review was left; and so on.

The factor analysis will be conducted based on the hotel and destination variables. The former has already been discussed in the paragraph above, thus in this section I will present the destination analysis, in which I will use factors such as GDP and Hofstede's cultural dimension variables.

Hofstede's variables indicate how a society's culture affects its values and how these values influence behavior. The variables are also part of the same-named theory, which is derived from factor analysis. Hofstede's model consists of six dimensions represented by: power distance index; individualism versus collectivism; masculinity versus femininity; uncertainty avoidance index; long-term versus short-term orientation; indulgence versus restraint. I'll go over each variable in more depth below.

**The power distance index (PDI)** measures how a society manages inequalities between people. People in societies with a high index embrace a hierarchical structure in which everyone has their own place. On the other hand, in societies with a low index, people aim to equalize power distribution.

**Individualism (IDV)** is common in societies where interpersonal bonds are weak and everyone is concerned primarily with themselves or their families. Individualistic societies might appear cold, whether due to the climate, the wide structure of towns, or reserved interactions between individuals.

**Masculinity (MAS)** is a society's predisposition for success, heroism, assertiveness, and material rewards. Femininity, on the other hand, demonstrates a tendency for cooperation, modesty, and concern for the weak.

The level to which people of a society feel intimidated by uncertainty, ambiguity, and unexpected situations is expressed by **uncertainty avoidance (UAI)**. Countries with a high index will not accept unconventional ideas or behavior. Countries with a low index, on the contrary, have a more relaxed attitude, aim to avoid conflict, and seek security through rules.

**Long-term orientation (LTO)** refers to a culture's attachment to the past as well as its acceptance of the future. Low-level societies value tradition and find it difficult to accept change, whereas high-level cultures encourage thrift and endeavors toward contemporary education as a means of preparing for the future.

**Indulgence (IVR)** describes a society's tendency to allow relatively unrestricted satisfaction of basic and natural human needs related to people's desire to enjoy life and have fun. Restraint, on the other hand, indicates a culture that suppresses these urges and replaces them with rigid social standards.

These observations are represented by a number of 80 countries considered some of the world's top urban tourist destinations.


![image](https://user-images.githubusercontent.com/76962878/194765470-158fa244-5021-4d90-8407-b8ce20d1a6e6.png)
 
>Figure 1: Countries included in the study (black on the map)

## Exploratory factor analysis (EFA)
I'll apply exploratory factor analysis to analyze the dataset. This method is designed with the aim of identifying the underlying relationships between the measured variables. It helps to interpret the data by minimazing the number of variables before building the analysis model. It will also calculates the maximum common variance of all variables and combines them into a common score.

This analysis, as the name implies, is used to explore factors that influence a specific section, rate, country, etc. As a result, my goal will be to conduct a study that will eventually indicate whether or not the selected factors cause variation in customer satisfaction in the hotel business.

For the initial data modeling, a correlogram will be created using all of the variables to determine which are not relevant for the ongoing analysis or if the variables have an excessively strong correlation with one another.

I selected exploratory factor analysis for this study since the model is considerably more conceptual than other methods and allows for latent variables (so-called factors). In the chosen field of study - customer satisfaction in the hospitality industry - understanding how different factors influence the variation between variables and whether they produce an increase or decrease in satisfaction is essential, which is why an analysis such as EFA is far more engaging than another.

## Results

* ### KMO index correlation matrix

![image](https://user-images.githubusercontent.com/76962878/194668085-c6b8a25e-8718-4928-831f-d29ee224812f.png)

>Figure 2: KMO index heatmap

The factorability of the main values can be determined using the correlogram of the KMO indices. The diagram's high values (over 0.6 - displayed by dark blue) indicate the presence of a strong correlation between the values tested. For example, I can state that the vast majority of my factors (13 in total) have the potential to become main factors in the study.

One of the strongest correlations is seen in the sleep quality rating for the hotels investigated. According to this, a guest's pleasure appears to be strongly related to the level of comfort and relaxation they experience in the country they visit. On the other hand, the GDP value as well as the PDI index ("power distance") play an equally vital role in the final rating given to the hotel, and thus in customer satisfaction. A high GDP can indicate that the country visited is one of the top choices for travellers, as tourism plays a very important role in a country's economy. The PDI index measures tourists' inclination to consider a country's administration and political issues before deciding whether or not to visit that country. Thus, the high value demonstrates how a country's instability and the way it prioritizes equality among people can damage its tourism industry.

* ### Factor variance
![image](https://user-images.githubusercontent.com/76962878/194765485-a282cfa8-3c7c-4e2a-ba44-93e041ea43cc.png)


>Figure 3: Factor variance table

To determine how many factors are required for the analysis, I will examine the eigenvalues, which show how much of the variance in the variables is explained by each factor. For example, the variance of the first factor is 3.7, implying that the factor can explain the variance of 3.7 variables.

The Bartlett test will be used to estimate the number of factors. I will accept as factors those variances at a higher level than the test result. The Bartlett test analyzes the null hypothesis, which evaluates whether the correlation matrix is identical, implying that there is no association between the variables.

To reject the null hypothesis, I need to prove that the statistical p-value is less than 0.05, showing that there is a 95% confidence level correlation between variables.

The weights reflect the percentage of variance covered of the overall variation for each value. The cumulative weights add all the weights together to determine which components are eligible for analysis.
 
 ![image](https://user-images.githubusercontent.com/76962878/190700021-6ba37b73-415e-492b-83af-d28753c0e959.png)

>Figure 4: Variance plot

I have 4 components with variance greater than 1, according to the Kaiser criterion (indicated in green in Figure 4). There are also 4 according to the Cattell criterion, but it was calculated differently: the variance loss of component 5 when compared to component 4 is greater than the variance loss of component 4 when compared to component 3. Because these two criteria are utilized for principal component analysis rather than factor analysis, I will stop using the Bartlett test to determine the number of factors in component 10.

* ### Factor analysis and correlogram
 ![image](https://user-images.githubusercontent.com/76962878/190700038-d18074fd-4da9-497d-afb4-cb260e3f9988.png)

>Figure 5: Correlogram between variables and factors

The correlation coefficients between the main variables and the 10 factors are shown in Figure 5. For the first factor, I can see a strong correlation with anything associated to the hotel's rating.

There are two types of rating criteria: subjective and objective. The subjective factors include value, sleep quality, and service, whereas the objective criteria, which are prominent, are location and room. Cleanliness is considered both subjective and objective.

This first factor indicates the causes of consumer satisfaction in hotels; thus, I can classify it as the level of customer comfort.

The biggest value obtained for the second factor is in GDP and the country's individualism variable. If the first factor focuses on the hotel, for the second one the emphasis is placed on the country and its economy as a determining factor for tourist satisfaction. For this study, I am examining developed economies with a high rate of tourists. At the same time, the presence of individualism indicates a visitor preference for less friendly countries. Perhaps this predisposition indicates that the visitors are from such a country, or that they are on a business trip rather than a vacation.

The factor is inversely correlated to the power distance index, indicating that, despite the visiting country's high level of individualism and GDP, the country may have an unequal power distribution. In other words, a rich and cold country may have a capitalist economic system.

Factor 3 is connected with hotel stars and prices. When we investigate the hotel ratings, we discover that the discrepancy in reported levels of customer satisfaction is linked to hotel features. As a result, travellers are more likely to select hotels that are popular and have a high reputation among customers. Tourists will consult sites such as TripAdvisor while deciding where to spend their vacation, as well as providing great satisfaction.

In factor 4, we can detect a desire for a vacation in countries that are forward-looking and prioritize advancement. The inverse relationship with a country's indulgence raises the question: why would tourists be drawn to countries that limit people's urge for fun? The solution is found by comparing this variable to the positively correlated one. A country's progress can frequently result in a low level of desire to satisfy human needs for entertainment and people's need to enjoy life.

Factor 5 has a high correlation with the service rating. Hotel services may sometimes exceed the customer's expectations prior to paying for accommodation. Overall client satisfaction is determined by both the hotel's expectations and performance. The hotel industry provides services such as the quality of personnel training and friendliness, the local level of hospitality development, and the food and beverages available.

The next two factors consider the hotel's location. The convenience provided by hotel services is a key factor in determining a high degree of satisfaction. It is much more convenient for a traveler if the chosen location is as close to the attractions offered in each city as possible, rather than wasting a lot of time just traveling from one place to another. The 'hotel distance' variable indicates the distance between the hotel and the city center. Therefore, hotel location is an important factor in the overall quality of hospitality services and has a direct impact on the total rating. Guests that are pleased with the service tend to give the location good ratings.

Hotel features, such as F3, are presented as a contributor of overall tourist satisfaction for factor 8. Thus, the size of the hotel, as reflected by the number of rooms, appears to influence customer decisions.

Furthermore, a preference for countries with a high level of masculinity can be seen. This trend can be traced back to countries with a rich history, such as Japan, or to European countries influenced by German culture (Wikipedia).

Consequently, the last element has an inverse relationship with the UAI index, which indicates tourists' preference for destinations that do not "avoid uncertainty." As a result, in the current setting, it is critical for travelers to select countries that welcome the new and different, where society imposes less laws and the atmosphere allows for free expression.

The 10 factors analyzed, the variables they contain, and the group to which they belong are listed below.
1. Comfort: overall_rating, cleanliness_rating, rooms_rating, sleepquality_rating, value_rating
2. The country's wealth: GDP, IDV, PDI (inverse)
3. Hotel: hotel_stars, price
4. Development: LTO index, IVR (inverse)
5. Services: service_rating
6. Location: location_rating
7. Convenience: hotel_distance
8. Hotel size: hotel_norooms
9. History and attractions: MAS
10. Freedom of expression: UAI (inverse)

* ### Factor scores
![image](https://user-images.githubusercontent.com/76962878/190700065-c010678b-c03f-493c-b2b4-0432421a1cfe.png)

>Figure 6: Score plot

Figure 6 shows the relationship between each factor and the initial variables. As we can see, industrialized countries such as Japan, New Zealand, and Australia, as well as several European countries, have high levels of hotel comfort (F1) and wealth (F2). As a result, the top right corner displays countries with high ratings and high individuality and GDP.

If we were to divide the plot into two halves, we can find a scattering of developed countries at the top and countries with lesser GDP than those above at the bottom. At the same time, the countries on the right side of the plot have good ratings for the hotels surveyed, while the countries on the left have low ratings for hospitality services.

* ### Correlations
![image](https://user-images.githubusercontent.com/76962878/190700082-31c82ed5-0daf-4787-88b2-ef2e2915a7e9.png)  | ![image](https://user-images.githubusercontent.com/76962878/190700096-6e1f8f56-38d6-4432-8c36-404f08011a42.png)
------------- | -------------
Figure 8: Correlation circle for F1 and F2  | Figure 7: Correlation circle for F3 and F4

When we choose to interpret the first two factors, we can notice that any other factors show a tilt of values towards the center of the circle as the level of significance falls. Therefore, I've decided to interpret the factors 1 and 2 to make the data easier to display. The two circles in Figure 8 represent the Bartlett test (dark blue) and the Cattell test (light blue).

Most variables show higher clustering on the F2 line in the space of the first two factors, with the exception of individuals, GDP, and PDI, which are positioned at the extremes of the correlation circle, on the F1 line. By comparing this circle to the correlogram, we may determine that the clustering of values on line F2 is caused by values that are very close to 0. We have this dispersion of results because of the significant variances between the two factors.

Meanwhile, the majority of the variables are in quadrants 1 and 4 of the circle, indicating a positive connection with the first factor examined. As a result, the values in quadrant 1 have a positive correlation with both factors studied, whereas those in quadrant 4 have a positive correlation with the first factor but a negative correlation with the second.

## Conclusions

In summary, the increase in online reviews and bookings indicates that travelers (particularly those who write reviews on TripAdvisor.com and other online services) are strongly inclined to choose hotels based on their online reputation, increasing the likelihood of high-quality hotels being chosen. The growing availability of online reviews and related information about the countries visited has resulted in more educated hotel selection decisions and, eventually, higher overall customer satisfaction.

## Bibliography
https://en.wikipedia.org/wiki/Hofstede%27s_cultural_dimensions_theory
https://www.hofstede-insights.com/models/national-culture/
https://towardsdatascience.com/factor-analysis-a-complete-tutorial-1b7621890e42
https://www.datacamp.com/community/tutorials/introduction-factor-analysis
https://en.wikipedia.org/wiki/Exploratory_factor_analysis
https://www.analyticsvidhya.com/blog/2020/10/dimensionality-reduction-using-factor-analysis-in-python/


