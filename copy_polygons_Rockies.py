#Import libraries
import arcpy

# Location of input and output folders
input_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Rotated.gdb"
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Redigitised_Palaeo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Present_Day.gdb\_3617_J_5"

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_Atlas_1972\Rotated.gdb"
featureclasses = arcpy.ListFeatureClasses()

# Iterate through the filtered list, trim each file name and create new feature class with that name
for item in featureclasses:
    name = item + "_ReDig"
    arcpy.CreateFeatureclass_management(output_dir, name, "POLYGON", spatial_reference = sp_ref)

print("Program Complete")