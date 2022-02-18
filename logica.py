#Crear un algoritmo en Python que simule el orden de infección de un patógeno zombie extendido en el aula 307 del cole. 
# La zombificación se producirá por el mordisco de un zombie hacia una persona no infectada.

#Se puede añadir cualquier variación al algoritmo, 
# como por ejemplo permitir que las personas mueran por diversas razones 
# (mediante sacrificios, resbalar y morir, morir de aburrimiento, morir programando…)
import tweepy
import config
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth, 
                 wait_on_rate_limit=True)
from os import system, name
from random import random, randrange, uniform
import time
import schedule
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
print("Inicio de patógeno zombie extendido en el aula 307 del cole")
#supervivientes=["Gerard","Alfredo","Dani Ruano","Marc","Laura","Raul","Diego","Juan Carlos","Arnau","David Ortega","Pol","David","Miguel","Xavi"]
supervivientes=["Gerard","Alfredo","Dani Ruano","Marc"]
muertes=[" sacrificado"," por un resbalón"," de aburrimiento", " programando"]
dia=0
def accion_dia():
    global supervivientes
    global dia
    if(len(supervivientes)==0):
        api.update_status("Se acabó la humanidad")
        print("Se acabó")
        return schedule.CancelJob
    
    #Sumamos un dia
    dia=dia+1

    #Superviviente afectado
    superviviente_afectado=randrange(0,len(supervivientes))

    #Tipo de muerte
    tipo_muerte=randrange(0,len(muertes))
    #print("")
    #print("Dia número: "+ str(dia))
    #Imprimimos la muerte
    #print("El superviviente "+ supervivientes[superviviente_afectado]+ " ha muerto"+ muertes[tipo_muerte])
    #Mostramos cuantos quedan  
    #print("Quedan "+ str((len(supervivientes))-1) +" supervivientes")
    
    informe="Dia número: "+ str(dia) + ". El superviviente "+ supervivientes[superviviente_afectado]+ " ha muerto"+ muertes[tipo_muerte]+". Quedan "+ str((len(supervivientes))-1) +" supervivientes"
    
    supervivientes.pop(superviviente_afectado)
    
    #api.update_status(status=informe)
    #print("tweet enviado")
    print(informe)

    
schedule.every(2).seconds.do(accion_dia)


#Eliminamos al superviviente del array

while True:

    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    if not schedule.jobs:
        break
