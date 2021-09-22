import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class ExampleLineEditWindow(QWidget):
    def __init__(self):
        super(ExampleLineEditWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel(self)
        line_edit = QLineEdit(self)

        line_edit.move(60, 100)
        self.label.move(60, 40)

        line_edit.textChanged[str].connect(self.on_change)
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Line edit example')

    def on_change(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main(args):
    app = QApplication(args)
    example = ExampleLineEditWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
