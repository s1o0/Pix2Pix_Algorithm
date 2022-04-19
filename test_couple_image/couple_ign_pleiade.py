from osgeo import gdal,ogr,osr
import pyproj
import os
from os import listdir
from os.path import isfile, join
from transition_image import transition_image

path = './test/ign/'
onlyfiles = os.listdir(path)

path = './test/pleiade/'
onlyfiles2 = os.listdir(path)

nb_img = 0
i=0
while i < len(onlyfiles): 
    path_to_ign_img = f'test/ign/{onlyfiles[i]}'
    path_to_ign_data = f'test/ign/{onlyfiles[i+1]}'
    i = i+2

    path_to_file_pleiade = f'pleiade_tif/{nb_img}.tif'
    path_to_new_pleiade_tif = f'result/pleiade/{nb_img}.tif'

    path_to_dim_pleiade = f'test/pleiade/p1/DIM_PHR1A_MS_202107121137240_SEN_5835792201-2.XML'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1


    path_to_dim_pleiade = f'test/pleiade/p2/DIM_PHR1A_MS_202107121137590_SEN_5835793201-2.XML'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = f'test/pleiade/p3/DIM_PHR1A_MS_202107121137328_SEN_5835794201-2.XML'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    '''path_to_dim_pleiade = f'test/pleiade/{onlyfiles2[3]}'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = f'test/pleiade/{onlyfiles2[4]}'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = f'test/pleiade/{onlyfiles2[5]}'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1'''





    
