import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class ExampleComboboxWindow(QWidget):
    def __init__(self):
        super(ExampleComboboxWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Ubuntu', self)

        combo = QComboBox(self)
        combo.addItems(['Ubuntu',
                        'Mandriva',
                        'Fedora',
                        'Arch',
                        'Gentoo'])
        combo.move(40, 40)
        self.label.move(40, 140)

        combo.activated[str].connect(self.on_activated)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Combobox example')

    def on_activated(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main(args):
    app = QApplication(args)
    example = ExampleComboboxWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
