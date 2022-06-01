import os
from elevate import elevate

elevate()
os.system('cmd /c "netsh interface set interface "Ethernet" enable"')