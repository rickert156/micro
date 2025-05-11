# Micropython + ESP32

## Прошивка плат
Необходимо установить утилиту для прошивки плат - esptool  
Ubuntu/Debian
```sh
sudo apt update && sudo apt install esptool -y
```
Endeavouros(Arch)
```sh
echo y | sudo pacman -Syu esptool
```

На Ubuntu/Debian/Sparky по какой-то причине esptool работает криво, из репa арча работает нормально.  
Протестированный(и подошедшие прошивки загружены в firmware)

## GPIO ESP32 
![ESP32](https://github.com/rickert156/micro/blob/main/img/esp32_pinout.png)

Порт(/dev/) у плат - /dev/ttyUSB0
Проверить наличие подключения можно так
```sh
ls /dev/ttyUSB*
```
Форматируем плату
```sh
sudo esptool.py --port /dev/ttyUSB0 erase_flash
```
Пишем прошивку
```sh
sudo esptool.py --baud 460800 write_flash 0x1000 firmware/ESP32_GENERIC-20250415-v1.25.0.bin
```
Встроенный светодиод на GPIO 2  </br>

У меня есть еще плата <strong>ESP32 D1 R32 Wemos</strong>, прошивать ее можно аналогично ESP32 [ESP32 pinout Wemos](https://github.com/rickert156/micro/blob/main/img/esp32_pinout_wemos.png)
Для проверки платы можно подключиться к ней через такие инструменты, как picocom. Сначале ее необходимо установить
```sh
echo y | sudo pacman -Syu picocom
```
Подключаемся к самой плате
```sh
sudo picocom -b 115200 /dev/ttyUSB0
```

## GPIO ESP32-C3 Supermini
![ESP32-C3 Supermini](https://github.com/rickert156/micro/blob/main/img/supermini-esp32-c3-pinout.jpg)

Порт(/dev/) у плат - /dev/ttyACM0  
Проверить наличие подключения можно так
```sh
ls /dev/ttyACM*
```

Встроенный светодиод на GPIO 8  </br>
Пока что в директориях по тестовому файлу, особо там ничего нет. Вожусь с решением проблемы с подключением к wi-fi, по какой-то причине не хочет подключаться </br>

Перед прошивкой нужно форматировать плату
```sh
sudo esptool.py --port /dev/ttyACM0 erase_flash
```

Прошивку можно найти на этой странице [https://micropython.org/download/ESP32_GENERIC_C3/](https://micropython.org/download/ESP32_GENERIC_C3/)  
На оф сайте указано, что такой командой можно прошить плату(немного модифицировал под себя)
```sh
sudo esptool.py --port /dev/ttyACM0 --baud 460800 write_flash 0 firmware/firmware.bit
```
Имя бинарника нужно будет заменить на актуальное </br>
Конкретно в моем случае подошла вот эта прошивка SP32_GENERIC_C3-20241129-v1.24.1.bin и только со второго раза
```sh
sudo esptool.py --port /dev/ttyACM0 --baud 460800 write_flash 0 firmware/ESP32_GENERIC_C3-20241129-v1.24.1.bin
```

## Resources
- Прошивки micropython [https://micropython.org/download/](https://micropython.org/download/)
