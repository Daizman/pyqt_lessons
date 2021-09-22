import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class ExampleEventSenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        button1 = QPushButton('Button 1', self)
        button1.move(30, 50)

        button2 = QPushButton('Button 2', self)
        button2.move(150, 50)

        button1.clicked.connect(self.button_clicked)
        button2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Event sender example')

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(f'{sender.text()} was pressed')


def main(args):
    app = QApplication(args)
    example = ExampleEventSenderWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
