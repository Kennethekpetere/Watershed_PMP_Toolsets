from math import floor
from affine import Affine
import numpy as np
import rasterio
import rasterio.features
import rasterio.warp
from rasterio.plot import show, show_hist

# Input PMP raster 
diff1 = './ImageStat/a30m1h.tif'
diff2 = './ImageStat/b1h2h.tif'
diff3 = './ImageStat/c2h3h.tif'
diff4 = './ImageStat/d3h6h.tif'
diff5 = './ImageStat/e6h12h.tif'
diff6 = './ImageStat/f12h24h.tif'

# Open PMP raster 
pmp30m1h = rasterio.open(diff1)
pmp1h2h = rasterio.open(diff2)
pmp2h3h = rasterio.open(diff3)
pmp3h6h = rasterio.open(diff4)
pmp6h12h = rasterio.open(diff5)
pmp12h24h = rasterio.open(diff6)
diflist = [pmp30m1h, pmp1h2h, pmp2h3h, pmp3h6h, pmp6h12h, pmp12h24h]

# read PMP raster 
pmp30m1h_r = pmp30m1h.read()
pmp1h2h_r = pmp1h2h.read()
pmp2h3h_r = pmp2h3h.read()
pmp3h6h_r = pmp3h6h.read()
pmp6h12h_r = pmp6h12h.read()
pmp12h24h_r = pmp12h24h.read()

diff_list = [pmp30m1h_r, pmp1h2h_r, pmp2h3h_r, pmp3h6h_r, pmp6h12h_r, pmp12h24h_r]

# # show PMP raster
# show(pmp30m1h, cmap='terrain') #'Blues'

# # show PMP histogram
# show_hist(pmp30m1h, bins=50)
# # show_hist(pmp30m1h, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")

for i in diff_list:
    #Loop through the list of difference maps 
    # Find PMP cells with value < 0 using comparison operators
    totPixels = np.sum(i)  # Total Pixel Count 

    inv = np.where(i < 0)    # Inverted Pixel Count   # skipna=True,  maskna='multi',  
    Noninv = np.where(i >= 0)    # Non-Inverted Pixel Count

    inv = np.sum(inv)
    Noninv = np.sum(Noninv)

    # inv = (np.sum(i < 0))    # Inverted Pixel Count   # skipna=True,  maskna='multi',  
    # Noninv = (np.sum(i >= 0))    # Non-Inverted Pixel Count
    
    
    check = (inv + Noninv)                  # Check Statistics
    percInv = (inv /totPixels * 100)


    # Get Cell Stats
    print("Total Pixel Count", totPixels)
    print("Check - Total Pixel", check)
    print("Inverted Pixel Count", inv)
    print("Percentage Inversion", round(percInv, 3))
    

# show PMP raster and histogram 
for e in diflist:
    # show PMP raster
    show(e, cmap='terrain') #'Blues'
    # show PMP histogram
    show_hist(e, bins=50)
print("done")



# for v in diflist:
#     # Read the dataset's valid data mask as a ndarray.
#     mask = v.dataset_mask()

#     # Extract feature shapes and values from the array.
#     for geom, val in rasterio.features.shapes(
#             mask, transform=v.transform):

#             # Transform shapes from the dataset's own coordinate
#             # reference system to CRS84 (EPSG:4326).
#             geom = rasterio.warp.transform_geom(
#             v.crs, 'EPSG:4326', geom, precision=6)
            
#             # Print GeoJSON shapes to stdout.
#             # print(geom)

#             #Loop through the list of difference maps 
#             i = val
#             # Find PMP cells with value < 0 using comparison operators
#             # totPixels = int(np.sum(i))  # Total Pixel Count 
#             inv = int(np.sum(i < 0))    # Inverted Pixel Count 
#             Noninv = int(np.sum(i >= 0))    # Non-Inverted Pixel Count
#             check = (inv + Noninv)                  # Check Statistics
#             percInv = ((inv/check) * 100)


#             # Get Cell Stats
#             # print("Total Pixel Count", totPixels)
#             print("Inverted Pixel Count", inv)
#             print("Percentage Inversion", round(percInv, 3))
#             print("Check - Total Pixel", check)

