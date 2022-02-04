import platform
import subprocess

class GetInfo:
    class System:
        _manufacturer=""
        _model=""
        _os=platform.system()
        _version=platform.release()
        _architecture=platform.machine()
        _ram=""
        _disk=""
        
    class CPU:
        _processor=""
        _cores=""
        _threads=""
        _bits=""
        _socket=""
        _minclock=""
        _maxclock=""
        
    class GPU:
        _graph_card=""
        _type=""
        _vram=""
        