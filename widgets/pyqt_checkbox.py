import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class ExampleCheckBoxWindow(QWidget):
    def __init__(self):
        super(ExampleCheckBoxWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        check_box = QCheckBox('Show title', self)  # self.check_box и не указать в QCheckBox self не прокатит
        check_box.move(20, 20)
        check_box.toggle()  # включем
        check_box.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 250, 280)
        self.setWindowTitle('QCheckBox')

    def change_title(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


def main(args):
    app = QApplication(args)
    example = ExampleCheckBoxWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
