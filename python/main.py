from prometheus_client import start_http_server, Gauge
import time
import psutil

if __name__ == '__main__':

   gauge = Gauge('system_process_count', 'System Process Count')
   start_http_server(8000)

   try:
      while True:
         gauge.set(len(psutil.pids()))
         time.sleep(1)
   except KeyboardInterrupt:
      print("Stoping Prometheus Custom metric server")
