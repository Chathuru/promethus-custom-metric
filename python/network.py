import psutil
from psutil._common import bytes2human

tot = psutil.net_io_counters()
pnic = psutil.net_io_counters(pernic=True)

nic_names = list(pnic.keys())
for nic in nic_names:
    print(nic, '\tSent ', bytes2human(pnic[nic].bytes_sent), '\tRecv', bytes2human(pnic[nic].bytes_recv))
