import sys
import dearpygui as dpi
import PySide6 as Side
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from dearpygui import *


#Run service
from SCZ import SCZ_client_beta

class  mainobject(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Project A  GUI - Alpha versions")
        self.setWindowIcon(QtGui.QIcon("web\\assets\\image\\favicon.png"))
        self.setGeometry(150, 150, 1500, 870)
        self.setStyleSheet("background-color: #505D7C")
       
        
    
        

def main_run():
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("/web/assets/image/favicon.png"))
    window = mainobject()
    window.show()
    sys.exit(app.exec())
   
    



