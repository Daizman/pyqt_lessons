import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog


class ExampleFontDialogWindow(QWidget):
    def __init__(self):
        super(ExampleFontDialogWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()

        button = QPushButton('Pick font', self)
        button.move(20, 20)
        button.clicked.connect(self.show_dialog)
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        v_box.addWidget(button)

        self.label = QLabel('Test label', self)
        self.label.move(130, 20)

        v_box.addWidget(self.label)
        self.setLayout(v_box)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog example')

    def show_dialog(self):
        font, status = QFontDialog.getFont()
        if status:
            self.label.setFont(font)


def main(args):
    app = QApplication(args)
    example = ExampleFontDialogWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
