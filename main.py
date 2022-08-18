from funcoes import *
import time
from command_runner.elevate import elevate

rede = 'POCO X3 NFC'
adaptador = 'Ethernet 1000'

'''ping = os.system('ping -n 1 www.google.com')
print(ping)'''

os.system ('taskkill /im uTorrent.exe -t')
conectar_rede_salva(rede)
estado = ''
while estado != 'Conectado':
    estado = estado_conexao_wifi()
    time.sleep(3)
    print(estado)
elevate(desabilitar_adaptador(adaptador))
os.system(r'"C:\Onedrives\OneDrive - abc\Programas\PortableApps\uTorrentPortable\uTorrentPortable.exe"')
time.sleep(15)
elevate(habilitar_adaptador(adaptador))