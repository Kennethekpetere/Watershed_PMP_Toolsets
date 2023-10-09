# Import Libraries 
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "ResampledPMP"
env.scratchWorkspace = "temp"
env.overwriteOutput=True

# Read and create rasters
pmp30mRes = Raster("res30mPMPKs.tif"); pmp1hRes = Raster("res1hPMPKs.tif"); pmp2hRes = Raster("res2hPMPKs.tif") 
pmp3hRes = Raster("res3hPMPKs.tif"); pmp6hRes = Raster("res6hPMPKs.tif"); pmp12hRes = Raster("res12hPMPKs.tif") 
pmp24hRes = Raster("res24hPMPKs.tif"); pmp2dRes = Raster("res2DPMPKs.tif"); pmp3dRes = Raster("res3DPMPKs.tif")

# Convert the PMP rasters into a list
pmp_list = [pmp30mRes, pmp1hRes, pmp2hRes, pmp3hRes, pmp6hRes, pmp12hRes, pmp24hRes, pmp2dRes, pmp3dRes]

# Read in shapefile
huc8 = 'HUC08KS.shp'; huc10 = 'HUC10KS.shp'; huc12 = 'HUC12KS.shp'

# Convert the HUCs into a list
huc_list = [huc8, huc10, huc12]


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


# Perform Analyses

# Name: ZonalStatisticsAsTable_Ex_standalone.py
# Description: Summarizes values of a multidimensional raster within the zones of another dataset and reports the results to a table.
# Requirements: Spatial Analyst Extension


# Set the local variables
inZoneData = huc12
zoneField = "FID"
inValueRaster = pmp3dRes # [pmp30mRes, pmp1hRes, pmp2hRes, pmp3hRes, pmp6hRes, pmp12hRes, pmp24hRes, pmp2dRes, pmp3dRes]
# inValueRaster = []
# for i in pmp_list:
#     i = inValueRaster
# inValueRaster = i

outTable = "KansasHUC12pmp3D.dbf"   # "zonalstatHUC08pmp3d.dbf"

# Execute ZonalStatisticsAsTable
print("Start Operation")
outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster, 
                                 outTable, ignore_nodata = "DATA", 
                                 statistics_type = "MEAN", 
                                 process_as_multidimensional = "CURRENT_SLICE")

#check in Spatial Analyst
arcpy.CheckInExtension("Spatial")

print("Done")