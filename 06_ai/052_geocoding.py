import geocoder

with open("assets/gay-seattle-places-geocoded.csv", "w", encoding="utf8") as geofp:
    geofp.write("name, frequency, lat, lng\n")
    with open("assets/gay-seattle-places.csv", "r", encoding="utf8") as fp:
        for line in fp.readlines():
            location = line.split(",")[0]
            freq = int(line.split(",")[1])
            try:
                g = geocoder.arcgis(location)
                lat = g.current_result.lat
                lng = g.current_result.lng
                geofp.write("%s, %d, %f, %f\n" % (location, freq, lat, lng))
                print(location, freq, lat, lng)
            except:
                pass
print("finished!")
