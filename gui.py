from PyQt5.QtWidgets import QToolBar, QVBoxLayout, QWidget, QMainWindow, QAction
from PyQt5.QtCore import QSize
from color_widget import Color

from record import Record

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window setup
        self.setWindowTitle("Job Application Dashboard")

        self.setMinimumSize(QSize(800, 400))
        # self.setMaximumSize(QSize(1000, 500))

        # main view will be toolbar at the top
        # and 2 main widget panes
        # top one for records
        # bottom one reserved for future info?

        # each pane should span the window horizontally
        layout = QVBoxLayout()

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # toolbar buttons
        new_record = QAction("New Record", self)
        new_record.triggered.connect(Signal.create_new_record)
        toolbar.addAction(new_record)


        # other widgets
        records = ScrollablePane()
        layout.addWidget(records)

        # for now, this is just filled in with a solid background
        # to distinguish it from the other widget pane
        reserved = Color('light grey')
        layout.addWidget(reserved)

        # keep this always
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# class meant to organize all signal methods in one place
# could split this out into a signals.py and just import signals
# instead of a class using only static methods
class Signal:
    @staticmethod
    def create_new_record(s):
        print("Creating new record", s)

class ScrollablePane(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # records within scrollable pane


