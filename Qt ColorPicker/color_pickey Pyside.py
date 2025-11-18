import sys
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import (QApplication
                                , QWidget 
                                , QLabel 
                                , QScrollBar
                                , QHBoxLayout
                                , QVBoxLayout
                                )

class ColorPicker(QWidget):
    
    colorChanged = Signal(QColor) #Événement 
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        fixed_width = 35
        self.red_sb = QScrollBar()
        self.red_color = QLabel()
        self.green_sb = QScrollBar()
        self.green_color = QLabel()
        self.blue_sb = QScrollBar()
        self.blue_color = QScrollBar()
        self.mixed_color = QLabel()
        
        self.mixed_color.setFixedWidth(fixed_width)
        
        red_layout = self.create_channel(self.red_sb, self.red_color, 'Red', fixed_width)
        green_layout = self.create_channel(self.green_sb, self.green_color, 'Green', fixed_width)
        blue_layout = self.create_channel(self.blue_sb, self.blue_color, 'Blue', fixed_width)
        
        channel_layout = QVBoxLayout()
        channel_layout.addLayout(red_layout)
        channel_layout.addLayout(green_layout)
        channel_layout.addLayout(blue_layout)
        
        mainlayout = QHBoxLayout()
        mainlayout.addLayout(channel_layout)
        mainlayout.addWidget(self.mixed_color)
        
        self.setLayout(mainlayout)
        
    def create_channel(self, sb, color, title, fixed_width):
        
        #Création des widgets requis
        title = QLabel()
        value = QLabel()
        
        #Configuration des widgets (mutateurs)
        title.setText(title)
        title.setFixedWidth(fixed_width)
        
        sb.setOrientation(Qt.Horizontal)
        sb.setRange(0,255)
        sb.setValue(0)
        sb.setMinimumWidth(2*fixed_width)
        
        value.setNum(0)
        value.setAlignment(Qt.AlignCenter)
        value.setFixedWidth(fixed_width)
        
        color.setFixedWidth(fixed_width)
        
        #Création du layout d'assemblage
        layout = QHBoxLayout()
        layout.addWidget(title)
        layout.addWidget(sb)
        layout.addWidget(value)
        layout.addWidget(color)
        
        #Établissement des connections
        sb.valueChanged.connect(value.setNum)
        sb.valueChanged.connect(self.update_colors)
        
        return layout
        
    def update_color(self, color_widget, r, g, b):
        image = QPixmap(color_widget.size())
        image.fill(QColor(r, g, b))
        color_widget.setPixmap(image)
    
    @Slot() #appelé en réponse à l'événement
    def update_colors(self):
        r = self.red_sb.value()
        g = self.green_sb.value()
        b = self.blue_sb.value()
        self.update_color(self.red_color, r, 0, 0)
        self.update_color(self.green_color, 0, g, 0)
        self.update_color(self.blue_color, 0, 0, b)
    
    @override
    def showEvent(self, event):
        super().showEvent(event)
        self.update_colors()
        
        
def main():
    app = QApplication(sys.argv)
    
    w = ColorPicker()
    w.show()
    
    sys.exit(app.exec())
        
if __name__ == '__main__':
    main()   