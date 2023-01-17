from platform import system as pf_system, release as pf_release, machine as pf_machine, version as pf_version, architecture as pf_architecture
from shutil import disk_usage as sh_disk_usage
from psutil import virtual_memory as ps_virtual_memory, cpu_count as ps_cpu_count, cpu_freq as ps_cpu_freq
from contextlib import suppress as cl_suppress
from multiprocessing import Process as mp_Process

BYTE_UNITS:list[str] = ["Bytes", "KB", "MB", "GB", "TB", "PB"]

def format_byte_size(byte_size:int) -> str:
    """The size in byte will be formated in KB, MB, GB, TB or PB."""
    global BYTE_UNITS
    
    for i in range(5):
        if byte_size < 1024**(i+1):
            selected_unit = i
            break

    if byte_size >= 1024:
        formated_size = round(byte_size/1024**selected_unit, 2)
    else:
        formated_size = round(byte_size)

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
    return f"{formated_size} {units[selected_unit]}"

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
        "TOTAL": format_byte_size(VIRTUAL_MEMORY.total),
        "AVAILABLE": format_byte_size(VIRTUAL_MEMORY.available),
        "PERCENT": f"{VIRTUAL_MEMORY.percent}%",
        "USED": format_byte_size(VIRTUAL_MEMORY.used),
        "FREE": format_byte_size(VIRTUAL_MEMORY.free),
        },
    "DISK": {
        "TOTAL": format_byte_size(DISK_USAGE.total),
        "USED": format_byte_size(DISK_USAGE.used),
        "FREE": format_byte_size(DISK_USAGE.free),
        },
}
CPU = {
    "MANUFACTURER": None,
    "MODEL": None,
    "CORES": ps_cpu_count(False), #PHYSICAL
    "THREADS": ps_cpu_count(True), #LOGICAL
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