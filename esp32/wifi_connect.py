from config import name_network, pass_network
import network, machine
import time

def log(update:str):
    with open('log.txt', 'a+') as file:
        file.write(f'{update}\n')

def connect_wifi():
    try:
        wifi = network.WLAN(network.STA_IF)
        wifi.active(True)
        time.sleep(2)
        networks = wifi.scan()

        counter_detected = 0
        
        for net in networks:
            if name_network == net[0].decode():
                counter_detected+=1
                if not wifi.isconnected():
                    wifi.connect(name_network, pass_network)
                    time.sleep(10)
            
                    if wifi.isconnected():
                        log(update=f"Connect to: {name_network}")
                    else:
                        log(update=f"Not Connected to: {name_network}")

                break
        if counter_detected == 0:
            log(update=f"{name_network} not found")


    except Exception as err:
        log(update=err)

connect_wifi()
