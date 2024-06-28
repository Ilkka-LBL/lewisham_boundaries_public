#%%
from pathlib import Path
import geopandas as gpd
from LBLWebAssets.create_static_assets import CreateAssets
import os
import pandas as pd

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

raw = Path('data/raw')
static_asset_path = Path('static_assets')

#%%
lbl_boundaries = raw.joinpath('lbl_wd22_full_shp/lbl_wd22_full.shp')
gdf = gpd.read_file(lbl_boundaries)
#%%
print(gdf)
lbl = gdf.dissolve(by='LAD22NM')                                                     
print(lbl)
#%%
lbl.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(lbl)
asset.output_static_files(Path('council boundary/geojson/lewisham.geojson'), bypass=True)
asset.output_static_files(Path('council boundary/shapefile/lewisham.shp'))
asset.output_static_files(Path('council boundary/json/lewisham.json'), bypass=True)

# %%
wards = []
for ward in list(gdf['WD22NM'].unique()):
    ward_poly = gdf[gdf['WD22NM'] == ward]
    ward_poly = ward_poly.dissolve(by='WD22NM')
    wards.append(ward_poly)

ward_geo = pd.concat(wards)
ward_geo = gpd.GeoDataFrame(ward_geo, geometry='geometry')
ward_geo.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(ward_geo)
asset.output_static_files(Path(f'ward boundaries/geojsons/wards_2022.geojson'), bypass=True)
asset.output_static_files(Path(f'ward boundaries/shapefiles/wards_2022.shp'))
asset.output_static_files(Path(f'ward boundaries/json/wards_2022.json'))

# %%


lbl_lsoas = raw.joinpath('Lewisham LSOAs/lsoas.shp')
lsoas_gdf = gpd.read_file(lbl_lsoas)
lsoa_poly = lsoas_gdf.dissolve(by='LSOA21NM')

#%%
print(lsoa_poly.crs)
print(lsoa_poly)
lsoa_poly.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(lsoa_poly)

asset.output_static_files(Path(f'lsoa boundaries/geojsons/lsoas.geojson'), bypass=True)

asset.output_static_files(Path(f'lsoa boundaries/shapefiles/lsoas.shp'))
asset.output_static_files(Path(f'lsoa boundaries/json/lsoas.json'))


# %%

lbl_oas = raw.joinpath('Lewisham OAs/lewisham oas.shp')
oas_gdf = gpd.read_file(lbl_oas)
oa_poly = oas_gdf.dissolve(by='OA21CD')

#%%
print(oa_poly.crs)
print(oa_poly)
oa_poly.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(oa_poly)

asset.output_static_files(Path(f'oa boundaries/geojsons/oas.geojson'), bypass=True)

asset.output_static_files(Path(f'oa boundaries/shapefiles/oas.shp'))
asset.output_static_files(Path(f'oa boundaries/json/oas.json'))

# %%

lbl_oas = raw.joinpath('Lewisham 2011 OAs/OA 2011.shp')
oas_gdf = gpd.read_file(lbl_oas)
oa_poly = oas_gdf.dissolve(by='OA11CD')
oa_poly.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(oa_poly)

asset.output_static_files(Path(f'oa 2011 boundaries/geojsons/oas.geojson'), bypass=True)

asset.output_static_files(Path(f'oa 2011 boundaries/shapefiles/oas.shp'))
asset.output_static_files(Path(f'oa 2011 boundaries/json/oas.json'))

# %%


lbl_lsoas = raw.joinpath('Lewisham 2011 LSOAs/lsoa 2011.shp')
lsoas_gdf = gpd.read_file(lbl_lsoas)
lsoa_poly = lsoas_gdf.dissolve(by='LSOA11NM')

#%%
print(lsoa_poly.crs)
print(lsoa_poly)
lsoa_poly.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(lsoa_poly)

asset.output_static_files(Path(f'lsoa 2011 boundaries/geojsons/lsoas.geojson'), bypass=True)

asset.output_static_files(Path(f'lsoa 2011 boundaries/shapefiles/lsoas.shp'))
asset.output_static_files(Path(f'lsoa 2011 boundaries/json/lsoas.json'))

# %%

lbl_msoas_2011 = raw.joinpath('Lewisham 2011 MSOAs/MSOA_2011_EW_BFC_V3.shp')
msoas__2011_gdf = gpd.read_file(lbl_msoas_2011)
msoa_poly_2011 = msoas__2011_gdf.dissolve(by='MSOA11NM')

#%%
print(msoa_poly_2011.crs)
print(msoa_poly_2011)
msoa_poly_2011.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(msoa_poly_2011)

asset.output_static_files(Path(f'msoa 2011 boundaries/geojsons/msoas.geojson'), bypass=True)

asset.output_static_files(Path(f'msoa 2011 boundaries/shapefiles/msoas.shp'))

asset.output_static_files(Path(f'msoa 2011 boundaries/json/msoas.json'))

# %%
lbl_msoas = raw.joinpath('Lewisham MSOAs/MSOA_2021_EW_BFC_V6.shp')
msoas_gdf = gpd.read_file(lbl_msoas)
msoa_poly = msoas_gdf.dissolve(by='MSOA21NM')

#%%
print(msoa_poly.crs)
print(msoa_poly)
msoa_poly.reset_index(inplace=True)
asset = CreateAssets(static_asset_path=static_asset_path)
asset.assets_from_geopandas(msoa_poly)

asset.output_static_files(Path(f'msoa boundaries/geojsons/msoas.geojson'), bypass=True)

asset.output_static_files(Path(f'msoa boundaries/json/msoas.json'))

#%%
