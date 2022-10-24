import numpy as np


class ACP:
    def __init__(self, X):
        self.X = X

        mean = np.mean(self.X, axis=0)
        variance = np.std(self.X, axis=0)
        self.Xstd = (self.X - mean) / variance

        self.R = np.corrcoef(self.Xstd, rowvar=False)

        self.Cov = np.cov(self.Xstd, rowvar=False)

        valProp, vectProp = np.linalg.eigh(self.Cov)

        k_des = [k for k in reversed(np.argsort(valProp))]
        self.alpha = valProp[k_des]
        self.a = vectProp[:, k_des]

        for col in range(self.a.shape[1]):
            minim = np.min(self.a[:, col])
            maxim = np.max(self.a[:, col])
            if np.abs(minim) > np.abs(maxim):
                self.a[:, col] = -self.a[:, col]

        self.C = self.Xstd @ self.a

        self.Rxc = self.a * np.sqrt(self.alpha)

        self.Cstd = self.C / np.sqrt(self.alpha)

        C2 = self.C * self.C
        C2sum = np.sum(C2, axis=1)
        self.CalObs = np.transpose(np.transpose(C2) / C2sum)

        self.betha = C2 / (self.alpha * self.X.shape[0])

        Rxc2 = self.Rxc * self.Rxc
        self.Comun = np.cumsum(Rxc2, axis=1)

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
