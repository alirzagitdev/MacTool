import psutil

def get_system_mac():
    result = {}
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                result[iface] = addr.address
    return result
        



