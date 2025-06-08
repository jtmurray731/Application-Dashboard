from PyQt5.QtWidgets import QApplication
import sys

from gui import MainWindow


app = QApplication(sys.argv)

window = MainWindow()
window.show()





if __name__ == '__main__':
    app.exec_()