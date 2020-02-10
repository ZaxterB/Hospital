from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    label2 = QLabel('I am a stegosaurus!')
    label2.show()
    app.exec_()