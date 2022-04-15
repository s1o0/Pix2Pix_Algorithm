from osgeo import gdal,ogr,osr
from pyproj import Proj, transform

#####ON ESSAYE D'OBTENIR LES COORDONEES DANS LE REFERENTIEL WGS84 (4326) DES 4 COINS DE L'IMAGE PLEIADE
def GetExtent(ds):
    """ Return list of corner coordinates from a gdal Dataset """
    xmin, xpixel, _, ymax, _, ypixel = ds.GetGeoTransform()
    width, height = ds.RasterXSize, ds.RasterYSize
    xmax = xmin + width * xpixel
    ymin = ymax + height * ypixel

    return (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)

def ReprojectCoords(coords,src_srs,tgt_srs):
    """ Reproject a list of x,y coordinates. """
    trans_coords=[]
    transform = osr.CoordinateTransformation( src_srs, tgt_srs)
    for x,y in coords:
        x,y,z = transform.TransformPoint(x,y)
        trans_coords.append([x,y])
    return trans_coords

raster=r'IMG_PHR1B_MS_002/IMG_PHR1B_MS_202104211119066_SEN_6005996101-2_R1C1.JP2'
ds=gdal.Open(raster)
ext=GetExtent(ds)
src_srs=osr.SpatialReference()
src_srs.ImportFromEPSG(4326)
#tgt_srs=osr.SpatialReference()
#tgt_srs.ImportFromEPSG(4326)
tgt_srs = src_srs.CloneGeogCS()
print("1")
geo_ext=ReprojectCoords(ext, src_srs, tgt_srs)
print(geo_ext)
'''
#####ON TRANSFORME CES COORDONNES DANS LE REFERENTIEL RGF93 (2154)
inProj = Proj('epsg:4326')
outProj = Proj('epsg:2154')
x1,y1 = -11705274.6374,4826473.6922
x2,y2 = transform(inProj,outProj,x1,y1)
print x2,y2


#####ON VEUT CUT L'IMAGE IGN MNT EN UTILISANT LES COORDONNES DE LIMAGE PLEIDA
upper_left_x = 699934.584491
upper_left_y = 6169364.0093
lower_right_x = 700160.946739
lower_right_y = 6168703.00544
window = (upper_left_x,upper_left_y,lower_right_x,lower_right_y)

gdal.Translate('output_crop_raster.tif', 'input_raster.tif', projWin = window)'''