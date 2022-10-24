import seaborn as sb
import numpy as np
import pandas as pd
from PySide2.QtCore import QAbstractTableModel, Qt


class Model(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, col, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            try:
                return self._df.columns.tolist()[col]
            except(IndexError, ):
                return None

        elif orientation == Qt.Vertical:
            try:
                return self._df.index.tolist()[col]
            except (IndexError, ):
                return None

    def data(self, index, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if not index.isValid():
            return None

        return str(self._df.iloc[index.row(), index.column()])

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]

        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=None):
        return len(self._df.index)

    def columnCount(self, parent=None):
        return len(self._df.columns)


def variance_plot(fig, alpha, nrcomp, titlu="Variance plot"):
    ax = fig.figure.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel("Components", fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel("Variance", fontdict={"fontsize": 12, "color": "b"})
    m = len(alpha)
    x = np.arange(1, m + 1)
    ax.set_xticks(x)
    ax.plot(x, alpha)
    ax.axhline(1, c='g', label="Kaiser")
    if nrcomp[1] is not np.NaN:
        ax.axhline(alpha[nrcomp[1] - 1], c='m', label="Variance weight > 0.8")
    if nrcomp[2] is not np.NaN:
        ax.axhline(alpha[nrcomp[2] - 1], c='c', label="Cattell")
    ax.axhline(alpha[nrcomp[3]-1], c='r', label="Bartlett")
    ax.scatter(x, alpha, c='r')
    ax.legend()

    fig.show()


def correlogram(fig, matrice=None, dec=2, titlu='Correlogram', valMin=-1, valMax=1):
    fig.figure.clf()
    ax = fig.figure.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 14, "color": "k"}, verticalalignment='bottom')
    fig.figure.subplots_adjust(left=.2)
    sb.heatmap(data=np.round(matrice, dec), cmap='RdBu', vmin=valMin, vmax=valMax, annot=True, ax=ax)
    fig.draw()
    fig.show()


def correlations_plot(fig, t, var1, var2, titlu="Correlations factors-components", aspect='auto'):
    ax = fig.figure.add_subplot(1, 1, 1)
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
    fig.show()


def scores_plot(fig, x, y, var1, var2, z, titlu="Scores plot", aspect='auto'):
    ax = fig.figure.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    ax.axvline(0)
    ax.axhline(0)
    ax.scatter(x, y, c="r")
    for i in range(len(z)):
        ax.text(x[i], y[i], z[i])
    fig.show()
