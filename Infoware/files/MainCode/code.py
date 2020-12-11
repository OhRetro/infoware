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

#System Informations------------------------------------------------------------
info = wmi.WMI()
PCinfo = info.Win32_ComputerSystem()[0]
PC = platform.uname()
PC_model = PCinfo.Model
PC_manufacturer = PCinfo.Manufacturer
PC_os = f'{PC.system} {PC.release}'
PC_os_ver = f'{PC.version}'
PC_arc = f'{PC.machine}'
RAM = psutil.virtual_memory()

#Disk
DISK = psutil.disk_partitions()
for DISK in DISK:
    try:
        DISK_total = psutil.disk_usage(DISK.mountpoint)
    except PermissionError:
        continue


#CPU Informations---------------------------------------------------------------
class CPUin:
    #Socket
    def socket():
        get_cpusocket = 'wmic cpu get SocketDesignation'
        str_cpusocket = os.popen(get_cpusocket).read().replace('SocketDesignation', '').split('\n\n')[1].replace('               ', '')
        return str_cpusocket

    #Usage:
    def usage():
        while True:
            str_usage = psutil.cpu_percent(interval=2)
            return str_usage

#Infos
CPU = cpuinfo.get_cpu_info()
CPU_model = CPU['brand_raw'].replace('(TM)', '™').replace('(R)', '®')
CPU_cores = psutil.cpu_count(logical=False)
CPU_threads = CPU['count']
CPU_bits = CPU['bits']
CPU_socket = CPUin.socket()
CPU_usage = CPUin.usage()

#Clock
CPU_maximumclock = CPU['hz_actual_friendly']
CPU_baseclock = CPU['hz_advertised_friendly']


#GPU Informations---------------------------------------------------------------
class GPU:
    #Model
    def model():
        dxdiag = 'dxdiag /t files/dxdiag.txt'
        os.popen(dxdiag)
        with open('files/dxdiag.txt') as f:
            for line in f:
                if "Card name:" in line:
                    return str(line).replace('Card name:', '').replace('\n', '').replace('            ', '')

    #Type
    def type():
        dxdiag = 'dxdiag /t files/dxdiag.txt'
        os.popen(dxdiag)

        with open('files/dxdiag.txt') as f:
            for line in f:
                if "Hybrid Graphics GPU:" in line:
                    return str(line).replace('Hybrid Graphics GPU:', '').replace('\n', '').replace(' ', '')

    #VRAM
    def VRAM():
        dxdiag = 'dxdiag /t files/dxdiag.txt'
        os.popen(dxdiag)

        with open('files/dxdiag.txt') as f:
            for line in f:
                if 'Dedicated Memory:' in line:
                    return str(line).replace('Dedicated Memory:', '').replace('\n', '').replace(' ', '')

GPU_model = GPU.model().replace('(TM)', '™').replace('(R)', '®')
GPU_type = GPU.type()
GPU_VRAM = GPU.VRAM()

#SizeByte-----------------------------------------------------------------------
def sizeByte(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor

#SizeHertz----------------------------------------------------------------------
#def sizeHertz(hertz, suffix='Hz'):
    #factor = 1000
    #for unit in ['', 'K', 'M', 'G']:
        #if hertz < factor:
            #return f'{hertz:.2f}{unit}{suffix}'
        #hertz /= factor
