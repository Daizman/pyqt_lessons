import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer, QTimerEvent


class ExampleProgressBarWindow(QWidget):
    def __init__(self):
        super(ExampleProgressBarWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 200, 25)

        self.button = QPushButton('Start', self)
        self.button.move(40, 80)
        self.button.clicked.connect(self.do_action)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Progress bar example')

    def timerEvent(self, a0: 'QTimerEvent') -> None:
        if self.step >= 100:
            self.timer.stop()
            self.button.setText('Finished')
            return

        self.step += 1
        self.progress_bar.setValue(self.step)

    def do_action(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            self.timer.start(100, self)  # таймаут, и объект, который будет принимать события
            self.button.setText('Stop')


def main(args):
    app = QApplication(args)
    example = ExampleProgressBarWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
