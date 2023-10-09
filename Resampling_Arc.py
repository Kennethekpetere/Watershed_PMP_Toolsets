# Import Libraries 
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "ResampledPMP"
env.scratchWorkspace = "temp"
env.overwriteOutput=True

# Read and create rasters
pmp30m = Raster("PMP30mKs.tif"); pmp1h = Raster("PMP1hKs.tif"); pmp2h = Raster("PMP2hKs.tif") 
pmp3h = Raster("PMP3hKs.tif"); pmp6h = Raster("PMP6hKs.tif"); pmp12h = Raster("PMP12hKs.tif") 
pmp24h = Raster("PMP24hKs.tif"); pmp2d = Raster("PMP2DKs.tif"); pmp3d = Raster("PMP3DKs.tif")


# # take a look on the rasters. Can also use RasterInfo class.
# print(pmp30m.path,pmp30m.spatialReference)
# print(pmp30m.bandCount, pmp30m.height, pmp30m.width)
# print(pmp30m.pixelType,pmp30m.noDataValue)


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


# Perform Analyses

# Set the local variables
inputRas = pmp3d
outputRas = "res3DPMPKs.tif"
# Convert the PMP rasters into a list
pmp_list = [pmp30m, pmp1h, pmp2h, pmp3h, pmp6h, pmp12h, pmp24h, pmp2d, pmp3d]
# set output variables
exp = ["RS30mPMP.tif", "RS1hPMP.tif", "RS2hPMP.tif", "RS3hPMP.tif", "RS6hPMP.tif", "RS12hPMP.tif", "RS24hPMP.tif", "RS2DPMP.tif", "RS3DPMP.tif"]

# Execute Resampling in arcpy
# for i in pmp_list:
#     print("Start Resampling")
#     arcpy.Resample_management(i, exp, "30", "BILINEAR")

print("Start Resampling")
arcpy.Resample_management(inputRas, outputRas, "0.00026634684", "BILINEAR") # 0.00026634684 = 30m   0.09881468125314735/371 = 0.00026634684
# arcpy.Resample_management(inputRas, outputRas, "10", "BILINEAR")


#check in Spatial Analyst
arcpy.CheckInExtension("Spatial")

print("Done")