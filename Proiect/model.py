from gui import *
import controller
import grafice as g
import analiza as an


class Frame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tabWidget.setCurrentWidget(self.tab)
        self.KMOindex()
        self.tabWidget.currentChanged.connect(self.tabChanged)

        self.buton_varianta.clicked.connect(self.factor_variance)
        self.buton_corelatii.clicked.connect(self.correlations)
        self.buton_scoruri.clicked.connect(self.scores)

    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.KMOindex()
        elif self.tabWidget.currentIndex() == 1:
            self.variance_plot()
        elif self.tabWidget.currentIndex() == 2:
            self.correlogram()
        elif self.tabWidget.currentIndex() == 3:
            self.correlations_plot()
        elif self.tabWidget.currentIndex() == 4:
            self.scores_plot()

    def scores_plot(self):
        model = an.Model

        f1 = model.f1
        f2 = model.f2
        observations = model.observations

        g.scores_plot(self.plot_scoruri.canvas, f1, f2, "F1", "F2", observations.values, "Factor scores", aspect=1)

    def scores(self):
        model = an.Model

        t_scores = model.t_scores
        t_scores.to_csv("dataOUT/Scores.csv")

        dialog = controller.DialogNonModal(self, t_scores, titlu="Factorial scores")
        dialog.show()

    def correlations_plot(self):
        model = an.Model

        t_loadings = model.t_loadings

        g.correlations_plot(self.plot_corelatii.canvas, t_loadings, "F1", "F2", aspect=1)

    def correlations(self):
        model = an.Model

        t_loadings = model.t_loadings
        t_loadings.to_csv("dataOUT/Correlations.csv")

        dialog = controller.DialogNonModal(self, t_loadings, titlu="Factor correlations")
        dialog.show()

    def correlogram(self):
        model = an.Model

        t_loadings = model.t_loadings

        g.correlogram(self.corelograma.canvas, matrice=t_loadings, dec=2, titlu='Factor - variable correlations')

    def variance_plot(self):
        model = an.Model

        nrfact = model.nrfact
        variance = model.variance

        g.variance_plot(self.plot_varianta.canvas, variance[0], nrfact)

    def KMOindex(self):
        model = an.Model

        t_kmo = model.matrix_df
        t_kmo.to_csv('dataOUT/KMOindex.csv')

        g.correlogram(self.factorabilitate.canvas, matrice=t_kmo, dec=2, titlu="Kaiser-Meyer-Olkin index heatmap")

    def factor_variance(self):
        model = an.Model

        t_variance = model.t_variance
        t_variance.to_csv("dataOUT/Variance_f.csv")

        dialog = controller.DialogNonModal(self, t_variance, titlu="Factors variance")
        dialog.show()
