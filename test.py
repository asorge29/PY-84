import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

class CustomButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                border-radius: 5px, 20px, 5px, 5px;
            }
            QPushButton::indicator {
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 255, 0.3);
            }
            QPushButton:hover::bottom-left {
                position: absolute;
                bottom: -5px;
                left: -5px;
                width: 10px;
                height: 10px;
                background-color: rgba(0, 0, 0, 0.3);
                border-radius: 20px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Custom Button Example")
    window.resize(400, 200)  # Set the window size
    button = CustomButton("Click me", window)
    button.setGeometry(50, 50, 200, 100)  # Set the button position and size
    window.show()
    sys.exit(app.exec_())
