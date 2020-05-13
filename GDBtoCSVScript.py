# Import arcpy module
import arcpy
import time
from arcpy import env
import os.path  
#from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = r"T:\Students\reid98\Final Project\Data3.gdb"

arcpy.env.overwriteOutput = True

in_dir = arcpy.env.workspace

out_dir = r"T:\Students\reid98\Final Project\ZSTables\\"

input_Tables = arcpy.ListTables()

for x in input_Tables:
    arcpy.CopyRows_management(x, out_dir + x + ".csv")
    print x + " copied"
