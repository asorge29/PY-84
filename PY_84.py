from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from ti84_window import Ui_py84_Window

class PY84(QWidget, Ui_py84_Window):
    def __init__(self):
        super().__init__()
        self._setupUI()
        self.currentEquation = ''

    def _setupUI(self):
        self.setupUi(self)

    def _connectButtonSignalsNormal(self):
        pass

    def _insertNumber(self, number, index=int):
        pass