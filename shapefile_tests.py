# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 07:45 2023

@author: rathk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs

# Usage example
shapefile_path = 'C:/Users/rathk/OneDrive/Desktop/Sample/counties/counties.shp'
shapefile_path1 = 'C:/Users/rathk/OneDrive/Desktop/Sample/baronies/baronies.shp'
shapefile_path2 = 'C:/Users/rathk/OneDrive/Desktop/Sample/civil_parishes/civil_parishes.shp'
shapefile_path3 = 'C:/Users/rathk/OneDrive/Desktop/Sample/eds/eds.shp'
shapefile_path4 = 'C:/Users/rathk/OneDrive/Desktop/Sample/Local_Electoral_Areas/Local_Electoral_Areas.shp'
shapefile_path5 = 'C:/Users/rathk/OneDrive/Desktop/Sample/provinces/provinces.shp'
shapefile_path6 = 'C:/Users/rathk/OneDrive/Desktop/Sample/townlands/townlands.shp'

### ----- RUN SHAPEFILE FILES TO UNDERSTAND THE VISUALISATION OF EACH FILE -----

# Create a heatmap
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')  # Equal aspect ratio
# Read the shapefile
gdf = gpd.read_file(shapefile_path1)
# Plot the shapefile
gdf.plot(ax=ax, color='white', edgecolor='black')

# Create a heatmap
fig1, ax1 = plt.subplots(figsize=(10, 10))
ax1.set_aspect('equal')  # Equal aspect ratio
# Read the shapefile
gdf1 = gpd.read_file(shapefile_path1)
# Plot the shapefile
gdf1.plot(ax1=ax1, color='white', edgecolor='black')


