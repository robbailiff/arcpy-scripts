# Import system modules
import arcpy

print("Program Started.")

# Set up workspace and then list the feature classes for that workspace
arcpy.env.workspace = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Outlines_Working.gdb"
featureclasses = arcpy.ListFeatureClasses()

# Set output location
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Redigitised_Paleo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Outlines_Working.gdb\GS_Aus_Crt_all"

# Iterate through the feature class list and create a polygon with the same name
for file_name in featureclasses:
	arcpy.CreateFeatureclass_management(output_dir, file_name, "POLYGON", spatial_reference = sp_ref)

print("Program Complete.")