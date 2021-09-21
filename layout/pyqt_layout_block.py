import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class ExampleBlockLayoutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        ok_button = QPushButton('ok')
        ok_button.clicked.connect(self.close)
        cancel_button = QPushButton('cancel')
        cancel_button.clicked.connect(self.close)
        cancel_button.setShortcut('Ctrl+Q')

        h_box = QHBoxLayout()
        h_box.addStretch(1)  # растяжение, свободное пространство перед кнопками, убрать, кнопки будут по ширине экрана
        h_box.addWidget(ok_button)
        h_box.addWidget(cancel_button)

        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Block layout example')


def main(args):
    app = QApplication(args)
    example = ExampleBlockLayoutWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
