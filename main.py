#!/usr/bin/python3
#Infoware
_version = "2.0"

#Imports
try:
    from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
    from PyQt5 import uic
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
        print("Is the file missing?")
        exit(0)

#About
def aboutProgram():
    about = QMessageBox()
    about.setWindowTitle('Created by OhRetro_')
    about.setText(f"Infoware v{_version}\nDo you want to open the program's repository on github?")
    about.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    openlink = about.exec_()

    if openlink == QMessageBox.Yes:
        webbrowser.open('https://github.com/OhRetro/Infoware')

#Infoware
class Infoware(QWidget):
    def __init__(self):
        super().__init__()
        gui = uic.loadUi('./main.ui', self)
        gui.Version_text.setText(f'v{_version}')
        
        _SYSTEM = GetInfo.System
        _CPU = GetInfo.CPU
        _GPU = GetInfo.GPU

        self.SetInfo.system(gui, 
                            _SYSTEM._manufacturer,
                            _SYSTEM._model,
                            _SYSTEM._os,
                            _SYSTEM._version,
                            _SYSTEM._architecture,
                            _SYSTEM._ram,
                            _SYSTEM._disk)
        self.SetInfo.cpu(gui,
                         _CPU._processor,
                         _CPU._cores,
                         _CPU._threads,
                         _CPU._bits,
                         _CPU._socket,
                         _CPU._minclock,
                         _CPU._maxclock)
        self.SetInfo.gpu(gui,
                         _GPU._graph_card,
                         _GPU._type,
                         _GPU._vram)

        #Display Message
        def display_message(title:str, message:str, standard_buttons=None):
            display = QMessageBox()
            display.setWindowTitle(title)
            display.setText(message)

            if standard_buttons is not None:
                display.setStandardButtons(standard_buttons)
                return display.exec_()
            else:   
                display.exec_()
                return

        #About
        def about():
            chosen_response = display_message("Created by OhRetro", 
                                              f"Infoware v{_version}\nDo you want to open the program's repository on github?", 
                                              QMessageBox.Yes | QMessageBox.No)

            if chosen_response == QMessageBox.Yes:
                webbrowser.open("https://github.com/OhRetro/Infoware")

        gui.About_button.clicked.connect(about)
        
        gui.show()

    #Set Info
    class SetInfo:
        #System
        def system(gui, manufacturer="", model="", os="", version="", architecture="", ram="", disk=""):
            gui.Manufacturer_display.setText(manufacturer)
            gui.Model_display.setText(model)
            gui.OS_display.setText(os)
            gui.OS_version_display.setText(version)
            gui.Arc_display.setText(architecture)
            gui.RAM_display.setText(ram)
            gui.Disk_display.setText(disk)

        #CPU
        def cpu(gui, processor="", cores="", threads="", bits="", socket="", minclocks="", maxclocks=""):
            gui.Processor_display.setText("")
            gui.Cores_display.setText("")
            gui.Threads_display.setText("")
            gui.Bits_display.setText("")
            gui.Socket_display.setText("")
            gui.MinClock_display.setText("")
            gui.MaxClock_display.setText("")

        #GPU
        def gpu(gui, graph_card="", type="", vram=""):
            gui.GraphicsCard_display.setText(graph_card)
            gui.Type_display.setText(type)
            gui.VRAM_display.setText(vram)

#Run
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Infoware()
    app.exec()