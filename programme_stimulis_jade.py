import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextBrowser, QMainWindow, QTextEdit
from PySide2.QtCore import QFile, Slot
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, filename : str):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = filename
        self.getChildren()
        
        self.rechercher_button.clicked.connect(self.check_if_in_table)
        self.inserer_button.clicked.connect(self.add_in_table)
        self.supprimer_button.clicked.connect(self.delete_from_table)

        self.output_field.setReadOnly(True)
        self.output_field.append("Messages :\n")

        self.table_visualizer.setReadOnly(True)
        self.visualize_table()

        self.show()


    def getChildren(self):
            self.central_widget = self.findChild(QWidget, "centralwidget")
            
            self.inserer_button = self.central_widget.findChild(QPushButton,"inserer_button")
            self.rechercher_button = self.central_widget.findChild(QPushButton,"rechercher_button")
            self.supprimer_button = self.central_widget.findChild(QPushButton,"supprimer_button")
            
            self.output_field = self.central_widget.findChild(QTextEdit,"output_field")
            self.table_visualizer = self.central_widget.findChild(QTextEdit,"table_visualizer")
            
            self.corps_text_input = self.central_widget.findChild(QLineEdit,"corps_text_input")
            self.tete_text_input = self.central_widget.findChild(QLineEdit,"tete_text_input")
            self.antenne_text_input = self.central_widget.findChild(QLineEdit,"antenne_text_input")
            self.bras_text_input = self.central_widget.findChild(QLineEdit,"bras_text_input")
            self.jambes_text_input = self.central_widget.findChild(QLineEdit,"jambes_text_input")
            self.doigts_text_input = self.central_widget.findChild(QLineEdit,"doigts_text_input")
            self.yeux_text_input = self.central_widget.findChild(QLineEdit,"yeux_text_input")

    def visualize_table(self):

        self.table_visualizer.setText("Ficher texte \"{}\" :\n".format(filename))

        with open(self.filename, "r") as table:
            for line in table.readlines():
                entry_as_list = line.replace("\n", '').split(",")[:-1]
                self.table_visualizer.append("{}".format(entry_as_list))


    def _get_input_list(self) -> list:
        input_list = []

        input_list.append(self.corps_text_input.text())
        input_list.append(self.tete_text_input.text())
        input_list.append(self.antenne_text_input.text())
        input_list.append(self.bras_text_input.text())
        input_list.append(self.jambes_text_input.text())
        input_list.append(self.doigts_text_input.text())
        input_list.append(self.yeux_text_input.text())

        new_list = []
        for val in input_list:
            if(val == ''):
                new_list.append('0')
            else:
                new_list.append(val)

        return new_list


    def check_if_in_table(self, input_list : list = None, standalone : bool = True) -> bool:
        """
        Function that checks whether a given input_list is already in the table.
        Can be called either by itself, in this case the boolean outputdoesn't matter but an 
        output is produced on the GUI.
        Or it is called by the methods add_to_table() or _delete_from_table() where the boolean
        value is used but there is no output on the GUI.

        """
        print("In function check_if_in_table()")
        
        if(not input_list):
            input_list = self._get_input_list()

        print("Input list is {}".format(input_list))

        is_numeric = self._is_input_numeric(input_list)

        if(not is_numeric and standalone):
            print("ERROR, INPUT IS NOT NUMERIC")
            self.output_field.append("{} n'est pas valide. Reessayez (chiffres uniquement).".format(input_list))
        else:
            with open(self.filename, "r") as table:
                print("Opening file")
                for line in table.readlines():
                    entry_as_list = line.replace("\n", '').split(",")[:-1]
                    if(input_list == entry_as_list):
                        print("{} is present in table".format(input_list))
                        if(standalone): # Write only when check_if_in_table is called by itself
                            self.output_field.append("{} est déjà présent dans la table".format(input_list))

                        return True
                if(standalone):
                    self.output_field.append("{} n'est pas présent dans la table".format(input_list))

        return False



    def add_in_table(self):
        print("In function add_in_table()")
        input_list = self._get_input_list()
        print("Input list is {}".format(input_list))

        if(self.check_if_in_table(input_list, False)):
            print("{} already in table. Aborting...".format(input_list))
            self.output_field.append("{} est déjà présent dans la table. Abandon...".format(input_list))

        else:
            with open(self.filename, "a") as table:
                status = self._add_one_line(table, input_list)
                if(status):
                    self.output_field.append("{} inséré.".format(input_list))
            self.visualize_table()



    def _is_input_numeric(self, input_list) -> bool:
        write_line = True

        # Check if everything is correct with the input list
        for input in input_list:
            write_line = write_line and input.isnumeric()
        return write_line
            

    def _add_one_line(self, file, input_list) -> bool:
        # Check if everything is correct with the input list
        is_numeric = self._is_input_numeric(input_list)
       
        # If correct, write to file
        if(is_numeric):
            for input in input_list:
                file.write("{},".format(int(input)))
            file.write("\n")
            print("Inserted {}".format(input_list))


        # Else, print error
        else:
            print("ERROR, INPUT IS NOT NUMERIC")
            self.output_field.append("{} n'est pas valide. Reessayez (chiffres uniquement).".format(input_list))

        return is_numeric # Report status




    def delete_from_table(self):
        print("In function delete_from_table()")
        input_list = self._get_input_list()

        if(not self._is_input_numeric(input_list)):
            print("ERROR, INPUT IS NOT NUMERIC")
            self.output_field.append("{} n'est pas valide. Reessayez (chiffres uniquement).".format(input_list))
            return

        all_entries = []

        if(self.check_if_in_table(input_list, False)):
            print("Deleting {}".format(input_list))
            self.output_field.append("{} supprimé.".format(input_list))

            # Reading all line from file and converting them to a list
            with open(self.filename, "r") as table:
                for line in table.readlines():
                    all_entries.append(line.replace("\n", '').split(",")[:-1])
                    print(line)
            # Re-opening the same file and writing back every item except
            # the input_list that we want to delete
            with open(self.filename, "w") as table:
                for entry in all_entries:
                    if(entry != input_list):
                        print("Writing {} to file".format(entry))
                        self._add_one_line(table, entry)

            self.visualize_table()
        else:
            print("{} not in file".format(input_list))
            self.output_field.append("{} n'est PAS présent dans la table. Abandon...".format(input_list))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # filename = sys.argv[1]
    filename = 'tables.txt'
    window = MainWindow(filename)

    sys.exit(app.exec_())
