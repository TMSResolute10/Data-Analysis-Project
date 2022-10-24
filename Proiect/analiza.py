import factor_analyzer as fa
import numpy as np
import pandas as pd

import functii as fct
import AEF as aef

from sklearn.preprocessing import StandardScaler


class Model:
    table = pd.read_csv('dataIN/data.csv', index_col=0, na_values=':')

    observations = table.index
    variables = table.columns
    numeric_matrix = table.values
    m = len(variables)
    factor_names = ["F" + str(i) for i in range(1, m+1)]

    X = fct.replaceNAN(numeric_matrix)

    model = aef.AEF(X)
    scalare = StandardScaler()
    Xstd = scalare.fit_transform(X)

    Xstd_df = pd.DataFrame(data=Xstd, index=observations, columns=variables)
    Xstd_df.to_csv('dataOUT/Xstd.csv')

    bartlettSphericity = fa.calculate_bartlett_sphericity(Xstd_df)

    kmo = fa.calculate_kmo(Xstd_df)

    vector = kmo[0]
    matrix = vector[:, np.newaxis]

    matrix_df = pd.DataFrame(data=matrix, index=variables, columns=['KMO index'])

    model_fact = fa.FactorAnalyzer(n_factors=m, rotation="varimax")
    model_fact.fit(X)
    variance = model_fact.get_factor_variance()
    nrfact = fct.ncomp_estim(variance[0], variance[2], limita=0.8)

    t_variance = pd.DataFrame(
        data=np.round(np.array(variance).T, 3),
        index=["F" + str(i) for i in range(1, m + 1)],
        columns=["Variance", "Weight", "Cumulative weight"]
    )

    nrSemnificativeFac = fct.factori_semnificativi(m, X)
    nrfact.append(nrSemnificativeFac)

    faModelAdecvat = fa.FactorAnalyzer(n_factors=m, rotation="varimax")
    faModelAdecvat.fit(X)

    loadings = faModelAdecvat.loadings_

    t_loadings = pd.DataFrame(
        np.round(loadings[:, :nrfact[3]], 3), variables, factor_names[:nrfact[3]])

    scores = faModelAdecvat.transform(X)
    t_scores = pd.DataFrame(
        np.round(scores[:, :nrfact[3]], 5), observations, factor_names[:nrfact[3]])

    f1 = t_scores.iloc[:, 0].values
    f2 = t_scores.iloc[:, 1].values
