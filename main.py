#Infoware
VERSION = 2.0

#Imports
from sys import argv as sys_argv
from traceback import format_exc as tb_format_exc
from webbrowser import open as wb_open

from pc import SYSTEM, CPU, GPU, debug

if SYSTEM["OS"] != "Windows":
    print("Infoware only works for now on Windows.")
    exit(2)

try:
    from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QStackedWidget, QTabBar
    from PyQt5 import uic
    from pyqt5_utils import Icon as oup_Icon, Button as oup_Button
    from pyqt5_utils import displaymessage as oup_displaymessage, settext as oup_settext, bindbutton as oup_bindbutton

except ImportError:
    print(tb_format_exc())
    print("\n[!] Please try running \"pip install -r requirements.txt\"")
    exit(1)

#Infoware
class Infoware(QWidget):
    def __init__(self):
        super().__init__()
        gui = uic.loadUi("./main.ui", self)
        gui.Version_TEXT.setText(f"v{VERSION}")

        #debug()
            
        oup_settext(
            gui,
            #System
            SysManufacturer_DISPLAY=SYSTEM["MANUFACTURER"],
            SysModel_DISPLAY=SYSTEM["MODEL"],
            SysOSName_DISPLAY=SYSTEM["OS"],
            SysOSVersion_DISPLAY=SYSTEM["VERSION"],
            SysArch_DISPLAY=SYSTEM["MACHINE"],
            SysRAM_DISPLAY=SYSTEM["RAM"]["TOTAL"],
            SysDisk_DISPLAY=SYSTEM["DISK"]["TOTAL"],
            #CPU
            CPUModel_DISPLAY=CPU["MODEL"],
            CPUCores_DISPLAY=CPU["CORES"],
            CPUThreads_DISPLAY=CPU["THREADS"],
            CPUArch_DISPLAY=CPU["ARCH"],
            CPUSocket_DISPLAY=CPU["SOCKET"],
            CPUMinClock_DISPLAY=CPU["FREQ"]["MIN"],
            CPUMaxClock_DISPLAY=CPU["FREQ"]["MAX"],
            #GPU
            GPUModel_DISPLAY=GPU["MODEL"],
            GPUType_DISPLAY=GPU["TYPE"],
            GPUVRAM_DISPLAY=GPU["VRAM"]
        )
 
        oup_bindbutton(gui, "About_BUTTON", self.about)
        gui.show()

    #About
    def about(self):
        response = oup_displaymessage(
            title="About Infoware",
            message=f"Infoware v{VERSION}; Created by OhRetro", 
            informative="Do you want to open the program's repository on github?",
            icon=oup_Icon["Information"],
            buttons=(oup_Button["Yes"] | oup_Button["No"]),
            windowicon="./icon.png"
        )

        if response == oup_Button["Yes"]:
            wb_open("https://github.com/OhRetro/Infoware")

#Run
if __name__ == "__main__":
    app = QApplication(sys_argv)
    window = Infoware()
    app.exec()