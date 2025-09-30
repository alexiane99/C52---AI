import sys, time
from GOLEngine_v2 import GOLEngine 
from PySide6.QtCore import Qt, QRect, QPoint, QSize, QTimer, SIGNAL
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush, QPen, QImage
from PySide6.QtWidgets import (QApplication # type: ignore
                                , QWidget 
                                , QLabel 
                                , QScrollBar
                                , QHBoxLayout
                                , QVBoxLayout
                                , QTextEdit
                                , QPushButton
                                
                            
                                
                                )

class GOLCanvas(QWidget): #CRÉATION D'UNE CLASSE POUR LA GESTION D'AFFICHAGE DU JEU
    
    def __init__(self, engine: GOLEngine, parent=None):
        super().__init__(parent)
        self.__engine = engine
        self.setMinimumSize(QSize(520, 520))
        self.__vivant_brush = QBrush(QColor(255, 255, 255))

    def paintEvent(self, event):

        height = self.__engine.height
        width = self.__engine.width
        
        image = QImage(width, height, QImage.Format_RGB32)

        image.fill(QColor(0,0,0)) #noir par défaut
    
        
        for y in range(height):
            for x in range(width):
                
                if(self.__engine.cell_value(x,y)): # == 1 donc vivant 
                    image.setPixelColor(x,y,QColor(255, 255,255))

        pixmap = QPixmap.fromImage(image)
        scale = pixmap.scaled(self.rect().size())

        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0,0,0))
        painter.drawPixmap(self.rect().topLeft(), scale)
        painter.end()
        
class Control_widget(QLabel):

    def __init__(self):
        self.pause_button = QPushButton("Pause", self)
        self.bystep_button = QPushButton("By Step", self)
        self.speed = QPushButton("Speed", self)
        self.is_running = True
        
        self.pause_button.clicked.connect(self.set_pause)
        self.bystep_button.clicked.connect(self.bystep_button)
        self.speed.clicked.connect(self.set_speed)

    def set_pause(self):
        
        #création d'une switch
        self.is_running = not self.is_running
            
        return self.is_running
        

    def set_bystep(self, waitingtime):
        return time.sleep(waitingtime)

    def set_speed():
        pass

class Info_widget(QWidget):

    def __init__(self):
        self.generation
        self.cell_count
        self.dead_count
        self.alive_count

