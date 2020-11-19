#Import libraries
import os, arcpy

# Location of input and output folders
input_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Rotated.gdb"
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Redigitised_Palaeo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Present_Day.gdb\_3617_J_5"

# List of image file extensions to be kept in the file list
ext = ['.bmp', '.jpg']

# List all the file names in the input directory
file_list = os.listdir(input_dir)
# Remove non image files from the list
#filtered_list = [x for x in file_list if x[-4:] in ex]

# Iterate through the filtered list, trim each file name and create new feature class with that name
for item in file_list:
	name = item + "_Redig"
	arcpy.CreateFeatureclass_management(output_dir, name, "POLYGON", spatial_reference = sp_ref)

print("Program Complete")