# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inserer_button = QPushButton(self.centralwidget)
        self.inserer_button.setObjectName(u"inserer_button")
        self.inserer_button.setGeometry(QRect(510, 100, 80, 23))
        self.rechercher_button = QPushButton(self.centralwidget)
        self.rechercher_button.setObjectName(u"rechercher_button")
        self.rechercher_button.setGeometry(QRect(420, 100, 80, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 31, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 20, 31, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 20, 31, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 20, 31, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(540, 20, 31, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(590, 20, 31, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(490, 20, 31, 16))
        self.supprimer_button = QPushButton(self.centralwidget)
        self.supprimer_button.setObjectName(u"supprimer_button")
        self.supprimer_button.setGeometry(QRect(600, 100, 80, 23))
        self.corps_text_input = QLineEdit(self.centralwidget)
        self.corps_text_input.setObjectName(u"corps_text_input")
        self.corps_text_input.setGeometry(QRect(290, 40, 21, 23))
        self.tete_text_input = QLineEdit(self.centralwidget)
        self.tete_text_input.setObjectName(u"tete_text_input")
        self.tete_text_input.setGeometry(QRect(330, 40, 21, 23))
        self.antenne_text_input = QLineEdit(self.centralwidget)
        self.antenne_text_input.setObjectName(u"antenne_text_input")
        self.antenne_text_input.setGeometry(QRect(380, 40, 21, 23))
        self.bras_text_input = QLineEdit(self.centralwidget)
        self.bras_text_input.setObjectName(u"bras_text_input")
        self.bras_text_input.setGeometry(QRect(430, 40, 21, 23))
        self.jambes_text_input = QLineEdit(self.centralwidget)
        self.jambes_text_input.setObjectName(u"jambes_text_input")
        self.jambes_text_input.setGeometry(QRect(480, 40, 21, 23))
        self.doigts_text_input = QLineEdit(self.centralwidget)
        self.doigts_text_input.setObjectName(u"doigts_text_input")
        self.doigts_text_input.setGeometry(QRect(530, 40, 21, 23))
        self.yeux_text_input = QLineEdit(self.centralwidget)
        self.yeux_text_input.setObjectName(u"yeux_text_input")
        self.yeux_text_input.setGeometry(QRect(580, 40, 21, 23))
        self.output_field = QTextEdit(self.centralwidget)
        self.output_field.setObjectName(u"output_field")
        self.output_field.setGeometry(QRect(280, 140, 401, 401))
        self.table_visualizer = QTextEdit(self.centralwidget)
        self.table_visualizer.setObjectName(u"table_visualizer")
        self.table_visualizer.setGeometry(QRect(10, 10, 261, 531))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 733, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        self.inserer_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.inserer_button.setText(QCoreApplication.translate("MainWindow", u"Ins\u00e9rer", None))
#if QT_CONFIG(accessibility)
        self.rechercher_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.rechercher_button.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"J", None))
#if QT_CONFIG(accessibility)
        self.supprimer_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.supprimer_button.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
    # retranslateUi

