#Import libraries
import arcpy

print("Program Started.")

# Location of input and output folders
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\WCSB_Atlas\WCSB_Redigitised_paleo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\WCSB_Atlas\WCSB_Outlines_Working.gdb\_13200_15_01"

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\WCSB_Atlas\WCSB_Outlines_Working.gdb"
featureclasses = arcpy.ListFeatureClasses()

# Create a count object
count = 0

# Iterate through the filtered list, trim each file name and create new feature class with that name
for item in featureclasses:
	if item[-4:] == '_ROT':
	    name = item[:-4]
	    arcpy.CreateFeatureclass_management(output_dir, name, "POLYGON", spatial_reference = sp_ref)
	    count += 1
        print("Number of polygons created: %s" % (count))

print("Program Complete")