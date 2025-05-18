from machine import Pin, SPI
import os
from lib.sdcard import SDCard

def sd_connect():
    # Настраиваем SPI
    spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

    # Инициализация SD-карты через SPI
    sd = SDCard(spi, Pin(5))  # CS на GPIO 5

    # Монтируем SD-карту на файловую систему
    try:
        os.mount(sd, "/sd")
        ls = os.listdir('/sd')
        print(f"SD-карта успешно смонтирована!\nСодержимое SD-карты: {ls}")
    except Exception as err:
        print(f"Ошибка монтирования SD-карты: {err}" )

sd_connect()
