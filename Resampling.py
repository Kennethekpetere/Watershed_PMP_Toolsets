
import numpy as np
import rasterio
import rasterio.features
import rasterio.warp
from rasterio.plot import show, show_hist
from rasterio.enums import Resampling

upscale_factor = 371 #(11132+1/30) # Upscaling from 11132m to 30m => matrix {371 by 371}

# Open PMP raster 
pmp30m = "./ResampledPMP/PMP30mKs.tif"; pmp1h = "./ResampledPMP/PMP1hKs.tif"; pmp2h = "./ResampledPMP/PMP2hKs.tif"
pmp3h = "./ResampledPMP/PMP3hKs.tif"; pmp6h = "./ResampledPMP/PMP6hKs.tif"; pmp12h = "./ResampledPMP/PMP12hKs.tif"
pmp24h = "./ResampledPMP/PMP24hKs.tif"; pmp2d = "./ResampledPMP/PMP2DKs.tif"; pmp3d = "./ResampledPMP/PMP3DKs.tif"

# Set images into a list
PMP_Image_List = [pmp30m, pmp1h, pmp2h, pmp3h, pmp6h, pmp12h, pmp24h, pmp2d, pmp3d]
exp = ["RS30mPMP_rio.tif", "RS1hPMP_rio.tif", "RS2hPMP_rio.tif", "RS3hPMP_rio.tif", 
      "RS6hPMP_rio.tif", "RS12hPMP_rio.tif", "RS24hPMP_rio.tif", "RS2DPMP_rio.tif", "RS3DPMP_rio.tif"]

# for i in PMP_Image_List:
#     with rasterio.open(i) as dataset:
        
#         # resample data to target shape
#         print("Start Resampling")
#         data = dataset.read(
#             out_shape=(
#                 dataset.count,
#                 int(dataset.height * upscale_factor),
#                 int(dataset.width * upscale_factor)
#             ),
#             resampling=Resampling.bilinear  # Other sampling techniques (bilinear, nearest, cubic, average)
#         )

#         # scale image transform
#         transform = dataset.transform * dataset.transform.scale(
#             (dataset.width / data.shape[-1]),
#             (dataset.height / data.shape[-2])
#         )
#         transform.save("./ResampledPMP/"+ exp.tif, overwrite=True) # n_workers=4,
# print("Done")


with rasterio.open(pmp30m) as dataset:

    # resample data to target shape
    print("Start Resampling")
    data = dataset.read(
        out_shape=(
            dataset.count,
            int(dataset.height * upscale_factor),
            int(dataset.width * upscale_factor)
        ),
        resampling=Resampling.bilinear  # Other sampling techniques (bilinear, nearest, cubic, average)
    )

    # scale image transform
    transform = dataset.transform * dataset.transform.scale(
        (dataset.width / data.shape[-1]),
        (dataset.height / data.shape[-2])
    )
    dataset.write("./ResampledPMP/RS30mPMP_rio.tif", overwrite=True) # n_workers=4,
    dataset.close()
print("Done")