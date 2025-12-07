grib = {}
while (s := input()) != '':
    grib[s] = grib.get(s, 0) + 1

print(grib)