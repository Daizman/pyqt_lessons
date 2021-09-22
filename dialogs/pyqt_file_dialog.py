import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QAction
from PyQt5.QtGui import QIcon


class ExampleFileDialogWindow(QMainWindow):
    def __init__(self):
        super(ExampleFileDialogWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction(QIcon('../resources/remove-button.png'), '&Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new file')
        open_file.triggered.connect(self.show_dialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('File dialog example')

    def show_dialog(self):
        f_name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        with open(f_name, encoding='UTF-8') as f:
            self.text_edit.setText(f.read())


def main(args):
    app = QApplication(args)
    example = ExampleFileDialogWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
