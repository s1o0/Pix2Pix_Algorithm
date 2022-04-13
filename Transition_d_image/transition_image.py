from osgeo import gdal
from osgeo import gdal,ogr,osr
import os


#Transition de l'image pleiade vers le lambert
filename = "IMG_PHR1A_MS_201802121120006_SEN_2710546101-002_R1C1.JP2"
input_raster = gdal.Open(filename)
output_raster = "IMG_PHR1A_MS_201802121120006_SEN_2710546101-002_R1C1.JP2"
warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:2154')
warp = None 

#Obtenir les infos de l'images pleiade transformée
src = gdal.Open("IMG_PHR1A_MS_201802121120006_SEN_2710546101-002_R1C1.JP2")
ulx, xres, xskew, uly, yskew, yres  = src.GetGeoTransform()
lrx = ulx + (src.RasterXSize * xres)
lry = uly + (src.RasterYSize * yres)


#Crop l'image ign ou avion
window = (ulx,uly,lrx,lry)

ds = gdal.Open('IMG_PHR1A_MS_201802121120006_SEN_2710546101-002_R1C1.JP2')
ds = gdal.Translate('output.tif', ds, projWin = window)
ds = None
