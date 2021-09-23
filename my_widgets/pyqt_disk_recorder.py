import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QPaintEvent, QFont, QColor, QPen


class Communicate(QObject):
    update_bw = pyqtSignal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super(BurningWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setMinimumSize(1, 30)
        self.__value = 75
        self.numbers = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    value = property(get_value, set_value)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        self.draw_widget(painter)
        painter.end()

    def draw_widget(self, painter):
        font = QFont('Serif', 7, QFont.Light)
        painter.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10))

        till = int((w / 750) * self.value)
        full = int((w / 750) * 700)

        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(QColor(255, 255, 125))
        if self.value >= 700:
            painter.drawRect(0, 0, full, h)

            painter.setPen(QColor(255, 175, 175))
            painter.setBrush(QColor(255, 175, 175))
            painter.drawRect(full, 0, till - full, h)
        else:
            painter.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)

        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(0, 0, w - 1, h - 1)

        for j, i in enumerate(range(step, 10 * step, step)):
            painter.drawLine(i, 0, i, 5)
            metrics = painter.fontMetrics()
            fw = metrics.width(str(self.numbers[j]))
            painter.drawText(i - fw / 2, h / 2, str(self.numbers[j]))


class ExampleWindowWithBurningWidget(QWidget):
    def __init__(self):
        super(ExampleWindowWithBurningWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setRange(1, 750)
        slider.setValue(75)
        slider.setGeometry(30, 40, 150, 30)

        self.communicate = Communicate()
        self.burning_widget = BurningWidget()
        # коннектим коммуникацию на вызов сеттера у нашего виджета
        self.communicate.update_bw[int].connect(self.burning_widget.set_value)

        # коннектим изменение слайдера к вызову метода для изменения значения
        slider.valueChanged[int].connect(self.change_value)
        h_box = QHBoxLayout()
        h_box.addWidget(self.burning_widget)
        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Simple my widget usage example')

    def change_value(self, value):
        # вызываем срабатывание сигнала
        self.communicate.update_bw.emit(value)
        # перерисовываем виджет после нового значения
        self.burning_widget.repaint()


def main(args):
    app = QApplication(args)
    example = ExampleWindowWithBurningWidget()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
