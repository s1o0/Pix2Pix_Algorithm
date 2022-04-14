import pyproj

wgs_leigon = pyproj.Transformer.from_crs(4326,25000)

leigValues = wgs_leigon.transform(3079.0,1400.0)

print(leigValues)
