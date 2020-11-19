# Import system modules
import arcpy

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Rocky_Mtn_1972_Atlas\Rotated.gdb"
featureclasses = arcpy.ListFeatureClasses()


# Iterate through the feature class list and rename each file
for file_name in featureclasses:
    new_name = file_name + "_ROT"
    arcpy.Rename_management(file_name, new_name, "FeatureClass")
