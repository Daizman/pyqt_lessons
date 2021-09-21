import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QLabel, QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        title_le = QLineEdit()
        author_le = QLineEdit()
        review_te = QTextEdit()

        grid.setSpacing(10)  # промежуток между виджетами

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_le, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_le, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_te, 3, 1, 5, 1)  # объединяет 5 строк в 1 столбце

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Example')


def main(args):
    app = QApplication(args)
    example = Example()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