class GOLApp(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        fixed_width = 250
        fixed_height = 250
        
        self.__gol_view = QLabel()
        self.__gol_app = QHBoxLayout() #pour contenir la vue
        self.__gol_control = QLabel() #widget contrôle
        self.__gol_info = QLabel() #widget infos
        self.__texte = QTextEdit()

        self.__gol_engine = GOLEngine(fixed_width, fixed_height)
        self.__canvas = GOLCanvas(self.__gol_engine)
        
        self.__is_running = True
        
        self.__controlWidget = Control_widget(self.__gol_control)

        view = self.__create_layout(self.__canvas, fixed_width, fixed_height, 'Vue', 0) #crée le widget selon tous ses parametres
        #view = self.__create_layout(self.__gol_view, fixed_width, fixed_height, 'Vue', 0)
        control = self.__create_layout(self.__gol_control, 250, 150, 'Contrôle', 2)
        info = self.__create_layout(self.__gol_info, 250, 150, 'Info', 1) 

        #applique la couleur aux widgets (c'est le widget qui est passé en paramètre et non son layout)
        self.__setView(self.__gol_view, 0, 0, 0) #noir
       
        #self.__update_viewGame(self.__gol_view, 900, 600)
        self.__setView(self.__gol_control, 135, 206, 250) #bleu
        self.__setView(self.__gol_info, 255, 165, 0) #orange

        self.__gol_app.addLayout(control)
        self.__gol_app.addLayout(view) #ajoute les layout créées au main
        self.__gol_app.addLayout(info)

        self.setLayout(self.__gol_app) #création du main layout avec tous ses components

        self.__gol_engine.randomize(0.75) #pour initialiser des cases au départ, sinon tous 0
        
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.__tick)
        #self.connect(self.__timer, SIGNAL('timeout()'), self.paintView(self.__gol_view, 4)) #tutorial YT: https://www.youtube.com/watch?v=xCAeoNAk2QA
        self.__timer.start()
        # self.__updateView() 
        

    def __create_layout(self, element, width, height, texte, indice): #permet la création du layout en fonction du widget 

        title = QLabel()
        title.setText(texte)
        title.setFixedWidth(width)


        # element.setFixedWidth(width)
        # element.setFixedHeight(height)
        #element.setMinimumWidth(width)
        

        layout = QVBoxLayout()

        if(indice == 1):
            layout.addStretch()

        layout.addWidget(title)
        layout.addWidget(element)

        #layout.addWidget(self.__texte.setText(texte)) ?? insertion de texte? 

        if(indice == 2):
            layout.addStretch()
        
        return layout

    def __setView(self, color_widget, r, g, b):

        image = QPixmap(color_widget.size())
        image.fill(QColor(r, g, b))
        color_widget.setPixmap(image)

    def __tick(self):
        
        while self.__is_running:
            self.__gol_engine.process()  # avance la simulation
            self.__canvas.update()
            #self.paintView(self.__gol_view)

    
    def paintView(self, widget): #crée une case dans le View 
        
        height = self.__gol_engine.height
        width = self.__gol_engine.width
        
        image = QImage(width, height, QImage.Format_RGB32)

        # image = QPixmap(widget.size())
        image.fill(QColor(0,0,0)) #noir par défaut
        
        #painter = QPainter(image)
        #painter.begin(self) #activer le painter; pas besoin vu qu'on utilise QPixmap
    
        
        for y in range(height):
            for x in range(width):
                
                if(self.__gol_engine.cell_value(x,y)): # == 1 donc vivant 
                    image.setPixelColor(x,y,QColor(255, 255,255))
                
                # code suggéré par AI 
                #pt1 correspondant au top_left de la case
                #x et y étant les indices des lignes et colonnes de la grille; size = taille de la case
                # pt1 = QPoint(x * size, y * size) 
                # case_size = QSize(size, size) #20, 20
                # case = QRect(pt1, case_size)
                
                # if self.__gol_engine._GOLEngine__grid[x][y] == 1: #pour qu'on aille cherche l'info dans la classe du modèle et non dans le constructeur
                    
                #     color = QColor(0,0,0)
    
                    
                # else:
                #     color = QColor(255,255,255)

                    # brush = QBrush()
                    # brush.setColor(255,255,255)
                


                # painter.setBrush(QBrush(color, Qt.SolidPattern)) #Qt.white
                
                # painter.fillRect(case, painter.brush())


        pixmap = QPixmap.fromImage(image)
        scale = pixmap.scaled(self.rect().size())

        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0,0,0))
        painter.drawPixmap(self.rect().topLeft(), scale)
        painter.end()

        # painter.end()
        # widget.setPixmap(image) 
        
    # def __updateView(self):
        
    #     # timer.timeout.connect(self.paintView(self.__gol_view, 20))
    #     self.connect(self.__timer, SIGNAL('timeout()'), self.paintView(self.__gol_view, 4)) #tutorial YT: https://www.youtube.com/watch?v=xCAeoNAk2QA
    #     self.__timer.start()
        
   
       
    
    # def print(self):
    #     for y in range(self.__height):
    #         for x in range(self.__width):
    #             print("█" if self.__grid[x][y] == 1 else " ", end='')
    #        #print()
    #     print()
    
    # Doc pour QTIMER & TIMEOUT
    # https://doc.qt.io/qtforpython-6.5/PySide6/QtCore/QTimer.html
    



def main():
    app = QApplication(sys.argv) # classe wrapper, écoute tout ce qui se passe dans l'OS et dispatch

    w = GOLApp()
    
    if (self.__controlWidget)

    w.show()

    sys.exit(app.exec()) # est une fonction bloquante

if __name__ == '__main__':
    main()     
