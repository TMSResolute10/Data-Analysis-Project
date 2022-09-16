import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd
from PySide2.QtCore import QAbstractTableModel, Qt
# QAbstractTableModel este clasa folosita pentru crearea unui model de tabel


# clasa folosita pentru conversia dataframe in tabel
class Model(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, col, orientation, role=Qt.DisplayRole):
        # verifica daca rolurile (denumirea coloanelor si indecsi) sunt afisate
        if role != Qt.DisplayRole:
            return None

        # afisare coloane
        if orientation == Qt.Horizontal:
            try:
                return self._df.columns.tolist()[col]
            except(IndexError, ):
                return None

        # afisare indecsi
        elif orientation == Qt.Vertical:
            try:
                return self._df.index.tolist()[col]
            except (IndexError, ):
                return None

    # convertim modelul
    def data(self, index, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if not index.isValid():
            return None

        return str(self._df.iloc[index.row(), index.column()])

    # pune valorile din dataframe in tabel
    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]

        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=None):
        return len(self._df.index)

    def columnCount(self, parent=None):
        return len(self._df.columns)


def corelograma(matrice=None, dec=2, titlu='Corelograma', valMin=-1, valMax=1):
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrice, dec), cmap='RdBu', vmin=valMin, vmax=valMax, annot=True)


def show():
    plt.show()


def plot_varianta(alpha, nrcomp, titlu="Plot varianta"):
    fig = plt.figure(figsize=(13, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel("Componente", fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel("Varianta", fontdict={"fontsize": 12, "color": "b"})
    m = len(alpha)
    x = np.arange(1, m + 1)
    ax.set_xticks(x)
    ax.plot(x, alpha)
    ax.axhline(1, c='g', label="Kaiser")
    if nrcomp[1] is not np.NaN:
        ax.axhline(alpha[nrcomp[1] - 1], c='m', label="Pondere varianta > 0.8")
    if nrcomp[2] is not np.NaN:
        ax.axhline(alpha[nrcomp[2] - 1], c='c', label="Cattell")
    ax.axhline(alpha[nrcomp[3]-1], c='r', label="Bartlett")
    ax.scatter(x, alpha, c='r')
    ax.legend()


def plot_corelatii(t, var1, var2, titlu="Corelatii variabile-componente", aspect='auto'):
    fig = plt.figure(figsize=(9, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    u = np.arange(0, np.pi * 2, 0.01)
    ax.plot(np.cos(u), np.sin(u))
    ax.plot(0.7 * np.cos(u), 0.7 * np.sin(u), c='c')
    ax.axvline(0)
    ax.axhline(0)
    ax.scatter(t[var1], t[var2], c="r")
    for i in range(len(t)):
        ax.text(t[var1].iloc[i], t[var2].iloc[i], t.index[i])


def plot_scoruri(x,y,var1, var2,z,titlu="Plot componente", aspect='auto'):
    fig = plt.figure(figsize=(13, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    ax.axvline(0)
    ax.axhline(0)
    ax.scatter(x, y, c="r")
    for i in range(len(z)):
        ax.text(x[i], y[i], z[i])