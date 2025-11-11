import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import (QApplication
                                , QWidget 
                                , QLabel 
                                , QScrollBar
                                , QHBoxLayout
                                , QVBoxLayout
                                )

class ColorPicker(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)

        fixed_width = 35
        self.__red_sb = QScrollBar()
        self.__red_color = QLabel()
        self.__green_sb = QScrollBar()
        self.__green_color = QLabel()
        self.__blue_sb = QScrollBar()
        self.__blue_color = QLabel()
        self.__mixed_color = QLabel()

        self.__mixed_color.setFixedWidth(fixed_width)

        red_layout = self.__create_channel(self.__red_sb, self.__red_color, 'Red', fixed_width)
        green_layout = self.__create_channel(self.__green_sb, self.__green_color, 'Green', fixed_width)
        blue_layout = self.__create_channel(self.__blue_sb, self.__blue_color, 'Blue', fixed_width)

        channel_layout = QVBoxLayout()
        channel_layout.addLayout(red_layout)
        channel_layout.addLayout(green_layout)
        channel_layout.addLayout(blue_layout)

        layout = QHBoxLayout()
        layout.addLayout(channel_layout)
        layout.addWidget(self.__mixed_color)

        self.setLayout(layout)

    def __create_channel(self, sb, color, title_text, fixed_width):
        #Création des widgets requis
        title = QLabel()
        value = QLabel()

        #Configuration des widgets (mutateurs)
        title.setText(title_text)
        title.setFixedWidth(fixed_width)
        
        sb.setOrientation(Qt.Horizontal)
        sb.setRange(0,255)
        sb.setMinimumWidth(2 * fixed_width)

        value.setNum(0)
        value.setAlignment(Qt.AlignCenter)
        value.setFixedWidth(fixed_width)

        #Création du layout et assemblage
        layout = QHBoxLayout()
        layout.addWidget(title)
        layout.addWidget(sb)
        layout.addWidget(value)
        layout.addWidget(color)

        #Établissement des connections
        sb.valueChanged.connect(value.setNum) #pas besoin de listener, bind directement
        sb.valueChanged.connect(self.__update_colors) #il n'y a rien d'existant dans la doc pour cette fonction
        
        return layout

    def __update_color(self, color_widget, r, g, b):
        image = QPixmap(color_widget.size())
        image.fill(QColor(r, g, b))
        color_widget.setPixmap(image)

    def __update_colors(self):
        r = self.__red_sb.value()
        g = self.__green_sb.value()
        b = self.__blue_sb.value()
        self.__update_color(self.__red_color, r, 0, 0)
        self.__update_color(self.__green_color, 0, g, 0)
        self.__update_color(self.__blue_color, 0, 0, b)
        self.__update_color(self.__mixed_color, r, g, b)

    def showEvent(self, event):
        super().showEvent(event) #dans la doc, fonction neutre
        self.__update_colors()


def main():
    app = QApplication(sys.argv) # classe wrapper, écoute tout ce qui se passe dans l'OS et dispatch

    w = ColorPicker()
    w.show()

    sys.exit(app.exec()) # est une fonction bloquante

if __name__ == '__main__':
    main()

 # def __create_channel(self, sb, color, title_text, fixed_width):
        #     title = QLabel()
        #     value = QLabel()

        #utilisation des mutateurs 
        # fixed_width = 35
        # red_title.setFixedWidth(fixed_width)
        # red_title.setText('Red')
        # self.__red_sb.setOrientation(Qt.Horizontal)
        # self.__red_sb.setRange(0,255)
        # self.__red_sb.setValue(0)
        # self.__red_sb.setMinimumWidth(2 * fixed_width)

        # red_value.setNum(0)
        # red_value.setFixedWidth(fixed_width)
        # red_value.setAlignment(Qt.AlignCenter)

        # self.__red_color.setFixedWidth(fixed_width)

        # red_layout = QHBoxLayout()
        # red_layout.addWidget(red_title)
        # red_layout.addWidget(self.__red_sb)
        # red_layout.addWidget(red_value)
        # red_layout.addWidget(self.__red_color)

        # self.setLayout(red_layout)