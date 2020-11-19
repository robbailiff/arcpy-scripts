# Import system modules
import arcpy

print("Program Started")

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Vinogradov_Atlas\Vinogradov_Outlines_Working.gdb"
featureclasses = arcpy.ListFeatureClasses()

# Create a count object
count = 0

# Iterate through the feature class list and rename each file
for file_name in featureclasses:
    if file_name[0] == '_':
        new_name = file_name + "_ROT"
        arcpy.Rename_management(file_name, new_name, "FeatureClass")
        count += 1
        print("Number of polygons renamed: %s" % (count))

print("Program Complete")
