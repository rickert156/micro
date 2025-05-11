# Micropython + ESP32

## Прошивка плат
Необходимо установить утилиту для прошивки плат - esptool  
Ubuntu/Debian
```sh
sudo apt update && sudo apt install esptool -y
```
Endeabouros(Arch)
```sh
sudo pacman -Syu esptool
```

На Ubuntu/Debian/Sparky по какой-то причине esptool работает криво, из репо арча работает нормально. 

## GPIO ESP32 
![ESP32](https://github.com/rickert156/micro/blob/main/img/esp32_pinout.png)
Встроенный светодиод на GPIO 2

## GPIO ESP32-C3 Supermini
![ESP32-C3 Supermini](https://github.com/rickert156/micro/blob/main/img/supermini-esp32-c3-pinout.jpg)
Встроенный светодиод на GPIO 8  </br>
Пока что в директориях по тестовому файлу, особо там ничего нет. Вожусь с решением проблемы с подключением к wi-fi, по какой-то причине не хочет подключаться
