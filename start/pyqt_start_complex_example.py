import sys
from PyQt5.QtWidgets import QApplication, QWidget


class ExampleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Complex Example')


def main(args):
    app = QApplication(args)
    example = ExampleWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
