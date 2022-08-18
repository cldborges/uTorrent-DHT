import os
from elevate import elevate
import time

elevate()
os.system('cmd /c "netsh interface set interface "Ethernet 100" disable"')
time.sleep(5)
os.system('cmd /c "netsh interface set interface "Ethernet 100" enable"')