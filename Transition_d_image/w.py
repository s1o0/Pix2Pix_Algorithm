import os
from osgeo import gdal,osr,ogr
import osgeo.gdal
osgeo.gdal.GetDriverByName
import numpy as np
import xml.etree.ElementTree as ET
import numpy

def getprojection(raster):
    try:
        print('----Get the projection of '+os.path.basename(raster))
        ds = gdal.Open(raster) #open the granule
        prj = ds.GetProjection() #get its projection
        geotransform = ds.GetGeoTransform() #
        ds = None
        pixelwidth = geotransform[1] #give us the spatial resolution
        pixelheight = geotransform[-1]
        srs=osr.SpatialReference(wkt=prj)
        #print('\nThe layer you load has :')
        #print('-Geographic Coordinate System (GCS) = EPSG:'+str(srs.GetAttrValue("GEOGCS|AUTHORITY", 1))) #give us the GCS (Geographic Coordinate System of the data)
        #print('-Projected Coordinate Systems (PROJCS) EPSG:'+str(srs.GetAttrValue("PROJCS|AUTHORITY", 1))+'('+str(srs.GetAttrValue("PROJCS|PROJECTION", 1))+')') #give us the Projected Coordinate System of the data
        SRS='EPSG:'+srs.GetAttrValue("PROJCS|AUTHORITY", 1)
        #print('SRS '+os.path.basename(raster)+'\n'+SRS)
        return pixelwidth, pixelheight, SRS
    except:
        print('Could not grab SRS for'+raster)

getprojection("IMG_PHR1A_MS_002/IMG_PHR1A_MS_202103261030221_SEN_5672535101-2_R1C1.JP2")
