#!/usr/bin/python3
#Infoware
_version = "2.0"

#Imports
try:
    from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
    from PyQt5 import uic
    from oreto_utils import PyQt
    import webbrowser

except ImportError as missing_package:
    missing_package = str(missing_package).replace("No module named ", "")
    print(f"{missing_package} is missing.\nPlease install {missing_package}.\n")
    exit(0)

finally:
    import sys

    try:
        from get import GetInfo

    except ImportError:
        print("Is 'get.py' missing?")
        exit(0)

#Infoware
class Infoware(QWidget):
    def __init__(self):
        super().__init__()
        gui = uic.loadUi("./main.ui", self)
        gui.Version_text.setText(f"v{_version}")

        _SYSTEM = GetInfo.System
        _CPU = GetInfo.CPU
        _GPU = GetInfo.GPU

        PyQt.set_text(
            gui,
            
            #System
            Manufacturer_display=_SYSTEM._manufacturer,
            Model_display=_SYSTEM._model,
            OS_display=_SYSTEM._os,
            OS_version_display=_SYSTEM._version,
            Arc_display=_SYSTEM._architecture,
            RAM_display=_SYSTEM._ram,
            Disk_display=_SYSTEM._disk,
            
            #CPU
            Processor_display=_CPU._model,
            Cores_display=_CPU._cores,
            Threads_display=_CPU._threads,
            Bits_display=_CPU._bits,
            Socket_display=_CPU._socket,
            MinClock_display=_CPU._minclock,
            MaxClock_display=_CPU._maxclock,
            
            #GPU
            GraphicsCard_display=_GPU._model,
            Type_display=_GPU._type,
            VRAM_display=_GPU._vram,
        )

        gui.About_button.clicked.connect(self.about)

        gui.show()

    #About
    def about(self):
        chosen_response = PyQt.display_message(
            "Created by OhRetro",
            f"Infoware v{_version}\nDo you want to open the program's repository on github?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if chosen_response == QMessageBox.Yes:
            webbrowser.open("https://github.com/OhRetro/Infoware")


#Run
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = Infoware()
        app.exec()
    except Exception as e:
        PyQt.display_message("a error ocorred", str(e))
