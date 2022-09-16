import sys  # import system library
import factor_analyzer as fa
import numpy as np
import pandas as pd

import functii as fct
import grafice as g
import AEF as aef

from PySide2.QtWidgets import QApplication, QTableView
from sklearn.preprocessing import StandardScaler  # standardizeaza prin eliminarea valorii medii

# citire date
table = pd.read_csv('dataIN/data.csv', index_col=0, na_values=':')

observations = table.index
variables = table.columns
numeric_matrix = table.values
m = len(variables)
factor_names = ["F" + str(i) for i in range(1, m+1)]

X = fct.inlocuireNAN(numeric_matrix)  # verifica daca sunt valori nule si pune media pe coloana in casuta lipsa
# print(X)

model = aef.AEF(X)
scalare = StandardScaler()
Xstd = scalare.fit_transform(X)  # standardizeaza matricea de valori numerice
# salvarea matricei standardizate in fisier CSV
Xstd_df = pd.DataFrame(data=Xstd, index=observations, columns=variables)
Xstd_df.to_csv('dataOUT/Xstd.csv')


# testul bartlett de sfericitate
bartlettSphericity = fa.calculate_bartlett_sphericity(Xstd_df)  # preia o matrice standardizata ca DataFrame
# print(bartlettSphericity)  # afiseaza doua valori, prima valoarea testului bartlett si a doua valorea tabelara

if bartlettSphericity[0] > bartlettSphericity[1]:
    print('Exista cel putin un factor comun!')
else:
    print('Nu exista factori!')
    exit(-1)


# calcul indici Kaiser-Meyer-Olkin
kmo = fa.calculate_kmo(Xstd_df)
# print(kmo)
vector = kmo[0]

# creare masiv 2D din masiv unidimensional
matrix = vector[:, np.newaxis]

# salvare indici KMO in fisier csv
matrix_df = pd.DataFrame(data=matrix, index=variables, columns=['Indici KMO'])
matrix_df.to_csv('dataOUT/IndiciKMO.csv')
g.corelograma(matrice=matrix_df, dec=2, titlu='Indici Kaiser-Meyer-Olkin')
# g.show()


# varianta factori
model_fact = fa.FactorAnalyzer(n_factors=m, rotation="varimax")
model_fact.fit(X)

variance = model_fact.get_factor_variance()  # calculeaza varianta factorilor intr-un dataframe care contine varianta,
# ponderea si ponderea cumulata pentru fiecare factor in parte

nrfact = fct.ncomp_estim(variance[0], variance[2], limita=0.8)

t_variance = pd.DataFrame(
    data=np.round(np.array(variance).T, 3),
    index=["F" + str(i) for i in range(1, m + 1)],
    columns=["Varianta", "Pondere", "Pondere cumulata"]
    )
t_variance.to_csv("dataOUT/Varianta_f.csv")


if kmo[1] > 0.5:
    print('Exista cel putin un factor comun!')
else:
    print('Nu exista factori!')
    exit(-2)

# calculul numarului de factori semnificativi
chi2TabMin = 1
nrSemnificativeFac = 2
for k in range(2, m + 1):
    faModel = fa.FactorAnalyzer(n_factors=k, rotation=None)
    faModel.fit(X)
    commonFac = faModel.loadings_  # returneaza factor loadings (factorii de corelatie)
    specificFac = faModel.get_uniquenesses()  # returneaza factorii specifici
    # print(commonFac)
    # print(specificFac)

    chi2Calc, chi2Tab = model.bartlett_test(commonFac, specificFac)
    # print(chi2Calc, chi2Tab)

    if np.isnan(chi2Tab):
        break
    if chi2Tab < chi2TabMin:
        chi2TabMin = chi2Tab
        nrSemnificativeFac = k

print('Numarul de factori semnificativi extrasi:', nrSemnificativeFac)

# plot de varianta
nrfact.append(nrSemnificativeFac)
g.plot_varianta(variance[0], nrfact)

faModelAdecvat = fa.FactorAnalyzer(n_factors=m, rotation="varimax")
faModelAdecvat.fit(X)

loadings = faModelAdecvat.loadings_  # matricea factorilor de corelatie

# print(loadings)
t_loadings = pd.DataFrame(np.round(loadings[:, :nrfact[3]], 3), variables, factor_names[:nrfact[3]])
print(t_loadings)
t_loadings.to_csv("dataOUT/Corelatii.csv")
g.corelograma(matrice=t_loadings, dec=2, titlu='Corelatii variabile factori')
# g.show()

g.plot_corelatii(t_loadings, "F1", "F2", aspect=1)
# g.show()

# matricea scorurilor
scores = faModelAdecvat.transform(X)
t_scores = pd.DataFrame(np.round(scores[:, :nrfact[3]], 5), observations, factor_names[:nrfact[3]])
# print(t_scores)
t_scores.to_csv("dataOUT/Scoruri.csv")

f1 = t_scores.iloc[:, 0].values
f2 = t_scores.iloc[:, 1].values
g.plot_scoruri(f1, f2, "F1", "F2", observations.values, "Scoruri factoriale", aspect=1)


# afiseaza tabelele si graficele la rularea programului
app = QApplication(sys.argv)

tableVar = g.Model(t_variance)
viewVar = QTableView()
viewVar.setModel(tableVar)
viewVar.resize(800, 750)
# viewVar.show()

tableLoad = g.Model(t_loadings)
viewLoad = QTableView()
viewLoad.setModel(tableLoad)
viewLoad.resize(800, 750)
# viewLoad.show()

tableScore = g.Model(t_scores)
viewScore = QTableView()
viewScore.setModel(tableScore)
viewScore.resize(800, 750)
# viewScore.show()

# g.show()
sys.exit(app.exec_())

