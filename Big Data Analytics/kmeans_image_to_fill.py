# Import necessary libraries
from copy import deepcopy
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt
import rasterio as rio

# read a rasterio image
src=rio.open('S2image.tif')
im=src.read()
# be careful with the shape
im.shape
nb_bands,size_x,size_y=im.shape
# put data between 0 and 1
# visualize and save bands
for i in range(nb_bands):
 # ...

# create a data matrix -> reshape data such as
#  data is of dimensions (size_x x size_y , nb_bands)
data=np.zeros((size_x*size_y,nb_bands))
for i in range(nb_bands):
    # ...
# verify data are correct
for i in range(nb_bands):
    print('band %.2d : min - max = [%.4f,%.4f]'%(i,np.min(data[:,i]),np.max(data[:,i])))



# perform k means
clusters = # ...

# rescale clustering
im_clusters=clusters.reshape((size_x,size_y))

# Plot the clustering
plt.clf()
plt.imshow(im_clusters)
plt.title('result_clustering')
plt.savefig('clustering_sentinel.png')
