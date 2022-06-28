#Infoware
VERSION = ["2.0", "Dev", 200]

#Imports
from sys import argv as sys_argv

try:
    from PyQt5.QtWidgets import QWidget, QApplication
    from PyQt5 import uic
    from oreto_utils.pyqt5_utils import Icon as oup_Icon, Button as oup_Button, displaymessage as oup_displaymessage, settext as oup_settext, bindbutton as oup_bindbutton
    from webbrowser import open as wb_open

except ImportError as e:
    raise ImportError(f"{e}") from e

from pc import SYSTEM, CPU, GPU, debug

#Infoware
class Infoware(QWidget):
    def __init__(self):
        super().__init__()
        gui = uic.loadUi("./main.ui", self)
        gui.Version_TEXT.setText(f"v{VERSION[0]}")

        debug() #TODO: REMOVE THIS LINE WHEN FINISHED
        
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
            CPUMinClock_DISPLAY=CPU["CLOCK"]["MIN"],
            CPUMaxClock_DISPLAY=CPU["CLOCK"]["MAX"],
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
            message=f"Infoware v{VERSION[0]} | {VERSION[1]} | Version Code: {VERSION[2]}; Created by OhRetro", 
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