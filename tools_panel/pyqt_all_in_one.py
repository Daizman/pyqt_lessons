import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit
from PyQt5.QtGui import QIcon


class ExampleAllToolsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        exit_action = QAction(QIcon('../resources/remove-button.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        tool_bar = self.addToolBar('Exit')
        tool_bar.addAction(exit_action)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowIconText('All tools in one application')


def main(args):
    app = QApplication(args)
    example = ExampleAllToolsWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
