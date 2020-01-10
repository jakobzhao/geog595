# Practical Exercise 7: Environmental data collection in real time with Raspberry Pi

- intro:
  - objective: echo with the title
  - context
    - deep learning based image recognition
    - enviromental data collection
    - open Hardware
    - real-time Cloud
  - outline
    - prep.
      - order Hardware
      - software/environment setup
      - senseHat
      - Camera
      - real-gis

## 1. Preparation

### 1.1 Hardware

what and where to purchase/order Amazon.
  - picture
  - cheap < $100.
  -

the RPi(motherboard), senseHat(other sensors: https://www.amazon.com/kuman-K5-USFor-Raspberry-Projects-Tutorials/dp/B016D5L5KE/ref=sr_1_3?crid=2AQDFL3J1N0TQ&keywords=raspberry+pi+sensors&qid=1578694540&sprefix=rasp%2Caps%2C199&sr=8-3), and camera (normal, night vision)

- RPI (other solutions)
  - https://www.ubuntupit.com/20-best-raspberry-pi-projects-that-you-can-start-right-now/
- solar recharger (optional), usage outdoor deployment
- monitor, mouse, keyboard (configuration)

how much in total.

### 1.2 Software (Environment Setup)

- 1. assemably
  - picutre (parts/labels)
  - References (1 senseHat,2 camera)
  - Note:
  - monitor
- 2. raspberrypi installation operating system (Linux)
  - download operating system.
    - predownload/download by users.(https://www.raspberrypi.org/downloads/)
  - software and packages
    - Python 3
    - Sense HAT for Python 3
    - python library for camera
- 3. turn on the RPi

```
>>>pip install XXXX
```
- 4. install prerequsite pakages and python libraries

```shell
sudo apt-get update
sudo apt-get install sense-hat
sudo reboot
```


- 4. log in info:
  - update username and pwd.(optional)

- 5. Test:

```python
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Hello world!")
```

>
> major python libraries
>  - tensorflow or pytorch
>  - pycamera (double check?)
>  - sensor (double check?)
> - scheduler - crontab
>  - real-time publish the data to a github
> repo (the cloud side).


## 2. Monitoring the environmental variables

The Sense HAT has a set of environmental sensors for detecting the surrounding conditions; it can measure pressure, temperature, and humidity.

refer to the `[01_env_sensor.py](01_env_sensor.py)`.

import the library for XXX
```Python
from sense_hat import SenseHat
```

next, declare vavriable to

```python
sense = SenseHat()
sense.clear()
```
XXXXXX
```python
temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

print("temp: %.2f, humidity: %.2f, pressure: %.2f" % (pressure, temp, humidity))

```


## 3. Recognizing objects from images/videos

3.1 tensorflow, image recognition
3.2

## 4. Synchronizing data to the cloud





## References


https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat

https://www.raspberrypi.org/documentation/hardware/sense-hat/


https://picamera.readthedocs.io/en/release-1.13/recipes1.html

https://github.com/bennuttall/sense-hat-examples/blob/master/python/astro_cam.py

Cameras: https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS?ref_=ast_bbp_dp&th=1&psc=1


**python libraries**

https://pypi.org/project/sense-hat/

https://github.com/astro-pi/python-sense-hat

https://github.com/bennuttall/sense-hat-examples
