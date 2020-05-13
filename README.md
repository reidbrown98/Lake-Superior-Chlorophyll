# Lake Superior Chlorophyll

This is an exploratory data analysis of the Chlorophyll-a content of Lake Superior. In this repo I included the cleaned dataset, the html of the EDA, the Python scripts showing how I exported this data, and my write-up communicating my findings. I plan on publishing the dataset for others to analyze. 

The data was sourced from NASA's MODIS-Aqua satallite. I chose the mapped data, got 4km pixel resolution, and selected the chlor_a band. The link to the download site is found below. The data downloads as netCDF files that can be opened in ESRI's ArcMap. From here I used my python scripts to turn the netCDF data into Raster data, and then I calculated the zonal statistics on the new raster file. From here I ran the script on all of the netCDF files from July 2002 until March 2020. After calculating the zonal statistics of all the new raster files I exported all of them from .gdb files to .csv files where I then uploaded them into R for analysis. 


[Link to Data Source](https://oceandata.sci.gsfc.nasa.gov/MODIS-Aqua/Mapped/Monthly/4km/chlor_a/)
[Link to Lake Superior EDA](https://reidbrown98.github.io/Lake-Superior-Chlorophyll/Lake-Superior-Data-Analysis.html)
