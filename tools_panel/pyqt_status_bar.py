import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class ExampleStatusBarWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Status bar example')


def main(args):
    app = QApplication(args)
    example = ExampleStatusBarWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
