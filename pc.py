from platform import system as pf_system, release as pf_release, machine as pf_machine, version as pf_version, architecture as pf_architecture
from oreto_utils.others_utils import formatsize as ouo_formatsize
from oreto_utils.terminal_utils import clear as out_clear
from shutil import disk_usage as sh_disk_usage
from psutil import virtual_memory as ps_virtual_memory, cpu_count as ps_cpu_count, cpu_freq as ps_cpu_freq
from contextlib import suppress as cl_suppress
from multiprocessing import Process as mp_Process

VIRTUAL_MEMORY = ps_virtual_memory()
DISK_USAGE = sh_disk_usage("C:/")
PF_ARCHITECTURE = pf_architecture()
CPU_FREQUENCY = ps_cpu_freq()

SYSTEM = {
    "MANUFACTURER": None,
    "MODEL": None,
    "OS": pf_system(),
    "REALEASE": pf_release(),
    "VERSION": pf_version(),
    "ARCH": {
        "BITS": PF_ARCHITECTURE[0],
        "LINKAGE": PF_ARCHITECTURE[1],
        },
    "MACHINE": pf_machine(),
    "RAM": {
        "TOTAL": ouo_formatsize(VIRTUAL_MEMORY.total),
        "AVAILABLE": ouo_formatsize(VIRTUAL_MEMORY.available),
        "PERCENT": f"{VIRTUAL_MEMORY.percent}%",
        "USED": ouo_formatsize(VIRTUAL_MEMORY.used),
        "FREE": ouo_formatsize(VIRTUAL_MEMORY.free),
        },
    "DISK": {
        "TOTAL": ouo_formatsize(DISK_USAGE.total),
        "USED": ouo_formatsize(DISK_USAGE.used),
        "FREE": ouo_formatsize(DISK_USAGE.free),
        },
}
CPU = {
    "MANUFACTURER": None,
    "MODEL": None,
    "CORES": {
        "PHYSICAL": ps_cpu_count(False),
        "LOGICAL": ps_cpu_count(True),
        },
    "THREADS": None,
    "ARCH": None,
    "SOCKET": None,
    "FREQ": {
        "MIN": None,
        "MAX": None,
        "CURRENT": None,
        },
    "USAGE": None,
}
GPU = {
    "MANUFACTURER": None,
    "MODEL": None,
    "TYPE": None,
    "VRAM": None,
}
        
def debug():
    with cl_suppress(Exception):
        from rich import print
      
    print("="*50)
    print("[DEBUG]", "System:")
    for SYSTEM_item in SYSTEM:
        print(f"{SYSTEM_item}: {SYSTEM[SYSTEM_item]}")
    print("\n[DEBUG]", "CPU:")
    for CPU_item in CPU:
        print(f"{CPU_item}: {CPU[CPU_item]}")
    print("\n[DEBUG]", "GPU:")
    for GPU_item in GPU:
        print(f"{GPU_item}: {GPU[GPU_item]}")
    print("="*50)
    
if __name__ == "__main__":
    debug()