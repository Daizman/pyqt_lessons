import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLCDNumber
from PyQt5.QtCore import Qt


class ExampleSignalAndSlotsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        v_box = QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(sld)

        self.setLayout(v_box)
        sld.valueChanged.connect(lcd.display)  # присоединяем сигнал valueChange к слоту lcd.display
        # отправитель - объект, который посылает сигнал, sld
        # получатель - объект, который получает сигнал, lcd
        # слот - метод, который реагирует на сигнал, display

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slots example')


def main(args):
    """
    Для работы с событиями PyQt5 имеет уникальный механизм сигналов и слотов.
    Сигналы и слоты используются для связи между объектами.
    Сигнал срабатывает тогда, когда происходит конкретное событие.
    Слот может быть любой функцией. Слот вызывается, когда срабатывает его сигнал.
    :param args:
    :return:
    """
    app = QApplication(args)
    example = ExampleSignalAndSlotsWindow()
    example.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
