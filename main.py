from PyQt5.QtWidgets import QApplication
import sys
from PY_84 import PY84

def main():
    app = QApplication(sys.argv)
    win = PY84()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()