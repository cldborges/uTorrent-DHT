import os
from elevate import elevate

def escanear_redes_proximas():
    os.system('cmd /c "netsh wlan show networks"')

def conectar_rede_salva(rede):
    os.system(f'''cmd /c "netsh wlan connect name="{rede}""''')

def descobrir_adaptadores():
    os.system('cmd /c "netsh interface show interface"')

def habilitar_adaptador(adaptador):
    elevate()
    os.system('cmd /c "netsh interface set interface "Ethernet" enable"')

def desabilitar_adaptador(adaptador):
    elevate()
    os.system('cmd /c "netsh interface set interface "Ethernet" disable"')