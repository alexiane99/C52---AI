import sys
from GOLEngine_v2 import GOLEngine 
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPixmap, QColor, QPainter, QBrush, QPen
from PySide6.QtWidgets import (QApplication
                                , QWidget 
                                , QLabel 
                                , QScrollBar
                                , QHBoxLayout
                                , QVBoxLayout
                                , QTextEdit
                                
                                )

class GOLApp(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        fixed_width = 800 
        fixed_height = 500

        self.__gol_view = QLabel()
        self.__gol_app = QHBoxLayout() #pour contenir la vue
        self.__gol_control = QLabel() #widget contrôle
        self.__gol_info = QLabel() #widget infos
        self.__texte = QTextEdit()

        #self.gol_engine = GOLEngine(900, 600)


        view = self.__create_layout(self.__gol_view, 900, 600, 'Vue', 0) #crée le widget selon tous ses parametres
        control = self.__create_layout(self.__gol_control, 250, 150, 'Contrôle', 2)
        info = self.__create_layout(self.__gol_info, 250, 150, 'Info', 1) 

        #applique la couleur aux widgets (c'est le widget qui est passé en paramètre et non son layout)
        self.__update_view(self.__gol_view, 0, 0, 0) #noir
       
        #self.__update_viewGame(self.__gol_view, 900, 600)
        self.__update_view(self.__gol_control, 135, 206, 250) #bleu
        self.__update_view(self.__gol_info, 255, 165, 0) #orange

        self.__gol_app.addLayout(control)
        self.__gol_app.addLayout(view) #ajoute les layout créées au main
        self.__gol_app.addLayout(info)

        self.setLayout(self.__gol_app) #création du main layout avec tous ses components

        self.paintView(self.__gol_view)

    def __create_layout(self, element, width, height, texte, indice): #permet la création du layout en fonction du widget 

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

    
    def paintView(self, widget): #crée une case dans le View 
        image = QPixmap(widget.size())
        image.fill(QColor(0, 0, 0))

        painter = QPainter(image)
        painter.begin(self) #activer le painter
        # brush = QBrush()
        # brush.setColor(255,255,255)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))

        pt1 = QPoint(0,0)
        pt2 = QPoint(20,20)
        case = QRect(pt1,pt2)
        painter.fillRect(case, painter.brush())

        print("ici")

        painter.end()
        widget.setPixmap(image) 



def main():
    app = QApplication(sys.argv) # classe wrapper, écoute tout ce qui se passe dans l'OS et dispatch

    w = GOLApp()

    w.show()

    sys.exit(app.exec()) # est une fonction bloquante

if __name__ == '__main__':
    main()     
