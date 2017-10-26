#!/usr/bin/env python3
# -*- coding; utf-8 -*-
from time import sleep
import os

class CacheSquid:
    def limparCache(self):
        #Para o squid3
        os.system("/etc/init.d/squid3 stop")
        
		#Suspende a execução por 15 segundos
        sleep(15)
        
		#Renomeie o diretório do Squid
        os.system("mv /var/spool/squid3 /var/spool/squid3.del")
        
		#Recrie o diretório de cache:
        os.system("mkdir /var/spool/squid3")
        
		#Dê permissão para o diretório criado: 
        os.system("chmod 777 /var/spool/squid3")
        
		#Reconstrua os arquivos de cache: 
        os.system("/var/spool/squid3 -z")
        
		#Suspende a execução por 50 minutos
        sleep(3000)
        
		#Inicie o servidor do Squid (nesse passo, a sua Internet já volta a funcionar): 
        os.system("/etc/init.d/squid3 start")
        
		#Apague o diretório de cache antigo, sem impactos para os usuários: 
        os.system("rm -rf /var/spool/squid3.del")

def main():
    cs = CacheSquid()
    cs.limparCache()

if __name__ == '__main__':
    main()
    




