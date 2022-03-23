import eel
import sys
import dearpygui as dpi
from dearpygui import *

#Run server
from SCZ import SCZ_client_beta


#eel Run app
def main():
    eel.init("web")
    eel.start("message.htm", size=(800, 800))
    
    
if __name__ == "__main__":
    main()

