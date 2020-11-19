# Import system modules
import arcpy

print("Program starting...")

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Ziegler_WTethys_Atlas\ZIegler_redigitised_paleo.gdb"
featureclasses = arcpy.ListFeatureClasses()


# Iterate through the feature class list and rename each file
for file_name in featureclasses:
    new_name = "_15427_plate_0_" + file_name
    arcpy.Rename_management(file_name, new_name, "FeatureClass")

print("Program Complete.")
