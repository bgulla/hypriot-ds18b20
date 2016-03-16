# DS18B20 Temperature Sensor + Docker + REST

This repo builds an ARM compatible Docker image that will output the values of DS18B20 sensors connected to a Raspberry Pi.

## GPIO Sensors are hard, use REST!
The container binds to a provided port and outputs the sensor data in easy to ingest JSON blobs. 

`curl http://hypriothost:8080/rest/v1.0/temperature/`
```json
{"28-00000483ba1a": "62.9366", "28-00000471c98d": "64.2866", "28-00000677f123": "48.7616"}
```

## Prerequesites
[Adafruit has an awesome guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20) but in short do the following commands:


`echo 'dtoverlay=w1-gpio' >> /boot/config.txt`

`echo 'w1-gpio' >> /etc/modules`

`echo 'w1-therm' >> /etc/modules`

`reboot`


## How to build
Building the image is straight forward:

* Git clone this repo
* `docker build -t hypriot-ds18b20`
* or `docker-compose up`

