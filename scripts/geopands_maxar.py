import geopandas as gpd
import os

# Path to your folder containing shapefiles
shapefile_directory = 'C:\\Users\\Brett\\Downloads\\Rome_Colosseum_2022-03-22_WV03_HD\\050012575010_01\\GIS_FILES'
destination_directory = 'D:\\Programming\\dumbfucks-club\\dumbfucks-club\\personal_site\\service\\static\\leaflet'

# raster command 
# gdalinfo C:\Users\Brett\Downloads\Rome_Colosseum_2022-03-22_WV03_HD\050012575010_01\050012575010_01_P001_PSH\22MAR22095810-S2AS-050012575010_01_P001.TIF
# gdal_translate -of VRT -projwin 290614.719 4641838.211 293231.619 4639626.911 C:\Users\Brett\Downloads\Rome_Colosseum_2022-03-22_WV03_HD\050012575010_01\050012575010_01_P001_PSH\22MAR22095810-S2AS-050012575010_01_P001.TIF .\static\leaflet\tempData\output.vrt
# gdal_translate -of VRT -a_srs EPSG:4326 -a_ullr 290614.719 4641838.211 293231.619 4639626.911 C:\Users\Brett\Downloads\Rome_Colosseum_2022-03-22_WV03_HD\050012575010_01\050012575010_01_P001_PSH\22MAR22095810-S2AS-050012575010_01_P001.TIF .\static\leaflet\tempData\output.vrt
# python C:\Users\Brett\anaconda3\envs\export-godot\Scripts\gdal2tiles.py -z 0-10 -p raster C:\Users\Brett\Downloads\Rome_Colosseum_2022-03-22_WV03_HD\050012575010_01\050012575010_01_P001_PSH\22MAR22095810-S2AS-050012575010_01_P001.TIF .\static\leaflet\maxarData\
# python C:\Users\Brett\anaconda3\envs\export-godot\Scripts\gdal2tiles.py .\static\leaflet\tempData\output.vrt .\static\leaflet\maxarData2\

# List all shapefiles in the directory
shapefiles = [f for f in os.listdir(shapefile_directory) if f.endswith('.shp')]

# Loop through shapefiles and convert them to GeoJSON
for shapefile in shapefiles:
    shapefile_path = os.path.join(shapefile_directory, shapefile)
    gdf = gpd.read_file(shapefile_path)
    
    # Convert to GeoJSON format and save
    geojson_file = shapefile.replace('.shp', '.geojson')
    geojson_path = os.path.join(destination_directory, geojson_file)
    print(geojson_path)
    gdf.to_file(geojson_path, driver='GeoJSON')

    print(f"Converted {shapefile} to GeoJSON.")