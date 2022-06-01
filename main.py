# import module
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'
 
# scan available Wifi networks
#os.system('cmd /c "netsh wlan show networks"')
 
# input Wifi name
#name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')

name_of_router = 'NET_CLDBORGES2'
 
# connect to the given wifi network
os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
 
print("If you're not yet connected, try connecting to a previously connected SSID again!")



if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    os.system('cmd /c "netsh interface set interface "Ethernet" disable"')
    sys.exit(0)