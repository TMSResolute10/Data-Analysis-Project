from PySide2.QtWidgets import *
from PySide2.QtCore import *


class ModelTabel(QAbstractTableModel):
    def __init__(self, data):
        super(ModelTabel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            coloana = index.column()
            linia = index.row()
            valoare = self._data.iloc[linia, coloana]
            return str(valoare)
        if role == Qt.TextAlignmentRole:
            return Qt.AlignLeft

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data.columns)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class DialogNonModal(QDialog):
    def __init__(self, parent, t, titlu="Tabel"):
        QDialog.__init__(self, parent)
        self.setModal(False)

        window = QMainWindow()
        centralWidget = QWidget()
        window.setCentralWidget(centralWidget)
        centralLayout = QGridLayout(centralWidget)

        tabel = QTableView()
        model = ModelTabel(data=t)
        tabel.setModel(model)

        tabel.setShowGrid(False)
        tabel.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        tabel.verticalHeader().setDefaultAlignment(Qt.AlignRight)

        tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabel.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabel.horizontalHeader().setMinimumSectionSize(70)

        tabel.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        centralLayout.addWidget(tabel)
        self.setLayout(centralLayout)
        self.setWindowTitle(titlu)
