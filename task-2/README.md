# Описание к скрипту для поиска MTU.

В реализации скрипта используется утилита ping. Представлен образ ubuntu 18.04 для подтверждения работы. Но скрипт готов выполняться и macos.

Сборка и запуска образа

``` 
docker build -t mtu_img .
docker run -i -t mtu_img 
```

Запуск скрипта
``` 
python3 mtu_finder.py host
```
Параметры скрипта можно посмотреть через 
```
python3 mtu_finder.py -h
PMTUD

positional arguments:
  host        discovery host

optional arguments:
  -h, --help  show this help message and exit
  -c C        count of ping by one discovery, by default 1
  -v          verbose mod
```
