from machine import Pin
from config import name_network, pass_network
from lib.current_time import current_time
import time, network

def report(pause:int, ping:int):
    pin = Pin(2, Pin.OUT)
    count = 0
    while count < ping:
        count+=1
        pin.value(1)
        time.sleep(pause)
        pin.value(0)
        time.sleep(pause)

def log(update:str):
    with open('log.txt', 'a+') as file:
        file.write(f'[{current_time()}] {update}\n')

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    
    networks = wifi.scan()
    status_search = False
    update_name = ""
    for net in networks:
        if name_network in net[0].decode():
            update_name = net[0].decode()
            status_search = True
    
    counter_bad_connect = 0
    status_connect = False
    if status_search == True:
        log(update="Сеть найдена!")
        while status_connect == False:
            wifi.connect(update_name, pass_network)
            time.sleep(2)
            if wifi.isconnected():
                log(update=f"Подключился к Wi-Fi: {update_name}")
                report(pause=0.1, ping=10)
                status_connect = True
                break
            else:
                log(update="Сеть найдена, но соединение не установлено")
                counter_bad_connect+=1
                report(pause=1, ping=5)
                if counter_bad_connect == 10:
                    break

    else:
        log(update="Сеть не найдена!")
        report(pause=1, ping=10)

    
try:
    connect_wifi()
except Exception as err:
    log(update=err)

