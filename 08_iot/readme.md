# Practical Exercise 7: Environmental data collection in real time with Raspberry Pi

**Instructor:** Bo Zhao, zhaobo@uw.edu; **Points Available** = 50

In this practical exercise, you will learn how to set up a Raspberry Pi,  collect environmental data (pressure, temperature, and humidity) using a Sense HAT, synchronize the collected data to GitHub for real-time GIS, and schedule an auto-run task using crontab. The aim of this project is to briefly introduce how a Raspberry Pi can be a great platform for building Internet of Things (IoT). At the end of the tutorial, you are expected to know how to connect sensors to a Raspberry Pi, and how to set up an automated task to synchronize data from local device to the cloud. Ok, let's get started!

## 1. Preparation
A Raspberry Pi is a low cost, credit-card size electronic board that is able to do everything a computer can do. It allows you to connect to various external accessories (such as sensors) and create applications to use the data collected. For this practical exercise, we will be using Sense HAT as our sensor.

### 1.1 What You Will Need

  - [Raspberry Pi 4 Model B](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_5?keywords=raspberry+pi&qid=1579033237&sr=8-5)
      - Although we are using the latest version, you can check out the older versions with lower cost on this [page](https://www.raspberrypi.org/products/).
  - [NOOBS Preloaded Micro SD Card](https://www.amazon.com/Raspberry-Noobs-Preloaded-Compatible-Models/dp/B07LB7L3D9/ref=sr_1_7?keywords=raspberry+pi+preloaded+sd+card+noobs&qid=1579036836&sr=8-7)
      - You can also buy a plain SD card and install NOOBS/Raspbian yourself (https://www.raspberrypi.org/downloads/).
  - [Sense HAT](https://www.amazon.com/Raspberry-Pi-Sense-HAT-AstroPi/dp/B014HDG74S)
  - [Solar recharger](https://www.amazon.com/24000mAh-Waterproof-Portable-Compatible-Smartphones/dp/B07C24XC2L/ref=sr_1_1_sspa?keywords=solar+recharger&qid=1579034413&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyN0FRQkdNQ0JIS1paJmVuY3J5cHRlZElkPUEwOTAyNjk1MjZQRldTMDRKOFM2ViZlbmNyeXB0ZWRBZElkPUEwNjA3NTAwM04xMjJMSlBRMElLRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) (optional) usage outdoor deployment
  - Type C USB charger
  - Micro HDMI Cable
  - Monitor, Mouse, Keyboard (configuration)

<!---
- [Camera Module (Standard Version)](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS?ref_=ast_bbp_dp&th=1&psc=1)
  - [Camera Module (Night Version)](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B071WP53K7?ref_=ast_bbp_dp&th=1) (optional)
--->

The total cost is around $150 in total, depending on the amount of accessary added. Besides Sense HAT, there are other [sensors]( https://www.amazon.com/kuman-K5-USFor-Raspberry-Projects-Tutorials/dp/B016D5L5KE/ref=sr_1_3?crid=2AQDFL3J1N0TQ&keywords=raspberry+pi+sensors&qid=1578694540&sprefix=rasp%2Caps%2C199&sr=8-3) available online for purchase. If you are interested in learning some cool projects that Raspberry Pi can do, check out this [article](https://www.ubuntupit.com/20-best-raspberry-pi-projects-that-you-can-start-right-now/)!


### 1.2 Environment Setup and Software Installation

#### 1.2.1 Assemably
  ![Assembly Parts](img/assembly_1.jpg)

  ![Assembly Parts](img/assembly_4.jpg)

  ![Assembly Parts](img/assembly_5.jpg)

  After everything is plugged in, the environment setup should look like this:

  ![Assembly Parts](img/assembly_3.jpg)




#### 1.2.2 Raspberry Pi Installation Operating System (Linux)

Now, we can go ahead and turn on the Raspberry Pi. On the first boot, the system will automatically expand the file system on the SD card.

  ![Assembly Parts](img/screen_1.JPG)

It will automatically reboot, and you will see a rainbow screen.

  ![Assembly Parts](img/screen_2.JPG)

After a few seconds, it will bring you to the Raspbian desktop.

  ![Assembly Parts](img/screen_3.JPG)

Complete the following steps to set up Raspberry Pi:

  - Click [Next].
  - Set [Country] to "United States"; [Language] to "American English"; [Timezone] to "Los Angeles".
  - Check both [Use English language] and [Use US keyboard].
  - Click [Next].
  - It is highly encouraged to create a new password. But if not, the original password is "raspberry".
  - Click [Next].
  - Select a WiFi network and click [Next], or [Skip] to continue without connecting.
  - Click [Next].
  - Enter the WiFi password and click [Next], or [Skip] to continue without connecting.
  - Update Software: Click [Next].
  - Click [OK].
  - Click [Restart].
  - Now we are ready to use Raspbeery Pi as a PC.

#### 1.2.3 Install the Sense HAT Packages

  - Connect to WiFi or ethernet.
  - Open Terminal (Shortcut: Ctrl + Alt + T).

  ![Terminal](img/terminal.jpg)
  - Within the terminal window, type in the following commands to install Sense HAT.
  ```shell
  sudo apt-get update # manually update the operating system
  sudo apt-get install sense-hat # install the Sense HAT package
  ```

<!---
  - To connect the Camera Module, click [Menu] > [Preferences] > [Raspberry Pi Configuration]:

  ![Raspberry Pi Configuration](img/config.png)
  - Select [Interfaces] and ensure that the camera is "Enabled":

  ![Raspberry Pi Configuration](img/interfaces.png)

  - Click [OK].
  - Open the terminal window and type in the following command.
  ```shell
  sudo reboot # reboot Raspberry Pi
  ```
--->

#### 1.2.4 Test Out Python Codes

  Now we will learn how to control a Sense HAT using Python codes.
  - To open Python IDE, click [Menu] > [Programming] > [Thonny Python IDE].
  - In your Python program, type in the following lines of code to set up your connection with the Sense HAT:
  ```Python
  from sense_hat import SenseHat
  sense = SenseHat()
  ```
  - Add this code to display a message on the Sense HAT's LED matrix.
  ```Python
  sense.show_message("Hello RPi")
  ```
  - Save your file as "Test Sense HAT.py" on your desktop.
  - Click the green play button to execute the codes. The message is displayed:

  ![Message Display](img/display.gif)

<!---
  - Open a new file to try out codes for taking pictures.
  - Enter the following codes:
  ```Python
  from picamera import picamera
  from time import sleep

  camera = PiCamera()

  camera.start_preview()
  sleep(5)
  camera.capture('/home/pi/Desktop/image.jpg')
  camera.stop_preview()
  ```
  - Save your file as "Test Camera.py" on your desktop then run the codes.
  - Your new image should be saved to the Desktop:

  ![Picture Display](img/imagee.jpg)
--->

## 2. Sense HAT: Collecting Environmental Data

The Sense HAT is an add-on board for Raspberry Pi that has a set of environmental sensors for detecting the surrounding conditions, including gyroscope, accelerometer, magnetometer, temperature, barometric pressure and humidity. There are tons of interesting [projects](https://projects.raspberrypi.org/en/projects?hardware[]=sense-hat) that can be made using Sense HAT.

For this tutorial, we will use Sense HAT to measure pressure, temperature, and humidity. We will use Python to run the program, and learn how to store the collected data into a CSV file (please refer to  [`01_env_sensor.py`](01_env_sensor.py).)

In a Python file, enter the following codes:
```Python
# Import the sense_hat module and instantiate a SenseHat object
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
temperature = sense.get_temperature()
humidity = sense.get_humidity()

print("pressure: %.2f, temperature: %.2f, humidity: %.2f" % (pressure, temperature, humidity))
```
After running the program, you should get something like this:
```Python
pressure: 1010.81, temperature: 37.74, humidity: 31.91
```
It would be useful if the data can be stored somewhere. For this exercise, we will store our environmental data in to a CSV file named `env.csv` within the `assets` folder. To write the data to a file, you first need to create it. At the end of the program, add the following line:
```Python
with open("assets/env.csv", "a", encoding="utf8") as fp:
```
This creates a new file called `env.csv` and opens it in "append" mode, so that lines are only written to the end of the file. Now you want to write the current timestamp, pressure, temperature, humidity data to `env.csv`:
```Python
with open("assets/env.csv", "a", encoding="utf8") as fp:
  fp.write("%d, %.2f, %.2f, %.2f \n" % (timestamp, pressure, temperature, humidity))
```
Each time you run the entire program, a new row of data will be added to the `env.csv` file.

To learn more about what a Sense Hat can do, please refer to the Python libraries at https://github.com/astro-pi/python-sense-hat.

## 3. Monitoring the Environmental Variables with Real-Time GIS
<!--
[client(RPI)] <-> Server <-> [Cloud Storage(GitHub(command line), Dropbox[python dropbox], Google Drive[python google dirve], Linux[rsync])]
-->

Now we have the data stored in our local drive, let's synchronize those data to the cloud, in this case, GitHub. With real-time GIS, you will have the ability to simultaneously tap into, analyze, and display streaming data collected from the Raspberry Pi sensors.

### 3.1 Synchronizing Data to GitHub
In the  [`iot.sh`](iot.sh) file, we (1) pull the latest data from GitHub (2) run the [`01_env_sensor.py`](01_env_sensor.py) to collect pressure, temperature, and humidity data and (3) add and commit changes (4) push the collected data back to GitHub, as shown below:


```shell
cd /home/pi/rpi-iot
sudo git pull https://[github-username]:[github-passowrd]@github.com/jakobzhao/rpi-iot.git
sudo /usr/bin/python3 /home/pi/rpi-iot/01_env_sensor.py
sudo git add .
sudo git commit -a -m 'Env Bot'
sudo git push https://[github-username]:[github-passowrd]@github.com/jakobzhao/rpi-iot.git
```
With this process, you will be able to monitor the collected data remotely in real time.

![env data](img/env_data.JPG)


### 3.2 Setting up `crontab` to Automate Tasks

When using the Raspberry Pi, many times you may have a program you want to automatically start it at boot so that you can use your project without logging in to the Raspberry Pi via SSH or VNC. Automating scripts is simple with `crontab`. Cron is part of the Raspbian operating system which is used to schedule commands or scripts to run periodically and at fixed intervals.

This command is especially useful when you want to run a program in a Raspberry Pi without a monitor. For this exercise, I connected the Raspberry Pi with a solar charger and set it up by the window to measure the changes in pressure, temperature, and humidity in my room. I set up `crontab` to execute `01_env_sensor.py` every minute. This is how the setting looks like:

![RPi remote setup](img/rpi_solar.jpg)


Now, let's learn how to auto-run Python programs on the Raspberry Pi.

- To begin, open up a terminal window.
- Run `crontab` with the `-e` flag to edit the cron table:

```shell
crontab -e
```
- When you first run the `crontab -e` command, you will be asked to select an editor to use. For now, let's use `/bin/nano`.

- In the `crontab` editor, you can add new cron jobs with this syntax:
```powershell
    *    *    *    *    *  COMMABD TO BE EXECUTED
    │    │    │    │    │─────────── Day of week (0 - 7) (Sunday = 0 or 7)
    │    │    │    │──────────────── Month (1 - 12)
    │    │    │───────────────────── Day of month (1 - 31)
    │    │────────────────────────── Hour (0 - 23)
    │─────────────────────────────── Minute (0 - 59)
```

- For this exercise, we will run the `iot.sh` file every minute (to learn how to schedule time, please refer to https://crontab.guru/). We can automate this process using `crontab` with the following code:

```shell
* * * * * sh [local_repository_path]/iot.sh # run iot.sh every minute
```
- To exit the editing environment, press `Crtl+X` and then `Y`.
- To activate the `crontab` schedule, type:

```shell
sudo service cron restart
```
- To check if the `crontab` is executed successfully, type:

```shell
sudo tail -f /var/log/syslog | grep CRON
```
Now, as long as there is power supply, the Raspberry Pi will automatically collect environmental data and update them to the cloud. With this, you can monitor the real-time data via GitHub remotely!

## 4. Deliverable

For the deliverable of this practical excercise, you are expected to collect continous environment data and save it into a github repository. (40 POINTS)

You are also expected to store the python and shell scripts to the repository (5 POINTS) and summarize what you have done in the readme.md (5 POINTS)


Create a repository to store the screenshots and then summarize your work in the `readme.md` file, and insert the screenshots to the `readme.md` file too (10 POINTS).

Also, we encourage you try to visualize the collected data using web based charts. Please refer to the [index.html](index.html) script under the 08_iot folder. This script can be openly accessed from this link: https://jakobzhao.github.io/geog595/08_iot/.

![webpage](img/web.png)


To submit your deliverable, please share the url of the Github repository to the **Canvas Dropbox** of this practical exercise. The file structure of this github repository should look like below.


```powershell
[your_repository]
    │
    │readme.md
    ├─assets
    │    env.csv  # a timely updated data file of the monitored environmental parameters.
```


**Note:** Lab assignments are required to be submitted electronically to Canvas unless stated otherwise. Efforts will be made to have them graded and returned within one week after they are submitted.Lab assignments are expected to be completed by the due date. ***A late penalty of at least 10 percentage units will be taken off each day after the due date.*** If you have a genuine reason(known medical condition, a pile-up of due assignments on other courses, ROTC,athletics teams, job interview, religious obligations etc.) for being unable to complete work on time, then some flexibility is possible. However, if in my judgment you could reasonably have let me know beforehand that there would likely be a delay, and then a late penalty will still be imposed if I don't hear from you until after the deadline has passed. For unforeseeable problems,I can be more flexible. If there are ongoing medical, personal, or other issues that are likely to affect your work all semester, then please arrange to see me to discuss the situation. There will be NO make-up exams except for circumstances like those above.


## Acknowledgement

I want to express my gratitude to Angel Lin who provided me research assistance on developing this assignment. The usual disclaims apply.

## References

https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat

https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

https://www.raspberrypi.org/documentation/hardware/sense-hat/

https://picamera.readthedocs.io/en/release-1.13/recipes1.html

https://github.com/bennuttall/sense-hat-examples/blob/master/python/astro_cam.py

https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS?ref_=ast_bbp_dp&th=1&psc=1


**python libraries**

https://pypi.org/project/sense-hat/

https://github.com/astro-pi/python-sense-hat

https://github.com/bennuttall/sense-hat-examples
