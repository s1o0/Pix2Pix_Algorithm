from osgeo import gdal
from osgeo import gdal,ogr,osr
import os


#Transition de l'image pleiade vers le lambert
filename = r"C:\path\to\input\raster
input_raster = gdal.Open(filename)
output_raster = r"C:\path\to\output\raster
warp = gdal.Warp(output_raster,input_raster,dstSRS='EPSG:2154')
warp = None 

#Obtenir les infos de l'images pleiade transformée
src = gdal.Open(path goes here)
ulx, xres, xskew, uly, yskew, yres  = src.GetGeoTransform()
lrx = ulx + (src.RasterXSize * xres)
lry = uly + (src.RasterYSize * yres)


#Crop l'image ign ou avion
window = (ulx,uly,lrx,lry)

gdal.Translate('output_crop_raster.tif', 'input_raster.tif', projWin = window)

