from funcoes import *
import time
from elevate import elevate
#import threading

rede = 'POCO X3 NFC'
adaptador = 'Ethernet 1000'

'''ping = os.system('ping -n 1 www.google.com')
print(ping)'''

elevate()
os.system ('taskkill /im uTorrent.exe -t')
conectar_rede_salva(rede)
estado = ''
contador = 0
while estado != 'Conectado' and contador < 20:
    estado = estado_conexao_wifi()
    time.sleep(3)
    print(estado)
    contador += 1

if contador >= 10:
    pass
else:
    desabilitar_adaptador(adaptador)
    #threading.Thread(target=abrir_programa).start()
    os.startfile(r'C:\Onedrives\OneDrive - abc\Programas\PortableApps\uTorrentPortable\uTorrentPortable.exe')
    time.sleep(60)
    habilitar_adaptador(adaptador)
    desconectar_wifi()