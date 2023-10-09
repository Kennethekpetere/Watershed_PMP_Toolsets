# Import Libraries 
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "Data"
env.scratchWorkspace = "temp"
env.overwriteOutput=True

# Read and create rasters
pmp30m = Raster("PMP30min.tif")
pmp1h = Raster("PMP1hr.tif")
pmp2h = Raster("PMP2hr.tif")
pmp3h = Raster("PMP3hr.tif")
pmp6h = Raster("PMP6hr.tif")
pmp12h = Raster("PMP12hr.tif")
pmp24h = Raster("PMP24hr.tif")
pmp2d = Raster("PMP2D.tif")
pmp3d = Raster("PMP3D.tif")

# Convert the PMP rasters into a list
pmp_list = [pmp30m, pmp1h, pmp2h, pmp3h, pmp6h, pmp12h, pmp24h, pmp2d, pmp3d]

# Read in shapefile
huc2 = 'HUC02.shp'
huc4 = 'HUC04.shp'
huc6 = 'HUC06.shp'
huc8 = 'HUC08.shp'
huc10 = 'HUC10.shp'
huc12 = 'HUC12.shp'

# Convert the HUCs into a list
huc_list = [huc2, huc4, huc6, huc8, huc10, huc12]

# # take a look on the rasters. Can also use RasterInfo class.
# print(pmp30m.path,pmp30m.spatialReference)
# print(pmp30m.bandCount, pmp30m.height, pmp30m.width)
# print(pmp30m.pixelType,pmp30m.noDataValue)


# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")


# Perform Analyses

# Name: ZonalStatisticsAsTable_Ex_standalone.py
# Description: Summarizes values of a multidimensional raster within the zones of another dataset and reports the results to a table.
# Requirements: Spatial Analyst Extension


# Set the local variables
inZoneData = huc2
zoneField = "FID"
inValueRaster = pmp3d # [pmp30m, pmp1h, pmp2h, pmp3h, pmp6h, pmp12h, pmp24h, pmp2d, pmp3d]
# inValueRaster = []
# for i in pmp_list:
#     i = inValueRaster
# inValueRaster = i

outTable = "HUC02pmp3d.dbf"   # "zonalstatHUC08pmp3d.dbf"

# Execute ZonalStatisticsAsTable
outZSaT = ZonalStatisticsAsTable(inZoneData, zoneField, inValueRaster, 
                                 outTable, ignore_nodata = "DATA", 
                                 statistics_type = "MIN_MAX_MEAN", 
                                 process_as_multidimensional = "CURRENT_SLICE")

#check in Spatial Analyst
arcpy.CheckInExtension("Spatial")

print("Done")