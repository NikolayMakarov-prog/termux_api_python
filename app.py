import termux_api.comands
from time import sleep
for i in range(1):
    sleep(0)
    termux_api.comands.termux_battery_status()