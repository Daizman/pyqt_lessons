import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class ExampleAbsoluteLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        label1 = QLabel('Zetcode', self)
        label1.move(15, 10)

        label2 = QLabel('tutorials', self)
        label2.move(35, 40)

        label3 = QLabel('for programmers', self)
        label3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute layout example')


def main(args):
    app = QApplication(args)
    example = ExampleAbsoluteLayoutWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
