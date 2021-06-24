from prometheus_client import start_http_server, Gauge, CollectorRegistry
from psutil._common import bytes2human
import socket
import psutil
import time

def update_gauge():
    host_ip = socket.gethostbyname(socket.gethostname())

    tot = psutil.net_io_counters()
    gauge_transmit_bytes_total.labels(host_ip).set(tot.bytes_sent)
    gauge_recive_bytes_total.labels(host_ip).set(tot.bytes_recv)

    pnic = psutil.net_io_counters(pernic=True)
    nic_names = list(pnic.keys())
    for nic in nic_names:
        gauge_transmit_bytes.labels(nic,host_ip).set(pnic[nic].bytes_sent)
        gauge_recive_bytes.labels(nic,host_ip).set(pnic[nic].bytes_recv)
        gauge_transmit_packets.labels(nic,host_ip).set(pnic[nic].packets_sent)
        gauge_recive_packets.labels(nic,host_ip).set(pnic[nic].packets_recv)

registry = CollectorRegistry()

gauge_transmit_bytes_total = Gauge('network_transmit_bytes_total', 'Total transmit data in bytes', ['instance'])
gauge_recive_bytes_total = Gauge('network_recive_bytes_total', 'Total recive data in bytes', ['instance'])

gauge_transmit_bytes = Gauge('network_transmit_bytes', 'Transmit data in bytes by device', ['device', 'instance'])
gauge_recive_bytes = Gauge('network_recive_bytes', 'Recive data in bytes by device', ['device', 'instance'])
gauge_transmit_packets = Gauge('network_transmit_packets', 'Transmit data in packets by device', ['device', 'instance'])
gauge_recive_packets = Gauge('network_recive_packets', 'Recive data in packets by device', ['device', 'instance'])

start_http_server(8000)

try:
    while True:
        update_gauge()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stoping Prometheus Custom metric server")
