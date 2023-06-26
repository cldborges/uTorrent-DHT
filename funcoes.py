import os
import subprocess
import re
# from elevate import elevate
#from command_runner.elevate import elevate

#elevate()

def escanear_redes_proximas():
    os.system('cmd /c "netsh wlan show networks"')

def conectar_rede_salva(rede):
    os.system(f'''cmd /c "netsh wlan connect name="{rede}""''')

def desconectar_wifi():
    os.system(f'''cmd /c "netsh wlan disconnect''')

def descobrir_adaptadores():
    os.system('cmd /c "netsh interface show interface"')

def habilitar_adaptador(adaptador):
  #  elevate()
    os.system(f'cmd /c "netsh interface set interface "{adaptador}" enable"')

def desabilitar_adaptador(adaptador):
    # elevate()
    os.system(f'cmd /c "netsh interface set interface "{adaptador}" disable"')

def estado_conexao_wifi():
    output = str(subprocess.check_output('cmd /c "netsh wlan show interfaces"', shell=True))
    padraoRegex = r'Estado *: (.*?)\\r\\n'
    estado = re.findall(padraoRegex, output)
    # print(estado[0])
    return estado[0]

def abrir_programa():
    os.system(r'"C:\Onedrives\OneDrive - abc\Programas\PortableApps\uTorrentPortable\uTorrentPortable.exe"')

# desconectar_wifi()
# print('fdfd')

# conectar_rede_salva('POCO X3 NFC')
# descobrir_adaptadores()
# desabilitar_adaptador('Ethernet')