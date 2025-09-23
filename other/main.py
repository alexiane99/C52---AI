import sys

from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import ( QApplication
                              , QWidget
                              , QLabel
                              , QPushButton
                              , QScrollBar
                              , QVBoxLayout
                              , QHBoxLayout
                              , QGroupBox
                              , QMainWindow)

from gol import GOLEngine


class GOLCanvas(QWidget):
    
    def __init__(self, engine: GOLEngine, parent=None):
        super().__init__(parent)
        self.__engine = engine
        self.setMinimumSize(QSize(520, 520))
        self.__vivant_brush = QBrush(QColor(255, 255, 255))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0))

        fenetre = self.rect()
        col, row = self.__engine.width, self.__engine.height
        if col <= 0 or row <= 0 or fenetre.width() <= 0 or fenetre.height() <= 0:
            painter.end()
            return

        width_colonne = fenetre.width() / col
        height_colonne = fenetre.height() / row

        painter.setBrush(self.__vivant_brush)
        painter.setPen(Qt.NoPen)

        for x in range(col):
            x1 = int(fenetre.left() + x * width_colonne)
            x2 = int(fenetre.left() + (x + 1) * width_colonne)
            w = x2 - x1
            if w <= 0:
                continue
            for y in range(row):
                if self.__engine.cell_value(x, y):
                    y1 = int(fenetre.top() + y * height_colonne)
                    y2 = int(fenetre.top() + (y + 1) * height_colonne)
                    h = y2 - y1
                    if h > 0:
                        painter.fillRect(x1, y1, w, h, self.__vivant_brush)

        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__engine = GOLEngine(100, 100) # hardcoder ici pour ta grlle
        self.__engine.randomize(0.85)

        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.__tick)

        self.__canvas = GOLCanvas(self.__engine)

        self.__btn_start_stop = QPushButton("Start")
        self.__btn_step = QPushButton("step")
        self.__speed_bar = QScrollBar(Qt.Horizontal)
        self.__speed_bar.setRange(1, 10)
        self.__speed_bar.setSingleStep(1)
        self.__speed_bar.setPageStep(1)
        self.__speed_bar.setValue(1)
        self.__lbl_speed = QLabel("x1")

        control_box = self.__controle_fenetre()

        self.__label_generation = QLabel("0")
        self.__label_alive = QLabel("0")
        self.__label_dead = QLabel("0")

        info_box = self.__info_fenetre()

        root = QWidget()
        h = QHBoxLayout(root)
        h.addWidget(control_box, 0, Qt.AlignTop)
        h.addWidget(self.__canvas, 1)
        h.addWidget(info_box, 0, Qt.AlignBottom)
        self.setCentralWidget(root)

        self.__btn_start_stop.clicked.connect(self.__signal_start)
        self.__btn_step.clicked.connect(self.__step)
        self.__speed_bar.valueChanged.connect(self.__change_vitesse)

        self.__update_vitesse_label(1)

    def __controle_fenetre(self):
        control = QGroupBox("Control")
        v = QVBoxLayout(control)
        v.addWidget(self.__btn_start_stop)
        v.addWidget(self.__btn_step)
        v.addSpacing(8)
        v.addWidget(QLabel("Speed:"))
        v.addWidget(self.__speed_bar)
        v.addWidget(self.__lbl_speed)
        v.addStretch(1)
        return control

    def __info_fenetre(self):
        info = QGroupBox("Information")
        v = QVBoxLayout(info)
        v.addWidget(QLabel("Generation:"))
        v.addWidget(self.__label_generation)
        v.addSpacing(6)
        v.addWidget(QLabel("Alive:"))
        v.addWidget(self.__label_alive)
        v.addSpacing(6)
        v.addWidget(QLabel("Dead:"))
        v.addWidget(self.__label_dead)
        v.addStretch(1)
        return info

    def __vitesse_a_ms(self, x_vitesse):
        return max(12, int(round(120 / x_vitesse)))

    def __change_vitesse(self, x_vitesse):
        self.__update_vitesse_label(x_vitesse)
        if self.__timer.isActive():
            self.__start(self.__vitesse_a_ms(x_vitesse))

    def __update_vitesse_label(self, x_vitesse):
        self.__lbl_speed.setText(f"x{x_vitesse}")

    def __signal_start(self):
        if self.__timer.isActive():
            self.__stop()
        else:
            self.__start(self.__vitesse_a_ms(self.__speed_bar.value()))

    def __start(self, interval_ms: int):
        self.__timer.start(interval_ms)
        self.__btn_start_stop.setText("stop")

    def __stop(self):
        self.__timer.stop()
        self.__btn_start_stop.setText("start")

    def __step(self):
        is_running = self.__timer.isActive()
        if is_running:
            self.__timer.stop()
        self.__tick()
        if is_running:
            self.__timer.start()

    def __tick(self):
        self.__engine.process()
        self.__canvas.update()
        total = self.__engine.width * self.__engine.height
        vivant = sum(
            self.__engine.cell_value(x, y)
            for x in range(self.__engine.width)
            for y in range(self.__engine.height)
        )
        dead = total-vivant
        self.__label_generation.setText(str(int(self.__label_generation.text())+1))
        self.__label_alive.setText(f"{vivant} ({vivant/total:.1%})")
        self.__label_dead.setText(f"{dead} ({dead/total:.1%})")


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
