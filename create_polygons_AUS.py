#Import libraries
import os, arcpy

print("Program Started.")

# Location of input folder
input_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\Images"
# Set output location
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Redigitised_Paleo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Outlines_Working.gdb\GS_Aus_Crt_all"

# List of image file extensions to be kept in the file list
ext = ['.bmp', '.jpg']

# List all the file names in the input directory
file_list = os.listdir(input_dir)
# Remove non image files from the list
filtered_list = [x for x in file_list if x[-4:] in ext]

# Create a count object
count = 0

# Iterate through the filtered list, trim each file name and create new feature class with that name
for item in filtered_list:
        if item[0] == 'GS':
                continue
        else:
                name = item[:-4]
                name = "_" + name
                arcpy.CreateFeatureclass_management(output_dir, name, "POLYGON", spatial_reference = sp_ref)
                count += 1
                print("Number of polygons created: %s" % (count))

print("Program Complete.")
