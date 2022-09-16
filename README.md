# Proiect Analiza Datelor

Proiectul urmareste sa analizeze un set de date folosind analiza factoriala exploratorie a datelor. Aceasta metoda este proiectata cu scopul de a identifica relațiile de baza dintre variabilele măsurate. 

Pentru vizualizarea si calculul legaturilor am folosit biblioteca pandas si numpy ale limbajului de programare Python.


## Descriere
Variabilele folosite in studiu conțin date despre un hotel ales aleatoriu aflat in capitala uneia dintre cele 80 de tari care participa la studiu si un prim review al acestuia colectat de pe TripAdvisor.com. Țin sa menționez ca rating-ul colectat nu definește calitatea tarii respective, si, ca in orice alta tara, exista o multitudine de factori care pot afecta acest rating precum: un client nemulțumit, alegerea unui hotel care nu îndeplinea anumite criterii si care nu mai exista la momentul actual, perioada in care a fost lăsat review-ul etc. 
Analiza factorilor se va face in funcție de variabile ce țin de hotel si cele ce țin de destinație. Pentru analiza destinației am utilizat variabile precum GDP (PIB) si variabilele dimensiunii culturale ale lui Hofstede.

## Rezultate

Heatmap KMO index |  Corelograma variabile si factori
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/76962878/190694547-44afdad8-0a1f-42f6-893b-119e24dd443e.png)  | ![image](https://user-images.githubusercontent.com/76962878/190698093-11637218-6c89-4a89-a576-9ee1a3527f3b.png)

Pentru o analiza mai detaliata click [aici](Proiect/Analiza.md).




> Sursa: Radojevic, T., Stanisic, N., & Stanic, N. (2016). Inside the Rating Scores: A Multilevel Analysis of the Factors Influencing Customer Satisfaction in the Hotel Industry. Cornell Hospitality Quarterly. 
Data set: Radojevic, T., Stanisic, N., & Stanic, N. (2016), Inside the Rating Scores: A Multilevel Analysis of the Factors Influencing Customer Satisfaction in the Hotel Industry., Mendeley Data, v1 
[dataset](http://dx.doi.org/10.17632/kwsrxshf9x.1) [research](https://www.researchgate.net/publication/312164283_Inside_the_Rating_Scores_A_Multilevel_Analysis_of_the_Factors_Influencing_Customer_Satisfaction_in_the_Hotel_Industry)
