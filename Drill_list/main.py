import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QComboBox, QPushButton)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import QSize




def loadDrill ():
    str_open = "CLASS SPIRAL_DRILL"#"#"
    str_close = "END_DATA"
    
    ptr_open = 0
    ptr_close = 0

    data_str = []
    with open("tool_database.dat", "r", encoding='utf-8') as data_file:
       for line in data_file:  
            line = data_file.readline()
            
            
            
    for line in data_str :
        print(line)
    return data_str




class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.resize(QSize(100, 100))
        self.btn = QPushButton("TEST BUTTON", self)

        self.btn.clicked.connect(self.on_click)  # соединение сигнала и слота (сигнал clicked и слот on_click)

    def on_click(self):
        loadDrill()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())