#Infoware
#Versão:1.2

import psutil
import shutil
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime
import platform, subprocess, distutils, math, random, sys
import cpuinfo
import GPUtil
import ctypes
import wmi
import json, os, time, re
from datetime import datetime

#Codes--------------------------------------------------------------------------
from files.MainCode.code import *

#Infoware-----------------------------------------------------------------------
class Infoware(QWidget):
    def __init__(self):
        super().__init__()
        gui = uic.loadUi('files/UI/main.ui', self)

        #OS Logo----------------------------------------------------------------
        #Win10
        if PC.system + PC.release == 'Windows10':
            pixmap = QPixmap('files/UI/Logos/OS/Windows10.png')
            gui.OS_Logo.setPixmap(pixmap)
            gui.OS_Logo.setScaledContents(True)

        #Win8.1
        if PC.system + PC.release == 'Windows8.1':
            pixmap = QPixmap('files/UI/Logos/OS/Windows8.1.png')
            gui.OS_Logo.setPixmap(pixmap)
            gui.OS_Logo.setScaledContents(True)

        #Win8
        if PC.system + PC.release == 'Windows8':
            pixmap = QPixmap('files/UI/Logos/OS/Windows8.png')
            gui.OS_Logo.setPixmap(pixmap)
            gui.OS_Logo.setScaledContents(True)

        #Win7
        if PC.system + PC.release == 'Windows7':
            pixmap = QPixmap('files/UI/Logos/OS/Windows7.png')
            gui.OS_Logo.setPixmap(pixmap)
            gui.OS_Logo.setScaledContents(True)

        #Linux
        if PC.system == 'Linux':
            pixmap = QPixmap('files/UI/Logos/OS/Linux.png')
            gui.OS_Logo.setPixmap(pixmap)
            gui.OS_Logo.setScaledContents(True)

        #Companys Logo----------------------------------------------------------
        #SAMSUNG
        if 'SAMSUNG' in PC_manufacturer:
            pixmap = QPixmap('files/UI/Logos/Companys/SAMSUNG.png')
            gui.Company_Logo.setPixmap(pixmap)
            gui.Company_Logo.setScaledContents(True)

        #Dell
        if 'Dell' in PC_manufacturer:
            pixmap = QPixmap('files/UI/Logos/Companys/Dell.png')
            gui.Company_Logo.setPixmap(pixmap)
            gui.Company_Logo.setScaledContents(True)

        #Lenovo
        if 'Lenovo' in PC_manufacturer:
            pixmap = QPixmap('files/UI/Logos/Companys/Lenovo.png')
            gui.Company_Logo.setPixmap(pixmap)
            gui.Company_Logo.setScaledContents(True)

        #ASUS
        if 'ASUS' in PC_manufacturer:
            pixmap = QPixmap('files/UI/Logos/Companys/ASUS.png')
            gui.Company_Logo.setPixmap(pixmap)
            gui.Company_Logo.setScaledContents(True)

        #Multilaser
        if 'Multilaser' in PC_manufacturer:
            pixmap = QPixmap('files/UI/Logos/Companys/Multilaser.png')
            gui.Company_Logo.setPixmap(pixmap)
            gui.Company_Logo.setScaledContents(True)

        #Positivo
        if 'Positivo' in PC_manufacturer:
            pixmap = QPixmap('files/UI/Logos/Companys/Positivo.png')
            gui.Company_Logo.setPixmap(pixmap)
            gui.Company_Logo.setScaledContents(True)

        #CPU Logo---------------------------------------------------------------
        #Intel
        if 'Intel' in CPU_model:
            pixmap = QPixmap('files/UI/Logos/CPU/intel.png')
            gui.CPULogo.setPixmap(pixmap)
            gui.CPULogo.setScaledContents(True)

        #AMD
        if 'AMD' in CPU_model:
            pixmap = QPixmap('files/UI/Logos/CPU/AMD.png')
            gui.CPULogo.setPixmap(pixmap)
            gui.CPULogo.setScaledContents(True)

        #System-----------------------------------------------------------------
        gui.Manufacturer_display.setText(PC_manufacturer)
        gui.Model_display.setText(PC_model)
        gui.OS_display.setText(PC_os)
        gui.Version_display.setText(PC_os_ver)
        gui.Arc_display.setText(PC_arc)
        gui.RAM_display.setText(f'{sizeByte(RAM.total)}')
        gui.Disk_display.setText(f'{sizeByte(DISK_total.total)}')

        #CPU--------------------------------------------------------------------
        #Infos
        gui.Processor_display.setText(CPU_model)
        gui.Cores_display.setText(str(CPU_cores))
        gui.Threads_display.setText(str(CPU_threads))
        gui.Bits_display.setText('x' + str(CPU_bits))
        gui.Socket_display.setText(CPU_socket)
        #gui.Usage_display.setText(str(CPU_usage) + '%')

        #Clock
        gui.BaseClock_display.setText(CPU_baseclock)
        gui.MaximumClock_display.setText(CPU_maximumclock)

        #GPU--------------------------------------------------------------------
        gui.GraphicsCard_display.setText(GPU_model)
        gui.Type_display.setText(GPU_type)
        gui.VRAM_display.setText(GPU_VRAM)

        gui.show()

#Run----------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Infoware()
    app.exec()
