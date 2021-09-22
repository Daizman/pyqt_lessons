import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate


class ExampleCalendarWindow(QWidget):
    def __init__(self):
        super(ExampleCalendarWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.move(20, 20)
        calendar.clicked[QDate].connect(self.show_date)

        self.label = QLabel(self)
        date = calendar.selectedDate()
        self.label.setText(date.toString('yyyy-dd-MM'))
        self.label.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar example')

    def show_date(self, date):
        self.label.setText(date.toString())


def main(args):
    app = QApplication(args)
    example = ExampleCalendarWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
