from PyQt5.QtWidgets import QToolBar, QVBoxLayout, QWidget, QMainWindow, QAction
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window setup
        self.setWindowTitle("Job Application Dashboard")
        # self.setMinimumSize(QSize(400, 200))
        # self.setMaximumSize(QSize(800, 600))

        layout = QVBoxLayout()

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # toolbar buttons
        new_record = QAction("New Record", self)
        new_record.triggered.connect(self.create_new_record)
        toolbar.addAction(new_record)


        # other widgets



        # keep this always
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # new record button signal
    def create_new_record(self, s):
        print("New record created", s)