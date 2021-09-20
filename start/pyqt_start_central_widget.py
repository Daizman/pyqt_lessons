import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class ExampleCentralWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.resize(300, 300)
        self.center()

        self.setWindowTitle('Central widget example')

    def center(self):
        frame_geometry = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center)
        self.move(frame_geometry.topLeft())


def main(args):
    app = QApplication(args)
    example = ExampleCentralWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
