import sys
import numpy as np 
import keyboard 
from GOLEngine_numpy import GOLEngine
from PySide6.QtCore import Qt, QRect, QPoint, QSize, QTimer, SIGNAL
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush, QPen, QImage
from PySide6.QtWidgets import (QApplication # type: ignore
                                , QWidget 
                                , QLabel 
                                , QScrollBar
                                , QHBoxLayout
                                , QVBoxLayout
                                , QTextEdit
                                , QMainWindow
                                , QPushButton
                                , QGroupBox
                                
                            
                                
                                )

class GOLCanvas(QWidget):
    def __init__(self, engine, parent=None):
        super().__init__(parent)
        self.__engine = engine
        self.setMinimumSize(QSize(520, 520))

    def paintEvent(self, _):
        # dimy, dimx = self.__engine.all_cells 
        dimy, dimx = self.__engine.height, self.__engine.width

        if dimy <= 0 or dimx <= 0:
            return 

        screen = QImage(dimx, dimy, QImage.Format_RGB32)
        screen.fill(QColor(0,0,0)) #est noir à la base 

        for y in range(dimy):
            for x in range(dimx):
                if self.__engine.cell_value(x,y):
                    screen.setPixelColor(x,y, QColor(255,255,255))
        
        pix = QPixmap.fromImage(screen)
        scaled = pix.scaled(self.rect().size())

        p = QPainter(self)
        p.fillRect(self.rect(), QColor(0,0,0))
        p.drawPixmap(self.rect().topLeft(), scaled)
        p.end()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.__engine = GOLEngine(250,250)
        self.__engine.set_rules((2,3), (3,))
        self.__engine.randomize(0.15)
        
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.__tick)
        #self.__timer.start(100)

        self.__canvas = GOLCanvas(self.__engine)
        
        #Layout principaux
        #self.__gol_app = QHBoxLayout() # pour contenir toute l'app 
        
        #GOL engine view 
        #viewLayout = QVBoxLayout()
        #viewLayout.addWidget(self.__canvas)
        
        # Pour le control panel 
        self.__btn_start_stop = QPushButton("Start")
        self.__btn_step = QPushButton("step")
        self.__speed_bar = QScrollBar(Qt.Horizontal)
        self.__speed_bar.setRange(1,10)
        self.__speed_bar.setSingleStep(1)
        self.__speed_bar.setPageStep(1)
        self.__speed_bar.setValue(1)
        self.__label_speed = QLabel("x1")
        control_panel = self.__set_control_panel() 
        
        # Control panel & Infos 
        # self.__gol_control = QLabel("Control") #widget contrôle
        # self.__gol_control.setAlignment(Qt.AlignCenter)
        # self.__gol_control.setFixedWidth(250)
        # self.__gol_control.setFixedHeight(150)
        # self.__gol_control.setMinimumWidth(250)
        # self.__gol_control.setAlignment(Qt.AlignCenter)
        # controlLayout = QVBoxLayout()
        # controlLayout.addWidget(self.__gol_control)
        
        #Pour le info panel 
        self.__label_generation = QLabel("0")
        self.__label_generation.setFixedWidth(100)
        self.__label_alive = QLabel("0")
        self.__label_alive.setFixedWidth(100)
        self.__label_dead = QLabel("0")
        self.__label_dead.setFixedWidth(100)
        
        info_panel = self.__set_info_panel()
        
        # self.__gol_info = QLabel("Info") #widget infos
        # self.__gol_info.setAlignment(Qt.AlignCenter)
        # self.__gol_info.setFixedWidth(250)
        # self.__gol_info.setFixedHeight(150)
        # self.__gol_info.setMinimumWidth(250)
        # self.__gol_info.setAlignment(Qt.AlignCenter)
        # infoLayout = QVBoxLayout()
        # infoLayout.addWidget(self.__gol_info)

        #crée le widget selon tous ses parametres
        #control = self.__create_layout(self.__gol_control, 250, 150, 'Contrôle', 2)
        #info = self.__create_layout(self.__gol_info, 250, 150, 'Info', 1) 

        #self.__update_view(self.__gol_control, 135, 206, 250) #bleu
        #self.__update_view(self.__gol_info, 255, 165, 0) #orange 

       
        # self.__gol_app.addLayout(controlLayout, stretch=1)
        # self.__gol_app.addLayout(viewLayout, stretch=3)
        # self.__gol_app.addLayout(infoLayout, stretch=1)

        main = QWidget()
        main_app = QHBoxLayout(main)
        main_app.addWidget(control_panel, 0, Qt.AlignTop)
        main_app.addWidget(self.__canvas, 1)
        main_app.addWidget(info_panel, 0, Qt.AlignBottom)
        #main.setLayout(self.__gol_app)
        self.setCentralWidget(main)
        
        self.__btn_start_stop.clicked.connect(self.__signal_start)


    def __set_control_panel(self):
        control = QGroupBox("Control")
        c = QVBoxLayout(control)
        c.addWidget(self.__btn_start_stop)
        c.addWidget(self.__btn_step)
        c.addSpacing(8)
        c.addWidget(QLabel("Speed:"))
        c.addWidget(self.__speed_bar)
        c.addWidget(self.__label_speed)
        c.addStretch(1)
        return control 
    
    def __set_info_panel(self):
        info = QGroupBox("Information")
        i = QVBoxLayout(info)
        i.addWidget(QLabel("Generation:"))
        i.addWidget(self.__label_generation)
        i.addSpacing(6)
        i.addWidget(QLabel("Alive:"))
        i.addWidget(self.__label_alive)
        i.addSpacing(6)
        i.addWidget(QLabel("Dead:"))
        i.addWidget(self.__label_dead)
        i.addStretch(1)
        return info 
    
    def __signal_start(self):
        if self.__timer.isActive():
            self.__stop()
        else:
            self.__start(self.__vitesse_a_ms(self.__speed_bar.value()))
    
    def __start(self, interval_ms):
        self.__timer.start(interval_ms)
        self.__btn_start_stop.setText("Stop")
    
    def __stop(self):
        self.__timer.stop()
        self.__btn_start_stop.setText("Start")
    
    def __vitesse_a_ms(self, x_vitesse):
        return max(12, int(round(120/x_vitesse)))
    
    # def __create_layout(self, element, width, height, texte, indice):

    #     title = QLabel()
    #     title.setText(texte)
    #     title.setFixedWidth(width)

    #     element.setFixedWidth(width)
    #     element.setFixedHeight(height)
    #     element.setMinimumWidth(width)
    #     element.setAlignment(Qt.AlignCenter)

    #     layout = QVBoxLayout()

    #     if(indice == 1):
    #         layout.addStretch()

    #     layout.addWidget(title)
    #     layout.addWidget(element)

    #     #layout.addWidget(self.__texte.setText(texte)) ?? insertion de texte? 

    #     if(indice == 2):
    #         layout.addStretch()
        
    #     return layout
    
    # def __update_view(self, color_widget, r, g, b):
    #     image = QPixmap(color_widget.size())
    #     image.fill(QColor(r, g, b))
    #     color_widget.setPixmap(image)

    def __tick(self):
        self.__engine.processing()
        self.__canvas.update()
        alive = self.__engine.cells_alive
        dead = self.__engine.cells_dead
        total = self.__engine.all_cells
        
        percent_alive = round((alive/total),4)
        percent_dead = round((dead/total),4)
        
        self.__label_alive.setText(f'{alive} ({percent_alive:.2%})')
        self.__label_dead.setText(f'{dead} ({percent_dead:.2%})')

def main():
    app = QApplication(sys.argv)
    
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
    
   
   

if __name__ == '__main__':
    main()