# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue Feb 25 14:17:14 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inserer_button = QtWidgets.QPushButton(self.centralwidget)
        self.inserer_button.setGeometry(QtCore.QRect(510, 100, 80, 23))
        self.inserer_button.setAccessibleName("")
        self.inserer_button.setObjectName("inserer_button")
        self.rechercher_button = QtWidgets.QPushButton(self.centralwidget)
        self.rechercher_button.setGeometry(QtCore.QRect(420, 100, 80, 23))
        self.rechercher_button.setAccessibleName("")
        self.rechercher_button.setObjectName("rechercher_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 20, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 20, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 20, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 20, 31, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(490, 20, 31, 16))
        self.label_7.setObjectName("label_7")
        self.supprimer_button = QtWidgets.QPushButton(self.centralwidget)
        self.supprimer_button.setGeometry(QtCore.QRect(600, 100, 80, 23))
        self.supprimer_button.setAccessibleName("")
        self.supprimer_button.setObjectName("supprimer_button")
        self.nom_bonhomme = QtWidgets.QLineEdit(self.centralwidget)
        self.nom_bonhomme.setGeometry(QtCore.QRect(280, 100, 113, 23))
        self.nom_bonhomme.setObjectName("nom_bonhomme")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 80, 111, 16))
        self.label_9.setObjectName("label_9")
        self.corps_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.corps_text_input.setGeometry(QtCore.QRect(290, 40, 21, 23))
        self.corps_text_input.setObjectName("corps_text_input")
        self.tete_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.tete_text_input.setGeometry(QtCore.QRect(330, 40, 21, 23))
        self.tete_text_input.setObjectName("tete_text_input")
        self.antenne_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.antenne_text_input.setGeometry(QtCore.QRect(380, 40, 21, 23))
        self.antenne_text_input.setObjectName("antenne_text_input")
        self.bras_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bras_text_input.setGeometry(QtCore.QRect(430, 40, 21, 23))
        self.bras_text_input.setObjectName("bras_text_input")
        self.jambes_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.jambes_text_input.setGeometry(QtCore.QRect(480, 40, 21, 23))
        self.jambes_text_input.setObjectName("jambes_text_input")
        self.doigts_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.doigts_text_input.setGeometry(QtCore.QRect(530, 40, 21, 23))
        self.doigts_text_input.setObjectName("doigts_text_input")
        self.yeux_text_input = QtWidgets.QLineEdit(self.centralwidget)
        self.yeux_text_input.setGeometry(QtCore.QRect(580, 40, 21, 23))
        self.yeux_text_input.setObjectName("yeux_text_input")
        self.output_field = QtWidgets.QTextEdit(self.centralwidget)
        self.output_field.setGeometry(QtCore.QRect(280, 140, 401, 401))
        self.output_field.setObjectName("output_field")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.inserer_button.setText(QtWidgets.QApplication.translate("MainWindow", "Insérer", None, -1))
        self.rechercher_button.setText(QtWidgets.QApplication.translate("MainWindow", "Rechercher", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "C", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "T", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "A", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "B", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "D", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Y", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "J", None, -1))
        self.supprimer_button.setText(QtWidgets.QApplication.translate("MainWindow", "Supprimer", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Nom bonhomme", None, -1))

