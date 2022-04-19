from osgeo import gdal,ogr,osr
import pyproj
import os
from os import listdir
from os.path import isfile, join
from transition_image import transition_image

path = 'E:/Donnees_stage/Simon_Beurel/Test_Couple_Image/test/ign'
onlyfiles = os.listdir(path)

path = 'E:/Donnees_stage/Simon_Beurel/Test_Couple_Image/test/pleiade'
onlyfiles2 = os.listdir(path)

nb_img = 0

while i < len(onlyfiles): 
    path_to_ign_img = onlyfiles[i]
    path_to_ign_data = onlyfiles[i+1]
    i = i+2

    path_to_file_pleiade = f'pleiade_tif/{nb_img}.tif'
    path_to_new_pleiade_tif = f'result/pleiade/{nb_img}.tif'

    path_to_dim_pleiade = onlyfiles2[0]
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.sytem(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1


    path_to_dim_pleiade = onlyfiles2[1]
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.sytem(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = onlyfiles2[2]
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.sytem(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = onlyfiles2[3]
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.sytem(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = onlyfiles2[4]
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.sytem(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1

    path_to_dim_pleiade = onlyfiles2[5]
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    os.sytem(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
    nb_img+=1





    
