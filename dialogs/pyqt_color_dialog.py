import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog


class ExampleColorDialogWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        color = QColor(0, 0, 0)

        self.button = QPushButton('Change color', self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet("QWidget { background-color: %s }" % color.name())
        self.frame.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog example')

    def show_dialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.frame.setStyleSheet("QWidget { background-color: %s }" % color.name())
            # используются css таблицы стилей


def main(args):
    app = QApplication(args)
    example = ExampleColorDialogWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
