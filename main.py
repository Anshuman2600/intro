# Now we will start workin with PyQT5 GUI
# GUI means Graphical User Interface

import sys # System-specific parameters and functions
# This module provides access to some variables used or maintained by 
# the interpreter and to functions that interact strongly with the interpreter. It is always available.

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # QLabel for labelling things like on our window
# import following module to work with icon
from PyQt5.QtGui import QIcon


#Boiler plate code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #title of window
        self.setWindowTitle("FirstGUI")
        # set size of window and its location
        self.setGeometry(700, 200, 500, 500)
        # for window icon
        self.setWindowIcon(QIcon("icon.jpg"))
        
def main():
    # code for getting window
    app = QApplication(sys.argv)
    # if using command line or terminal prompt
    # sys.argv: The list of command line arguments passed to a Python script.argv[0]
    # is the script name(it is operating system dependent whether this a full pathname or not). If the command
    # was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no
    # script name was passed to the Python interpreter.argv[0] is the empty string.
    window = MainWindow() # Default method of our show is to hide the window
    window.show()
    sys.exit(app.exec_()) 








if __name__ == "__main__":
    main()
