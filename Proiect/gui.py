# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiwqNidq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1283, 775)
        MainWindow.setStyleSheet(u"/*  ------------------------------------------------------------------------  */\n"
"/* QtMaterial - https://github.com/UN-GCPDS/qt-material\n"
"/* By Yeison Cardona - GCPDS\n"
"/*  ------------------------------------------------------------------------  */\n"
"\n"
"*{\n"
"  color: #2F2F31;\n"
"  font-family: \"IBM Plex Sans SemiBold\";\n"
"  line-height: {{line_height}};\n"
"  font-size: 25px;\n"
"background-color: #000000;\n"
"  selection-background-color: #F3F3F3;\n"
"  selection-color: #2F2F2F;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"*:focus {\n"
"   outline: none;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  Custom colors  */\n"
"\n"
".danger{\n"
"  color: #D91E27;\n"
"}\n"
"\n"
".warning{\n"
"  color: #24F2A7;\n"
"}\n"
"\n"
".success{\n"
"  color: #F87C0A;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  Basic widgets  */\n"
"\n"
"QWidget {\n"
"  background-color: #F3F3F3;\n"
"}\n"
"\n"
"QFrame {\n"
""
                        "  background-color: #FFFFFF;\n"
"}\n"
"\n"
"QSplitter {\n"
"  background-color: transparent;\n"
"  border: none\n"
"}\n"
"\n"
"QStatusBar {\n"
"  color: #2F2F31;\n"
"  background-color: #FFFFFF20;\n"
"  border-radius: 0px;\n"
"}\n"
"\n"
"MplWidget {\n"
"	padding-left: 20px;\n"
"}\n"
"\n"
"QScrollArea,\n"
"QStackedWidget,\n"
"QWidget > QToolBox,\n"
"QToolBox > QWidget,\n"
"QTabWidget > QWidget {\n"
"  border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: none;\n"
"margin: -12px -9px -13px -12px;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  Inputs  */\n"
"\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTextEdit,\n"
"QLineEdit,\n"
"QPushButton {\n"
"  color: #ECECEC;\n"
"  background-color: #ECECEC;\n"
"  border-top: #ECECEC;\n"
"  border-top-style: solid;\n"
"  border-width: 2px;\n"
"  border-radius: 0px;\n"
"  padding: 8px 16px ;\n"
"  height: 18px;\n"
"}\n"
"\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTreeView,\n"
"QLi"
                        "stView,\n"
"QLineEdit,\n"
"QComboBox {\n"
"  padding-left: 15px;\n"
"  border-radius: 0px;\n"
"  background-color: #2f2f31;\n"
"  border-width: 0 0 2px 0;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"QPlainTextEdit {\n"
"  border-radius: 4px;\n"
"  padding: 8px 16px;\n"
"  background-color: #000000;\n"
"  \n"
"}\n"
"\n"
"QDateTimeEdit:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled,\n"
"QTextEdit:disabled,\n"
"QLineEdit:disabled {\n"
"  color: #ECECEC20;\n"
"  background-color: #2f2f3170;\n"
"  border: #ECECEC20;\n"
"border-style: solid;\n"
"  border-width: 2px;\n"
"  border-width: 0 0 2px 0;\n"
"  padding: 8px 16px ;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"  padding: 8px;\n"
"  border-radius: 4px;\n"
"  background-color: #2f2f31;\n"
"}\n"
"\n"
"QDateTimeEdit:disabled,\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled,\n"
"QTextEdit:disabled,\n"
"QL"
                        "ineEdit:disabled {\n"
"  color: #ECECEC20;\n"
"  background-color: #2f2f3175;\n"
"  border: #ECECEC20;\n"
"border-style: solid;\n"
"  border-width: 2px;\n"
"  border-width: 0 0 2px 0;\n"
"}\n"
"\n"
"QComboBox {\n"
"  color: #ECECEC;\n"
"  border: #ECECEC;\n"
"border-style: solid;\n"
"  border-width: 1px;\n"
"  border-width: 0 0 2px 0;\n"
"  background-color: #2f2f31;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 36px;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"  color: #ECECEC20;\n"
"  background-color: #2f2f3175;\n"
"  border-bottom-style: 2px solid;\n"
"  border-bottom:  #ECECEC20;\n"
"}\n"
"QComboBox::drop-down {\n"
"  border: none;\n"
"  color: #ECECEC;\n"
"  width: 20px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"  image: url(icon:/primary/downarrow.svg);\n"
"  margin-right: 10px;\n"
"}\n"
"QComboBox::down-arrow:disabled {\n"
"  image: url(icon:/disabled/downarrow.svg);\n"
"  margin-right: 10px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  bac"
                        "kground-color: #2f2f31;\n"
"  border: #FFFFFF;\n"
"border-style: solid;\n"
"  border-width: 2px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox[frame='false'] {\n"
"  color: #ECECEC;\n"
"  background-color: transparent;\n"
"  border: 1px solid transparent;\n"
"}\n"
"QComboBox[frame='false']:disabled {\n"
"  color: #ECECEC20;\n"
"}\n"
"QDateTimeEdit::up-button,\n"
"QDoubleSpinBox::up-button,\n"
"QSpinBox::up-button {\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: top right;\n"
"  width: 20px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"  image: url(icon:/primary/uparrow.svg);\n"
"  border-width: 0px;\n"
"  margin-right: 5px;\n"
"}\n"
"\n"
"QDateTimeEdit::up-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled,\n"
"QSpinBox::up-button:disabled {\n"
"  image: url(icon:/disabled/uparrow.svg);\n"
"}\n"
"\n"
"QDateTimeEdit::down-button,\n"
"QDoubleSpinBox::down-button,\n"
"QSpinBox::down-button {\n"
"  subcontrol-origin: border;\n"
"  subcontrol-position: bottom right;\n"
""
                        "  width: 20px;\n"
"  image: url(icon:/primary/downarrow.svg);\n"
"  border-width: 0px;\n"
"  border-top-width: 0;\n"
"  margin-right: 5px;\n"
"}\n"
"\n"
"QDateTimeEdit::down-button:disabled,\n"
"QDoubleSpinBox::down-button:disabled,\n"
"QSpinBox::down-button:disabled {\n"
"  image: url(icon:/disabled/downarrow.svg);\n"
"}\n"
"\n"
"QPushButton {\n"
"  margin: 0px;\n"
"  padding: 0px 16px;\n"
"  height: 34px;\n"
"  min-height: 34px;\n"
"  max-height: 34px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked,\n"
"QPushButton:pressed {\n"
"  color: #000000;\n"
"  background-color: #ECECEC;\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"  padding: 5px;\n"
"  margin: 0px;\n"
"  color: #ECECEC;\n"
"  border: none;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:flat:hover {\n"
"  background-color: #ECECEC20;\n"
"}\n"
"\n"
"QPushButton:flat:pressed,\n"
"QPushButton:flat:checked {\n"
"  background-color: #ECECEC10;\n"
"}\n"
"\n"
"QPushButton:disabled,\n"
"QPushButton:flat:disabled {\n"
"  color: #FFFFFF75;\n"
"  background-"
                        "color: transparent;\n"
"  border-color:  #2f2f31;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"  border: #FFFFFF75;\n"
"	border-width: 2px solid;\n"
"}\n"
"\n"
"QPushButton:checked:disabled {\n"
"  color: #2f2f31;\n"
"  background-color: #FFFFFF;\n"
"  border-color:  #FFFFFF;\n"
"}\n"
"\n"
"QTabBar{\n"
"  color: red;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  color: #909597;\n"
"  font-size: 14px;\n"
"background-color: #ECECEC;\n"
"margin-right: 1px;\n"
"  font-family: \"IBM Plex Sans Medium\";\n"
"}\n"
"\n"
"QTabBar::tab:bottom,\n"
"QTabBar::tab:top{\n"
"  padding: 0 43px;\n"
"  height: 30px;\n"
"}\n"
"\n"
"QTabBar::tab:left,\n"
"QTabBar::tab:right{\n"
"  padding: 15px 0;\n"
"  width: 30px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected,\n"
"QTabBar::tab:top:hover {\n"
"  color: #000000;\n"
"font-family: \"IBM Plex Sans SemiBold\";\n"
"background-color: #FFFFFF;\n"
"  border: solid black;\n"
"border-radius: 0;\n"
"border-width: 1px 0 0 0;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected,\n"
"QTabBar::tab:bottom:hover {\n"
"  colo"
                        "r: #ECECEC;\n"
"  border-top: #ECECEC;\n"
"border-top-style: 2px solid;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected,\n"
"QTabBar::tab:right:hover {\n"
"  color: #ECECEC;\n"
"  border-left: #ECECEC;\n"
"border-left-style: 2px solid;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected,\n"
"QTabBar::tab:left:hover {\n"
"  color: #ECECEC;\n"
"  border-right: #ECECEC;\n"
"border-right-style: 2px solid;\n"
"}\n"
"\n"
"QTabBar QToolButton:hover,\n"
"QTabBar QToolButton {\n"
"  border: 20px;\n"
"  background-color: #000000;\n"
"}\n"
"\n"
"QTabBar QToolButton::up-arrow {\n"
"  image: url(icon:/disabled/uparrow2.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::up-arrow:hover {\n"
"  image: url(icon:/primary/uparrow2.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::down-arrow {\n"
"  image: url(icon:/disabled/downarrow2.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::down-arrow:hover {\n"
"  image: url(icon:/primary/downarrow2.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"  image: url(icon:/primary/rightarrow2.svg);\n"
"}\n"
"\n"
"QTabBa"
                        "r QToolButton::right-arrow:hover {\n"
"  image: url(icon:/disabled/rightarrow2.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"  image: url(icon:/primary/leftarrow2.svg);\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:hover {\n"
"  image: url(icon:/disabled/leftarrow2.svg);\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"  image: url(icon:/disabled/tab_close.svg);\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"  image: url(icon:/primary/tab_close.svg);\n"
"}\n"
"\n"
"QGroupBox {\n"
"  background-color: #2f2f31;\n"
"  border-radius: 4px;\n"
"  padding: 15px;\n"
"  padding-top: 30px;\n"
"  line-height: 13px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  color: #2F2F3140;\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 15px;\n"
"  margin-top: 10px;\n"
"  background-color: #000000;\n"
"  background-color: transparent;\n"
"  height: 20px;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QRadioButton and QCheckBox labels "
                        " */\n"
"\n"
"QRadioButton,\n"
"QCheckBox {\n"
"  spacing: 10px;\n"
"  color: #2F2F31;\n"
"  line-height: 14px;\n"
"  height: 30px;\n"
"  background-color: transparent;\n"
"  spacing: 5px;\n"
"}\n"
"\n"
"QRadioButton:disabled,\n"
"QCheckBox:disabled {\n"
"  color: #2F2F3130;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  General Indicators  */\n"
"\n"
"QGroupBox::indicator {\n"
"  width: 18px;\n"
"  height: 18px;\n"
"  border-radius: 3px;\n"
"}\n"
"\n"
"QMenu::indicator,\n"
"QListView::indicator,\n"
"QTableWidget::indicator,\n"
"QRadioButton::indicator,\n"
"QCheckBox::indicator {\n"
"  width: 24px;\n"
"  height: 24px;\n"
"  border-radius: 4px;\n"
" }\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QListView Indicator  */\n"
"\n"
"QListView::indicator:checked,\n"
"QListView::indicator:checked:selected,\n"
"QListView::indicator:checked:focus {\n"
"  image: url(icon:/primary/checklist.svg);\n"
"}\n"
"\n"
"QLi"
                        "stView::indicator:checked:selected:active {\n"
"  image: url(icon:/primary/checklist_invert.svg);\n"
"}\n"
"\n"
"QListView::indicator:checked:disabled {\n"
"  image: url(icon:/disabled/checklist.svg);\n"
"}\n"
"\n"
"QListView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate:selected,\n"
"QListView::indicator:indeterminate:focus {\n"
"  image: url(icon:/primary/checklist_indeterminate.svg);\n"
"}\n"
"\n"
"QListView::indicator:indeterminate:selected:active {\n"
"  image: url(icon:/primary/checklist_indeterminate_invert.svg);\n"
"}\n"
"\n"
"QListView::indicator:indeterminate:disabled {\n"
"  image: url(icon:/disabled/checklist_indeterminate.svg);\n"
"}\n"
"QTableView::indicator:enabled:checked,\n"
"QTableView::indicator:enabled:checked:selected,\n"
"QTableView::indicator:enabled:checked:focus {\n"
"  image: url(icon:/primary/checkbox_checked.svg);\n"
"}\n"
"\n"
"QTableView::indicator:checked:selected:active {\n"
"  image: url(icon:/primary/checkbox_checked_invert.svg);\n"
"}\n"
"\n"
"QTableView::i"
                        "ndicator:disabled:checked,\n"
"QTableView::indicator:disabled:checked:selected,\n"
"QTableView::indicator:disabled:checked:focus {\n"
"  image: url(icon:/disabled/checkbox_checked.svg);\n"
"}\n"
"\n"
"QTableView::indicator:enabled:unchecked,\n"
"QTableView::indicator:enabled:unchecked:selected,\n"
"QTableView::indicator:enabled:unchecked:focus {\n"
"  image: url(icon:/primary/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QTableView::indicator:unchecked:selected:active {\n"
"  image: url(icon:/primary/checkbox_unchecked_invert.svg);\n"
"}\n"
"\n"
"QTableView::indicator:disabled:unchecked,\n"
"QTableView::indicator:disabled:unchecked:selected,\n"
"QTableView::indicator:disabled:unchecked:focus {\n"
"  image: url(icon:/disabled/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QTableView::indicator:enabled:indeterminate,\n"
"QTableView::indicator:enabled:indeterminate:selected,\n"
"QTableView::indicator:enabled:indeterminate:focus {\n"
"  image: url(icon:/primary/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QTableView::indicator:"
                        "indeterminate:selected:active {\n"
"  image: url(icon:/primary/checkbox_indeterminate_invert.svg);\n"
"}\n"
"\n"
"QTableView::indicator:disabled:indeterminate,\n"
"QTableView::indicator:disabled:indeterminate:selected,\n"
"QTableView::indicator:disabled:indeterminate:focus {\n"
"  image: url(icon:/disabled/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QCheckBox and QGroupBox Indicator  */\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QGroupBox::indicator:checked {\n"
"  image: url(icon:/primary/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked {\n"
"  image: url(icon:/primary/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate {\n"
"  image: url(icon:/primary/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled {\n"
"  image: url(icon:/disab"
                        "led/checkbox_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"  image: url(icon:/disabled/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled,\n"
"QGroupBox::indicator:indeterminate:disabled {\n"
"  image: url(icon:/disabled/checkbox_indeterminate.svg);\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QRadioButton Indicator  */\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  image: url(icon:/primary/radiobutton_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"  image: url(icon:/primary/radiobutton_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled {\n"
"  image: url(icon:/disabled/radiobutton_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"  image: url(icon:/disabled/radiobutton_unchecked.svg);\n"
"}\n"
"\n"
"QDockWidget {\n"
"  color: #2F2F31;\n"
"  border: #2f2f31;\n"
"border-style:"
                        " 2px solid;\n"
"  titlebar-close-icon: url(icon:/primary/close.svg);\n"
"  titlebar-normal-icon: url(icon:/primary/float.svg);\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  text-align: left;\n"
"  padding-left: 35px;\n"
"  padding: 3px;\n"
"  margin-top: 4px;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QComboBox indicator  */\n"
"\n"
"QComboBox::indicator:checked {\n"
"  image: url(icon:/primary/checklist.svg);\n"
"}\n"
"\n"
"QComboBox::indicator:checked:selected {\n"
"  image: url(icon:/primary/checklist_invert.svg);\n"
"}\n"
"\n"
"QComboBox::item,\n"
"QCalendarWidget QMenu::item,\n"
"QMenu::item {\n"
"  height: 26px;\n"
"  border: 8px solid transparent;\n"
"  color: #2F2F31;\n"
"}\n"
"\n"
"\n"
"QCalendarWidget QMenu::item,\n"
"QMenu::item {\n"
"  padding: 0px 25px 0px 20px;\n"
"}\n"
"\n"
"QComboBox::item:selected,\n"
"QCalendarWidget QMenu::item:selected,\n"
"QMenu::item:selected {\n"
"  color: #2F2F2F;\n"
"  background-color: "
                        "#F3F3F3;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QComboBox::item:disabled,\n"
"QCalendarWidget QMenu::item:disabled,\n"
"QMenu::item:disabled {\n"
"  color: #2F2F3130;\n"
"}\n"
"\n"
"QCalendarWidget QMenu,\n"
"QMenu {\n"
"  background-color: #2f2f31;\n"
"  border: #FFFFFF;\n"
"border-style: 2px solid;\n"
"  border-radius: 4px;\n"
"  margin-top: 3px;\n"
"}\n"
"QMenu::separator {\n"
"  height: 2px;\n"
"  background-color: #FFFFFF;\n"
"  margin-left: 2px;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QMenu::right-arrow{\n"
"  image: url(icon:/primary/rightarrow.svg);\n"
"  width: 15px;\n"
"  height: 15px;\n"
"}\n"
"\n"
"QMenu::right-arrow:selected{\n"
"  image: url(icon:/disabled/rightarrow.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"  image: url(icon:/primary/checkbox_unchecked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"  image: url(icon:/primary/checkbox_unchecked_invert.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"  image: url(icon:/prim"
                        "ary/checkbox_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"  image: url(icon:/primary/checkbox_checked_invert.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked {\n"
"  image: url(icon:/primary/radiobutton_unchecked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"  image: url(icon:/primary/radiobutton_unchecked_invert.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"  image: url(icon:/primary/radiobutton_checked.svg);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"  image: url(icon:/primary/radiobutton_checked_invert.svg);\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QMenuBar  */\n"
"\n"
"QMenuBar {\n"
"  background-color: #2f2f31;\n"
"  color: #2F2F31;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"  height: 30px;\n"
"  padding: 8px;\n"
"  background-color: transparent;\n"
"  color: #2F2F31;\n"
"}\n"
"\n"
"QMenuBar::item:selected,\n"
"QMenuBar::item:pressed {\n"
""
                        "  color: #2F2F2F;\n"
"  background-color: #F3F3F3;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QToolBox  */\n"
"\n"
"QToolBox::tab {\n"
"  background-color: #2f2f31;\n"
"  color: #2F2F31;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:selected,\n"
"QToolBox::tab:hover {\n"
"  background-color: #ECECEC20;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QProgressBar  */\n"
"\n"
"QProgressBar {\n"
"  border-radius: 0;\n"
"  background-color: #FFFFFF;\n"
"  text-align: center;\n"
"  color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #ECECEC;\n"
"}\n"
"QScrollBar:horizontal {\n"
"  border: 0;\n"
"  background: #ECECEC;\n"
"  height: 8px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0;\n"
"  background: #ECECEC;\n"
"  width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background: #ECECEC;\n"
"  min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:"
                        "vertical {\n"
"  background: #ECECEC;\n"
"  min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background: #ECECEC;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"  border: 0;\n"
"  background: transparent;\n"
"  width: 0px;\n"
"  height: 0px;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QSlider  */\n"
"\n"
"QSlider:horizontal {\n"
"  min-height: 20px;\n"
"  max-height: 20px;\n"
"}\n"
"\n"
"QSlider:vertical {\n"
"  min-width: 20px;\n"
"  max-width: 20px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  height: 4px;\n"
"  background: #393939;\n"
"  margin: 0 10px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"  width: 4px;\n"
"  background: #393939;\n"
"  margin: 10px 0;\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  image: url(icon:/primary/slider"
                        ".svg);\n"
"  width: 20px;\n"
"  height: 20px;\n"
"  margin: -20px -10px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"  image: url(icon:/primary/slider.svg);\n"
"  border-radius: 20px;\n"
"  width: 20px;\n"
"  height: 20px;\n"
"  margin: -10px -20px;\n"
"}\n"
"\n"
"QSlider::add-page {\n"
"background: #2f2f31;\n"
"}\n"
"\n"
"QSlider::sub-page {\n"
"background: #ECECEC;\n"
"}\n"
"\n"
"QLabel {\n"
"  border: none;\n"
"  background: transparent;\n"
"  color: #2F2F31;\n"
"\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"  color: #2F2F3120\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  VLines and HLinex  */\n"
"\n"
"QFrame[frameShape=\"4\"] {\n"
"    background: none;\n"
"}\n"
"\n"
"QFrame[frameShape=\"5\"] {\n"
"    background: none;\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"] {\n"
"  border-color: #FFFFFF;\n"
"}\n"
"\n"
"QToolBar {\n"
"  background: #000000;\n"
"  border: 0px solid;\n"
"}\n"
"QToolBar:horizontal {\n"
"  border-bottom: #FFFFFF"
                        ";\n"
"border-bottom-style: 1px solid ;\n"
"}\n"
"\n"
"QToolBar:vertical {\n"
"  border-right:  #FFFFFF;\n"
"border-right-style: 1px solid;\n"
"}\n"
"\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  image: url(icon:/primary/toolbar-handle-horizontal.svg);\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  image: url(icon:/primary/toolbar-handle-vertical.svg);\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  border-right:  #FFFFFF;\n"
"border-right-style: 1px solid;\n"
"  border-left:  #FFFFFF;\n"
"border-left-style: 1px solid;\n"
"  width: 1px;\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  border-top:  #FFFFFF;\n"
"border-top-style: 1px solid;\n"
"  border-bottom:  #FFFFFF;\n"
"border-bottom-style: 1px solid;\n"
"  height: 1px;\n"
"}\n"
"\n"
"QToolButton {\n"
"  background: #000000;\n"
"  border: 0px;\n"
"  height: 40px;\n"
"  margin: 3px;\n"
"  padding: 3px;\n"
"  border-right:  #000000;\n"
"border-right-style: 10px solid;\n"
"  border-left:  #000000;\n"
"border-left-style: 10px solid;\n"
"}\n"
"\n"
"QTo"
                        "olButton:hover {\n"
"  background: #FFFFFF;\n"
"  border-right: #FFFFFF;\n"
"border-right-style: 10px solid;\n"
"  border-left:  #FFFFFF;\n"
"border-left-style: 10px solid;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  background: #2f2f31;\n"
"  border-right: #2f2f31;\n"
"border-right-style: 10px solid;\n"
"  border-left: #2f2f31;\n"
"border-left-style: 10px solid;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"  background: #FFFFFF;\n"
"  border-left:  #FFFFFF;\n"
"border-left-style: 10px solid;\n"
"  border-right:  #ECECEC;\n"
"border-right-style: 10px solid;\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView {\n"
"  border-radius: 4px;\n"
"  padding: 5px;\n"
"  margin: 0px;\n"
"}\n"
"\n"
"QTreeView::item,\n"
"QListView::item {\n"
"  padding: 5px;\n"
"  min-height: 25px;\n"
"  selection-color: #FFFFFF; /* For Windows */\n"
"  border-color: transparent;  /* Fix #34 */\n"
"}\n"
"\n"
"QTreeView::item:selected,\n"
"QListView::item:selected {\n"
"  background-color: #ECECEC20;\n"
"  selection-background-color: #ECECEC20;\n"
"  color"
                        ": #2F2F31;\n"
"  selection-color: #2F2F31; /* For Windows */\n"
"}\n"
"\n"
"QTreeView::item:selected:focus,\n"
"QListView::item:selected:focus {\n"
"  background-color: #ECECEC;\n"
"  selection-background-color: #ECECEC;\n"
"  color: #2F2F2F;\n"
"  selection-color: #2F2F2F; /* For Windows */\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  QTreeView  */\n"
"\n"
"QTreeView::branch{\n"
"  background-color: #2F2F31;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings,\n"
"QTreeView::branch:closed:has-children:!has-siblings {\n"
"  image: url(icon:/primary/branch-closed.svg);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"  image: url(icon:/primary/branch-open.svg);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"  border-image: url(icon:/disabled/vline.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(icon:"
                        "/disabled/branch-more.svg) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item,\n"
"QTreeView::branch:has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(icon:/disabled/branch-end.svg) 0;\n"
"}\n"
"\n"
"QTreeView QHeaderView::section {\n"
"  border: none;\n"
"}\n"
"QPushButton.danger {\n"
"  border-color: #D91E27;\n"
"  color: #D91E27;\n"
"}\n"
"\n"
"QPushButton.danger:checked,\n"
"QPushButton.danger:pressed {\n"
"  color: #000000;\n"
"  background-color: #D91E27;\n"
"}\n"
"\n"
"QPushButton.warning{\n"
"  border-color: #24F2A7;\n"
"  color: #24F2A7;\n"
"}\n"
"\n"
"QPushButton.warning:checked,\n"
"QPushButton.warning:pressed {\n"
"  color: #000000;\n"
"  background-color: #24F2A7;\n"
"}\n"
"\n"
"QPushButton.success {\n"
"  border-color: #F87C0A;\n"
"  color: #F87C0A;\n"
"}\n"
"\n"
"QPushButton.success:checked,\n"
"QPushButton.success:pressed {\n"
"  color: #000000;\n"
"  background-color: #F87C0A;\n"
"}\n"
"\n"
"QPushButton.danger:flat:hover {\n"
"  background-color: #D9"
                        "1E2720;\n"
"}\n"
"\n"
"QPushButton.danger:flat:pressed,\n"
"QPushButton.danger:flat:checked {\n"
"  background-color: #D91E2710;\n"
"  color: #D91E27;\n"
"}\n"
"\n"
"QPushButton.warning:flat:hover {\n"
"  background-color: #24F2A720;\n"
"}\n"
"\n"
"QPushButton.warning:flat:pressed,\n"
"QPushButton.warning:flat:checked {\n"
"  background-color: #24F2A710;\n"
"  color: #24F2A7;\n"
"}\n"
"\n"
"QPushButton.success:flat:hover {\n"
"  background-color:#F87C0A20;\n"
"}\n"
"\n"
"QPushButton.success:flat:pressed,\n"
"QPushButton.success:flat:checked {\n"
"  background-color: #F87C0A10;\n"
"  color: #F87C0A;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"  background-color: #FFFFFF;\n"
"  border-bottom: 1px solid #CDCDCD;\n"
"border-top: 1px solid #CDCDCD;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QTableView {\n"
"    color: #717171;\n"
"	font-size: 15px;\n"
"    border: none;\n"
"gridline-color: white;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"QTableView::item{\n"
"    border-bottom: 1px solid #CDCDCD;\n"
"}\n"
"\n"
"QTabl"
                        "eView::item:selected{\n"
"	background-color: #f0f1f2;\n"
"  color: #717171;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #FFFFFF;\n"
"  height: 35px;\n"
"  color: #CDCDCD;\n"
"border-style: 1px solid;\n"
"border-color: #CDCDCD;\n"
"font-size: 15px;\n"
"  }\n"
"\n"
"QHeaderView::section::vertical {\n"
"border-bottom: 1px solid #CDCDCD;\n"
"color: #717171;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:checked {\n"
"	background-color: white;\n"
"color: #717171;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal{\n"
"border-top: 1px solid #CDCDCD;\n"
"border-bottom: 1px solid #CDCDCD;\n"
"}\n"
"\n"
"QLCDNumber {\n"
"  color: #ECECEC;\n"
"  background-color:#ECECEC10;\n"
"  border: #ECECEC30;\n"
"border-style:  1px solid;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"#qt_calendar_prevmonth {\n"
"  qproperty-icon: url(icon:/primary/leftarrow.svg);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"  qproperty-icon: url(icon:/primary/rightarrow.svg);\n"
"}\n"
""
                        "\n"
"/*  ------------------------------------------------------------------------  */\n"
"/*  Inline QLineEdit  */\n"
"\n"
"QTreeView QLineEdit,\n"
"QListView QLineEdit {\n"
"  color: #2F2F31;\n"
"  background-color: #2F2F31;\n"
"  border: 1px solid unset;\n"
"  border-radius: unset;\n"
"  padding: unset;\n"
"  padding-left: unset;\n"
"  height: unset;\n"
"  border-width: unset;\n"
"  border-top-left-radius: unset;\n"
"  border-top-right-radius: unset;\n"
"}\n"
"QToolTip {\n"
"  padding: 5px;\n"
"  border:  #000000;\n"
"border-style: 1px solid;\n"
"  border-radius: 4px;\n"
"  color: #2F2F31;\n"
"  background-color: #FFFFFF;\n"
"}\n"
"\n"
"QDialog QToolButton,\n"
"QDialog QToolButton:hover,\n"
"QDialog QToolButton:pressed,\n"
"QDialog QToolButton:checked {\n"
"  background-color: unset;\n"
"  border: 0px;\n"
"  height: unset;\n"
"  margin: unset;\n"
"  padding: unset;\n"
"  border-right: unset;\n"
"  border-left: unset;\n"
"}\n"
"\n"
"/*  ------------------------------------------------------------------------ "
                        " */\n"
"/*  Grips  */\n"
"\n"
"\n"
"QMainWindow::separator:vertical,\n"
"QSplitter::handle:horizontal {\n"
"  image: url(icon:/primary/splitter-horizontal.svg);\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal,\n"
"QSplitter::handle:vertical {\n"
"  image: url(icon:/primary/splitter-vertical.svg);\n"
"}\n"
"\n"
"QSizeGrip {\n"
"  image: url(icon:/primary/sizegrip.svg);\n"
"  background-color: transparent;\n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(145, 0))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_18 = QFrame(self.tab)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.frame_18)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        self.frame_14.setMinimumSize(QSize(0, 91))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"IBM Plex Sans SemiBold")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setMargin(10)
        self.label_7.setIndent(0)

        self.verticalLayout_13.addWidget(self.label_7, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.factorabilitate = MplWidget(self.frame_18)
        self.factorabilitate.setObjectName(u"factorabilitate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.factorabilitate.sizePolicy().hasHeightForWidth())
        self.factorabilitate.setSizePolicy(sizePolicy2)
        self.factorabilitate.setFrameShape(QFrame.StyledPanel)
        self.factorabilitate.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.factorabilitate)


        self.gridLayout.addWidget(self.frame_18, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_15 = QFrame(self.tab_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.frame_15)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 91))
        self.frame_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setMargin(10)
        self.label_3.setIndent(0)

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.plot_varianta = MplWidget(self.frame_15)
        self.plot_varianta.setObjectName(u"plot_varianta")
        sizePolicy2.setHeightForWidth(self.plot_varianta.sizePolicy().hasHeightForWidth())
        self.plot_varianta.setSizePolicy(sizePolicy2)
        self.plot_varianta.setFrameShape(QFrame.StyledPanel)
        self.plot_varianta.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.plot_varianta)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_8.addWidget(self.plot_varianta)

        self.buton_varianta = QPushButton(self.frame_15)
        self.buton_varianta.setObjectName(u"buton_varianta")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buton_varianta.sizePolicy().hasHeightForWidth())
        self.buton_varianta.setSizePolicy(sizePolicy3)
        self.buton_varianta.setMinimumSize(QSize(150, 36))
        self.buton_varianta.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"IBM Plex Sans Medium\";")

        self.verticalLayout_8.addWidget(self.buton_varianta, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.frame_15, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_13 = QFrame(self.tab_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_8 = QFrame(self.frame_13)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 91))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setMargin(10)
        self.label_4.setIndent(0)

        self.verticalLayout_7.addWidget(self.label_4)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.corelograma = MplWidget(self.frame_13)
        self.corelograma.setObjectName(u"corelograma")
        sizePolicy2.setHeightForWidth(self.corelograma.sizePolicy().hasHeightForWidth())
        self.corelograma.setSizePolicy(sizePolicy2)
        self.corelograma.setFrameShape(QFrame.StyledPanel)
        self.corelograma.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.corelograma)

        self.buton_corelatii = QPushButton(self.frame_13)
        self.buton_corelatii.setObjectName(u"buton_corelatii")
        self.buton_corelatii.setMinimumSize(QSize(150, 36))
        self.buton_corelatii.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"IBM Plex Sans Medium\";")

        self.verticalLayout_10.addWidget(self.buton_corelatii, 0, Qt.AlignRight)


        self.gridLayout_3.addWidget(self.frame_13, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_16 = QFrame(self.tab_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setMinimumSize(QSize(0, 91))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setMargin(10)
        self.label_5.setIndent(0)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.plot_corelatii = MplWidget(self.frame_16)
        self.plot_corelatii.setObjectName(u"plot_corelatii")
        sizePolicy2.setHeightForWidth(self.plot_corelatii.sizePolicy().hasHeightForWidth())
        self.plot_corelatii.setSizePolicy(sizePolicy2)
        self.plot_corelatii.setFrameShape(QFrame.StyledPanel)
        self.plot_corelatii.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.plot_corelatii)


        self.gridLayout_4.addWidget(self.frame_16, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_17 = QFrame(self.tab_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_17)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_12 = QFrame(self.frame_17)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 91))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setMargin(10)
        self.label_6.setIndent(0)

        self.verticalLayout_11.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.plot_scoruri = MplWidget(self.frame_17)
        self.plot_scoruri.setObjectName(u"plot_scoruri")
        sizePolicy2.setHeightForWidth(self.plot_scoruri.sizePolicy().hasHeightForWidth())
        self.plot_scoruri.setSizePolicy(sizePolicy2)
        self.plot_scoruri.setFrameShape(QFrame.StyledPanel)
        self.plot_scoruri.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.plot_scoruri)

        self.buton_scoruri = QPushButton(self.frame_17)
        self.buton_scoruri.setObjectName(u"buton_scoruri")
        self.buton_scoruri.setMinimumSize(QSize(150, 36))
        self.buton_scoruri.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 12pt \"IBM Plex Sans Medium\";")

        self.verticalLayout_4.addWidget(self.buton_scoruri, 0, Qt.AlignRight)


        self.gridLayout_5.addWidget(self.frame_17, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Factorabilitate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Factorabilitate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plot varianta", None))
        self.buton_varianta.setText(QCoreApplication.translate("MainWindow", u"Varianta factori", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Plot varianta", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Corelograma", None))
        self.buton_corelatii.setText(QCoreApplication.translate("MainWindow", u"Corelatii", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Corelograma", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Plot corelatii", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Plot corelatii", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Plot scoruri", None))
        self.buton_scoruri.setText(QCoreApplication.translate("MainWindow", u"Scoruri", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Plot scoruri", None))
    # retranslateUi

