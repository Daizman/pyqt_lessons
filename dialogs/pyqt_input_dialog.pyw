import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QPushButton


class ExampleInputDialogWindow(QWidget):
    def __init__(self):
        super(ExampleInputDialogWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.button = QPushButton('Show dialog', self)
        self.button.move(30, 20)
        self.button.clicked.connect(self.show_dialog)

        self.le = QLineEdit(self)
        self.le.move(130, 20)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Input dialog example')

    def show_dialog(self):
        text, status = QInputDialog.getText(self, 'Input dialog', 'Enter your name')

        if status:
            self.le.setText(text)


def main(args):
    app = QApplication(args)
    example = ExampleInputDialogWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
