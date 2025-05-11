from machine import Pin
from config import name_network, pass_network
import time, network


def report(timeout:int):
    PIN = Pin(8, Pin.OUT)
    number = 0 
    while number < 10:
        number+=1
        PIN.value(1)
        time.sleep(timeout)
        PIN.value(0)
        time.sleep(timeout)

def log(update:str):
    with open('log.txt', 'a+') as file:
        file.write(f'{update}\n')

def connect_wifi():
    try:
        inet_wifi = network.WLAN(network.STA_IF)
        inet_wifi.active(True)
        time.sleep(2)
        log(update=inet_wifi.scan())
        inet_wifi.active(True)
        inet_wifi.connect(name_network, pass_network)
        if inet_wifi.isconnected():
            report(timeout=1)
            log(update="Connect")
        else:
            report(timeout=0.1)
            log(update="Not connect")
        
    except Exception as err:
        log(update=err)

connect_wifi()

