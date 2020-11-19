#Import libraries
import arcpy

# Location of output folder
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Vinogradov_Atlas\Vinogradov_Redigitised_Paleo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Vinogradov_Atlas\Vinogradov_Outlines_Working.gdb\Vinogradov_Cz"

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\Vinogradov_Atlas\Vinogradov_Outlines_Working.gdb"
featureclasses = arcpy.ListFeatureClasses()

# Create a count object
count = 0

# Iterate through the filtered list, trim each file name and create new feature class with that name
for name in featureclasses:
    arcpy.CreateFeatureclass_management(output_dir, name, "POLYGON", spatial_reference = sp_ref)
    count += 1
    print("Number of polygons created: %s" % (count))

print("Program Complete")
