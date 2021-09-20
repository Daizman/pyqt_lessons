import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class ExampleToolBarWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        exit_action = QAction(QIcon('../resources/remove-button.png'), '&Exit', self)
        exit_action.triggered.connect(qApp.quit)
        exit_action.setStatusTip('Exit application')  # работает только с установленным статус баром
        exit_action.setShortcut('Ctrl+Q')

        self.statusBar()  # первый вызов создает статус бар

        self.tool_bar = self.addToolBar('Exit')
        self.tool_bar.addAction(exit_action)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Tool bar example')


def main(args):
    app = QApplication(args)
    example = ExampleToolBarWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
