import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main(args):
    app = QApplication(args)

    widget = QWidget()
    widget.resize(250, 250)
    widget.move(300, 300)
    widget.setWindowTitle('Simple example')
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
