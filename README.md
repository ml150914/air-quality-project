# air-quality-project

Welcome to air-lab! A particulate matter sensor to measure the concentration of polluting particles at your location!

## What is air-lab? 

In the last years, attention toward environmental question arose consistently - we see the effect of global warming for instance. In particular
the pollution of air and soil is becoming more and more affecting out everyday life. Estimates talk about millions of death every year due to air pollution, due to 
natural or anthropic source. 

The idea of developing low-cost particulate matter sensor is almost [10 years old](https://amt.copernicus.org/preprints/amt-2015-331/amt-2015-331.pdf), with several 
studies and toolkit developed in this context. 

Here, we focus on a simple, cheap and scalable solution to out problem. Following [Rigacci's blog](https://www.rigacci.org/wiki/doku.php/doc/appunti/hardware/raspberrypi_air), we will create a particulate matter-weather station capable of measuring the concentration
of microscopic elements in our enviroment along with atmospheric-pressure, humidity percentage and room-temperature. 

This project started with Livia Conti, scientist and researcher at Italian Istituto Italiano di Fisica Nucleare (INFN) - Sezione di Padova, and then applied to the Air-Lab experience with Sabine Hemmer, technologyst at INFN - Sezione di Padova. The idea was to develope a cheap, scalable, easy to assemble and configure particulate matter sensor to promote the scientific knowledge and culture among the high-school students in Veneto (north-east of Italy). The project succeeded, and we presented it at [ICERI conference 2020](http://dx.doi.org/10.21125/iceri.2022.0794). 

This repo systematize the results, slim the codes and push forward the realization of the sensor, by including a public dashboard where data are automatically loaded and can be visible. 

## Hardware

![alt text](https://github.com/ml150914/air-quality-project/blob/main/img/hardware/Full.jpeg?raw=true)

The particulate matter sensors consists in several parts: its core is the Raspberry Pi 3b+, that will provide the computational power, software and the bus 
connections to the sensors used in this project. The other components are 

- The Humidity-Pressure-Temperature sensor [BME280](https://www.az-delivery.de/en/products/gy-bme280): this component will provide via I2C connection to the Raspi the measures of Humidity (in percentage), Pressure and Temperature. 
- The Real Time Clock [DS1307](https://www.adafruit.com/product/3296?srsltid=AfmBOoqToZsj_g6XT4jFUPPgfDiY9sam4DGW6y4Wb-nZz4YL4SSkPlxn): in this way a clock is provided even if the Raspi is not connected to the WiFi; useful for outdoors measurements.
- The [PMS5003](https://www.aqmd.gov/docs/default-source/aq-spec/resources-page/plantower-pms5003-manual_v2-3.pdf) sensor: cheap and robust sensor that will measure the concentration of particulate matter (PM1.0 - PM2.5 - PM10).

Along with these, you will need of course some basic do-it-yourself stuff like the breadboard for the connections, wires (compatible with the GPIO pins of the Raspi), scissors, tin soldering, insulating tape and a lot of patience!

## Software 

## Check the data!

## Aknowledgments 
