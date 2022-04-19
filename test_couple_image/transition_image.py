from osgeo import gdal,ogr,osr
import pyproj
import os

def transition_image(path_to_dim_pleiade,path_to_file_pleiade,path_to_ign_data,path_to_new_pleiade_tif):
    
    os.system(f'gdal_translate -of GTiff -co COMPRESS=NONE -co BIGTIFF=IF_NEEDED {path_to_dim_pleiade} {path_to_file_pleiade}')

    with open(path_to_ign_data, 'r') as fp:
        # lines to read
        line_numbers = [8, 10]
        for i, line in enumerate(fp):
            # read line 8 and 10
            if i==8:
                lhs, rhs = line.split(" ", 1)
                twoparse = lhs.split(",")
                x_haut_gauche_string = twoparse[0].replace('(', '')
                y_haut_gauche_string = twoparse[1].replace(')', '')

                x_haut_gauche = float(x_haut_gauche_string)
                y_haut_gauche = float(y_haut_gauche_string)
            elif i==10:
                lhs, rhs = line.split(" ", 1)
                twoparse = lhs.split(",")
                x_bas_droite_string = twoparse[0].replace('(', '')
                y_bas_droite_string = twoparse[1].replace(')', '')

                x_bas_droite = float(x_bas_droite_string)
                y_bas_droite = float(y_bas_droite_string)
            elif i > 10:
                # don't read after line 10 to save time
                break

    proj = pyproj.Transformer.from_crs(2154, 4326, always_xy=True)
    x_haut_gauche,y_haut_gauche = proj.transform(x_haut_gauche,y_haut_gauche)
    x_bas_droite,y_bas_droite = proj.transform(x_bas_droite,y_bas_droite)

    '''
    print("*---------------*")
    print(x_haut_gauche)
    print(y_haut_gauche)
    print()
    print(x_bas_droite)
    print(y_bas_droite)
    '''

    x_min = min(x_bas_droite,x_haut_gauche)
    x_max = max(x_bas_droite,x_haut_gauche)

    y_min = min(y_bas_droite,y_haut_gauche)
    y_max = max(y_bas_droite,y_haut_gauche)

    '''
    print("*--------------*")
    print()
    print(x_min)
    print(y_min)
    print()
    print(x_max)
    print(y_max)
    '''
    os.system(f'gdalwarp -s_srs EPSG:4326 -t_srs EPSG:4326 -te {x_min} {y_min} {x_max} {y_max} -te_srs EPSG:4326 {path_to_file_pleiade} {path_to_new_pleiade_tif}')
