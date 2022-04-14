from osgeo import gdal,ogr,osr
import numpy as np
import matplotlib.pyplot as plt
import pyproj
import os

print("Début......")
print("*--------------------*")
#Open the first file (Pleiade)
file = input("Pleiade File :")
ds = gdal.Open(file)
print("Fichier ouvert!")


#On récupère les coordonnées des angles
ulx, xres, xskew, uly, yskew, yres = ds.GetGeoTransform()
lrx = ulx + (ds.RasterXSize * xres)
lry = uly + (ds.RasterYSize * yres)


print("Coordonées récupérées!")
print(str(ulx)+" "+str(uly)+" "+str(lrx)+" "+str(lry)+" ")
#On traduit ces coordonées
wgs_leigon = pyproj.Transformer.from_crs(4326,2154)
#leigon_wgs = pyproj.Transformer.from_crs(2154,4326)

leigValues = wgs_leigon.transform(lrx, lry)
print(leigValues)
leigValues2 = wgs_leigon.transform(ulx,uly)
print(leigValues2)
print("Coordonées traduites")
file_ign = input("IGN File :")
#On cut l'image IGN
x_min = leigValues[0]
y_min = leigValues[1]
x_max = leigValues[2]
y_max = leigValues[3]
commande = "gdwalwarp -te "+x_min+" "+y_min+" "+x_max+" "+y_max+" "+file_ign+" "+file_ign
os.system(commande)
print("Done ! you can check now")
print("*-------------------------------*")

