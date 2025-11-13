import sys
import numpy as np 
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
        self.__engine.randomize(0.5)

        self.__canvas = GOLCanvas(self.__engine)
        self.__gol_app = QHBoxLayout() # pour contenir toute l'app 
        self.__gol_view = QLabel()
        self.__gol_control = QLabel() #widget contrôle
        self.__gol_info = QLabel() #widget infos

        view = self.__create_layout(self.__gol_view, 900, 600, 'Vue', 0) #crée le widget selon tous ses parametres
        control = self.__create_layout(self.__gol_control, 250, 150, 'Contrôle', 2)
        info = self.__create_layout(self.__gol_info, 250, 150, 'Info', 1) 

        self.__update_view(self.__gol_view, 0, 0, 0) #noir
        self.__update_view(self.__gol_control, 135, 206, 250) #bleu
        self.__update_view(self.__gol_info, 255, 165, 0) #orange

        self.__gol_app.addLayout(view) #ajoute les layout créées au main
        self.__gol_app.addLayout(control)
        self.__gol_app.addLayout(info)

        self.setLayout(self.__gol_app)


    def __create_layout(self, element, width, height, texte, indice):

        title = QLabel()
        title.setText(texte)
        title.setFixedWidth(width)

        element.setFixedWidth(width)
        element.setFixedHeight(height)
        element.setMinimumWidth(width)
        element.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()

        if(indice == 1):
            layout.addStretch()

        layout.addWidget(title)
        layout.addWidget(element)

        #layout.addWidget(self.__texte.setText(texte)) ?? insertion de texte? 

        if(indice == 2):
            layout.addStretch()
        
        return layout
    
    def __update_view(self, color_widget, r, g, b):
        image = QPixmap(color_widget.size())
        image.fill(QColor(r, g, b))
        color_widget.setPixmap(image)


    
    def __tick(self):
        self.__engine.processing()
        self.__canvas.update()

def main():
    app = QApplication(sys.argv)

    w = MainWindow()
    w.__tick()
    w.show()
    sys.exit(app.exec())
   

if __name__ == '__main__':
    main()