from osgeo import gdal,ogr,osr
import pyproj
import os
from os import listdir
from os.path import isfile, join
from transition_image import transition_image
from parse_folder import parse_name_file,parse_folder
from percent_black import percent_black_pixels
#######RENSEIGNER LE DOSSIER IGN###########
path = './test/ign/p1/'
onlyfiles = parse_folder(path)

path = './test/pleiade/'
onlyfiles2 = os.listdir(path)

nb_img = 0
i=0


while i < len(onlyfiles):
    print(f'Level {i}/{len(onlyfiles)}')
    #######RENSEIGNER LE DOSSIER ##############
    path_to_ign_img = f'test/ign/p1/{onlyfiles[i]}.ecw'
    path_to_ign_data = f'test/ign/p1/{onlyfiles[i]}.tab'
    i = i+1


    print()
    print(path_to_ign_img)
    print(path_to_ign_data)
    print()

    path_to_file_pleiade = f'pleiade_tif/{nb_img}.tif'
    path_to_new_pleiade_tif = f'result/pleiade/{nb_img}.tif'
    path_to_dim_pleiade = f'test/pleiade/p1/DIM_PHR1A_MS_202107121137240_SEN_5835792201-2.XML'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    pixels_noirs = percent_black_pixels(f'./result/pleiade/{nb_img}.tif')
    if pixels_noirs >=65.0:
        os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
        nb_img+=1
    else:
        os.system(f'rm ./result/pleiade/{nb_img}.tif')
        print(f'File destroy because {pixels_noirs}% of black_pixels')
    
    print()

    path_to_file_pleiade = f'pleiade_tif/{nb_img}.tif'
    path_to_new_pleiade_tif = f'result/pleiade/{nb_img}.tif'
    path_to_dim_pleiade = f'test/pleiade/p2/DIM_PHR1A_MS_202107121137590_SEN_5835793201-2.XML'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    pixels_noirs = percent_black_pixels(f'./result/pleiade/{nb_img}.tif')
    if pixels_noirs >=65.0:
        os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
        nb_img+=1
    else:
        os.system(f'rm ./result/pleiade/{nb_img}.tif')
        print(f'File destroy because {pixels_noirs}% of black_pixels')

    print()

    path_to_file_pleiade = f'pleiade_tif/{nb_img}.tif'
    path_to_new_pleiade_tif = f'result/pleiade/{nb_img}.tif'
    path_to_dim_pleiade = f'test/pleiade/p3/DIM_PHR1A_MS_202107121137328_SEN_5835794201-2.XML'
    transition_image(path_to_dim_pleiade, path_to_file_pleiade, path_to_ign_data, path_to_new_pleiade_tif)
    pixels_noirs = percent_black_pixels(f'./result/pleiade/{nb_img}.tif')
    if pixels_noirs >=65.0:
        os.system(f'cp {path_to_ign_img} result/ign/{nb_img}.ecw')
        nb_img+=1
    else:
        os.system(f'rm ./result/pleiade/{nb_img}.tif')
        print(f'File destroy because {pixels_noirs}% of black_pixels')

    print()