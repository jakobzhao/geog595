# created on Dec 24, 2020
# @author:          Bo Zhao (zhaobo@uw.edu), Angel Lin(XXX@uw.edu)
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     XXXXXXX


from sense_hat import SenseHat


sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

print("temp: %.2f, humidity: %.2f, pressure: %.2f" % (pressure, temp, humidity))
