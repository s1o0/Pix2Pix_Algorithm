from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

ds = gdal.Open("IMG_PHR1A_MS_201802121120006_SEN_2710546101-002_R1C1.JP2")

proj = ds.GetGeoTransform()
print(proj)
print()
print()
print()



dqReprj = gdal.Warp("x.tif", ds, dstSRS="EPSG:4326")

dx = gdal.Open("x.tif")
gx = dx.GetGeoTransform()
print(gx)

