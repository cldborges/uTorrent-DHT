import os
import subprocess
import re
from elevate import elevate
#from command_runner.elevate import elevate

elevate()

def escanear_redes_proximas():
    os.system('cmd /c "netsh wlan show networks"')

def conectar_rede_salva(rede):
    os.system(f'''cmd /c "netsh wlan connect name="{rede}""''')

def descobrir_adaptadores():
    os.system('cmd /c "netsh interface show interface"')

def habilitar_adaptador(adaptador):
  #  elevate()
    os.system(f'cmd /c "netsh interface set interface "{adaptador}" enable"')

def desabilitar_adaptador(adaptador):
 #   elevate()
    os.system(f'cmd /c "netsh interface set interface "{adaptador}" disable"')

def estado_conexao_wifi():
    output = str(subprocess.check_output('cmd /c "netsh wlan show interfaces"', shell=True))
    padraoRegex = r'Estado *: (.*?)\\r\\n'
    estado = re.findall(padraoRegex, output)
    return estado[0]

habilitar_adaptador('Ethernet 100')
print('fdfd')