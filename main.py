from funcoes import *
import time
from elevate import elevate
#import threading

rede = 'POCO X3 NFC'
#rede = 'Nina'

adaptador = 'Ethernet'

'''ping = os.system('ping -n 1 www.google.com')
print(ping)'''

elevate()
os.system ('taskkill /im uTorrent.exe -t -f')
conectar_rede_salva(rede)
estado = ''
contador = 0
while estado != 'Conectado' and contador < 20:
    estado = estado_conexao_wifi()
    time.sleep(3)
    print(estado)
    contador += 1

if contador >= 20:
    pass
else:
    desabilitar_adaptador(adaptador)
    #threading.Thread(target=abrir_programa).start()
    os.startfile(r'C:\Programas\PortableApps\uTorrentPortable\uTorrentPortable.exe')
    time.sleep(30)
    habilitar_adaptador(adaptador)
    desconectar_wifi()
