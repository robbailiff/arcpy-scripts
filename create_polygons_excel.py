# Import libraries
import os, openpyxl, csv, arcpy

print("Program Started.")

# List of all timeslices from Permian to Pleistocene
timeslices = ['Asselian', 'Sakmarian', 'Artinskian', 'Kungurian', 'Roadian', 'Wordian', 'Capitanian', 'Wuchiapingian', 'Changhsingian', 'Induan', 'Olenekian', 'Anisian', 'Ladinian', 'Carnian', 'Norian', 'Rhaetian', 'Hettangian', 'Sinemurian', 'Pliensbachian', 'Toarcian', 'Aalenian', 'Bajocian', 'Bathonian', 'Callovian', 'Oxfordian', 'Kimmeridgian', 'Tithonian', 'Berriasian', 'Valanginian', 'Hauterivian', 'Barremian', 'Aptian', 'Albian', 'Cenomanian', 'Turonian', 'Coniacian', 'Santonian', 'Campanian', 'Maastrichtian', 'Danian', 'Selandian', 'Thanetian', 'Ypresian', 'Lutetian', 'Bartonian', 'Priabonian', 'Rupelian', 'Chattian', 'Aquitanian', 'Burdigalian', 'Langhian', 'Serravalian', 'Tortonian', 'Messinian', 'Zanclean', 'Piacenzian', 'Gelasian', 'Pleistocene']

# Set working directory and switch to it
working_folder = r'C:\Users\rgjb\Desktop'
os.chdir(working_folder)

# Open excel workbook and select the sheet you want to open
xl_file = openpyxl.load_workbook('GS_Aus.xlsx')
sheet = xl_file.get_sheet_by_name("Sheet1")

# Empty list for adding formatting columns       
formatted_rows = []

# Iterate through each row of the spreadsheet and retrieve the data
for row in range(1, sheet.max_row + 1):
    ref_id = sheet.cell(row, column=1).value
    age = sheet.cell(row, column=2).value
    name = sheet.cell(row, column=3).value
    file_name = '_' + str(ref_id) + '_' + name + '_' + age
# Append each column list to the main formatted row list
    formatted_rows.append(file_name)

# Set output location
output_dir = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Redigitised_Paleo.gdb"
# Location of file to be used for spatial reference
sp_ref = r"S:\PROGRAMMES\Globe_2021\ConfidencePolygons\PalaeoAtlases\Atlases\GS_Aus_Atlas\GS_Aus_Outlines_Working.gdb\GS_Aus_Crt_all"

# Create a count object
count = 0

for name in formatted_rows:
    arcpy.CreateFeatureclass_management(output_dir, name, "POLYGON", spatial_reference = sp_ref)
    count += 1
    print("Number of polygons created: %s" % (count))

print("Program Complete.")