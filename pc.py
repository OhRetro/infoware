from platform import system as pf_system, release as pf_release, machine as pf_machine, version as pf_version, architecture as pf_architecture
from oreto_utils.others_utils import formatsize as ouo_formatsize
from shutil import disk_usage as sh_disk_usage
from psutil import virtual_memory as ps_virtual_memory

VIRTUAL_MEMORY = ps_virtual_memory()
DISK_USAGE = sh_disk_usage("C:/")
PF_ARCHITECTURE = pf_architecture()

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
        "AVAILABLE": ouo_formatsize(VIRTUAL_MEMORY.available), # TODO: find a way of auto updating this
        "PERCENT": f"{VIRTUAL_MEMORY.percent}%", # TODO: find a way of auto updating this
        "USED": ouo_formatsize(VIRTUAL_MEMORY.used), # TODO: find a way of auto updating this
        "FREE": ouo_formatsize(VIRTUAL_MEMORY.free), # TODO: find a way of auto updating this
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
    "CORES": None,
    "THREADS": None,
    "ARCH": None,
    "SOCKET": None,
    "CLOCK": {
        "MIN": None,
        "MAX": None
        },
    "USAGE": None, # TODO: find a way of auto updating this
}
GPU = {
    "MANUFACTURER": None,
    "MODEL": None,
    "TYPE": None,
    "VRAM": None,
}

def debug():
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