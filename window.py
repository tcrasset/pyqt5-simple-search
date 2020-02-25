import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextBrowser, QMainWindow
from PySide2.QtCore import QFile, Slot
from ui_mainwindow import Ui_MainWindow
# from PyQt5.QtGui import *
# from PyQt5.QtCore import QFile
# from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


@Slot()
def say_hello():
    print("Button clicked, Hello!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    central_widget = window.findChild(QWidget, "centralwidget")

    inserer_button = central_widget.findChild(QPushButton,"inserer_button")
    rechercher_button = central_widget.findChild(QPushButton,"rechercher_button")
    supprimer_button = central_widget.findChild(QPushButton,"supprimer_button")

    nom_bonhomme = central_widget.findChild(QLineEdit,"nom_bonhomme")
    output_box = central_widget.findChild(QTextBrowser,"output_box")
    
    corps_text_input = central_widget.findChild(QLineEdit,"corps_text_input")
    tete_text_input = central_widget.findChild(QLineEdit,"tete_text_input")
    antenne_text_input = central_widget.findChild(QLineEdit,"antenne_text_input")
    bras_text_input = central_widget.findChild(QLineEdit,"bras_text_input")
    jambes_text_input = central_widget.findChild(QLineEdit,"jambes_text_input")
    doigts_text_input = central_widget.findChild(QLineEdit,"doigts_text_input")
    yeux_text_input = central_widget.findChild(QLineEdit,"yeux_text_input")

    inserer_button.clicked.connect(say_hello())

    

    # widget = loader.ui.findChild(QPushButton, "button")
    # widget.returnPressed.connect(self.return_pressed)


    sys.exit(app.exec_())
