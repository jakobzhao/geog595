# created on Dec 24, 2020
# @author:          Bo Zhao (zhaobo@uw.edu), Angel Lin(XXX@uw.edu)
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     XXXXXXX


from sense_hat import SenseHat

from datetime import datetime
# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

print("temp: %.2f, humidity: %.2f, pressure: %.2f" % (pressure, temp, humidity))

with open("assets/env.csv", "a", encoding="utf8") as fp:
    # fp.write("temp: %.2f, humidity: %.2f, pressure: %.2f" % (pressure, temp, humidity))
    fp.write("%d, %.2f, %.2f, %.2f \n" % (timestamp, pressure, temp, humidity))
