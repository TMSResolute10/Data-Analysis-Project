import numpy as np

# avem clasa pentru modelul acp si calculele necesare pentru acesta
class ACP:
    def __init__(self, X):
        self.X = X

        # standardizarea valorilor variabilelor observate
        mean = np.mean(self.X, axis=0)  # medii calculate pe coloane
        variance = np.std(self.X, axis=0)  # avem variabilele pe coloane
        self.Xstd = (self.X - mean) / variance

        # calcul matrice de corelatie
        self.R = np.corrcoef(self.Xstd, rowvar=False)

        # calcul matrice de covarianta
        self.Cov = np.cov(self.Xstd, rowvar=False)  # avem variabilele pe coloane
        # print('Matrice cov:' + str(self.Cov.shape[0]) + ' linii, ' + str(self.Cov.shape[1]) + ' coloane')

        # calcul valorii proprii si vectori proprii ai matricei de varianta/covarianta
        valProp, vectProp = np.linalg.eigh(self.Cov)
        # print(valProp)

        # sortare descrescatoare a valorilor proprii si avectorilor proprii
        k_des = [k for k in reversed(np.argsort(valProp))]
        # print(k_des)
        self.alpha = valProp[k_des]
        self.a = vectProp[:, k_des]
        # print(self.alpha)

        # regularizare vectorilor proprii
        for col in range(self.a.shape[1]):
            minim = np.min(self.a[:, col])
            maxim = np.max(self.a[:, col])
            if np.abs(minim) > np.abs(maxim):
                self.a[:, col] = -self.a[:, col]

        # calcul componentelor principale
        self.C = self.Xstd @ self.a  # operatorul @ este supraincarcat pentru inmultire matriceala

        # calcul factori de corelatie - corelatie dintre variabilele initiale si componentele principale
        # (factor loadings)
        self.Rxc = self.a * np.sqrt(self.alpha)

        # calculul scorurilor (componentele principale standardizate)
        self.Cstd = self.C / np.sqrt(self.alpha)

        # calculul calitatii reprezentarii observatiilor pe axele conponentelor principale
        C2 = self.C * self.C
        C2sum = np.sum(C2, axis=1)  # calcul peranduri, pentru observatii
        self.CalObs = np.transpose(np.transpose(C2) / C2sum)

        # calculul contributiei observatiilor la varianta axelor componentelor
        self.betha = C2 / (self.alpha * self.X.shape[0])

        # calculul comunitatilor - componentele principale regasite in variabilele initiale (observate)
        Rxc2 = self.Rxc * self.Rxc
        self.Comun = np.cumsum(Rxc2, axis=1)  # sume cumulative calculate pe linii, pentru observatii

    def getR(self):
        return self.R

    def getXstd(self):
        return self.Xstd

    def getValProp(self):
        return self.alpha

    def getCompPrin(self):
        return self.C

    def getFactoriCorelatie(self):
        return self.Rxc

    def getScoruri(self):
        return self.Cstd

    def getCalObs(self):
        return self.CalObs

    def getBetha(self):
        return self.betha

    def getComun(self):
        return self.Comun