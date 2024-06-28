Lewisham boundaries
==============================

The assets to be mapped are found in `static_assets` folder, where there are three sub-folders: `epsg_27700`, `epsg_3857`, and `epsg_4326`. Inside these folders, you can find the assets projected to EPSG:27700, EPSG:3857, and EPSG:4326 coordinate reference system. EPSG:27700 and EPSG:3857 are the two CRSs that are compatible with the Ordnance Survey (OS) APIs. OS APIs default to EPSG:27700, but can also support EPSG:3857. The information contained in the assets is the same, whichever projection is chosen.

Each of the projection folders contains three other folders: `council boundary`, `lsoa boundaries`, and `ward boundaries`. Inside `council boundary` and `ward boundaries` directories, we have further split the data to geojson and shapefile folders. The `.geojson` and `.shp` files inside `council boundary` folder represent Lewisham Council as a polygon. The `.geojson` and `.shp` files inside `ward boundaries` folder are the 2022 ward level boundaries for Lewisham.

Please note that the boundaries in the folders are the most up-to-date boundaries and are subject to changes. We use `(BFC) Full resolution - clipped to coastline` boundaries.
 

Folder Organization
------------

    ├── README.md                               <- The top-level README for developers using this project.
    ├── .gitignore                              <- NEVER DELETE THIS FILE.
    ├── clean_dataset.py                        <- Compilation and reformatting of data to create data files in /data/processed/
    ├── data
    │   ├── downloaded                          <- Data from downloads.
    │   ├── interim                             <- Intermediate data that has been transformed.
    │   ├── processed                           <- The final, canonical data sets for modeling.
    │   └── raw                                 <- The original, immutable data dump.
    │
    └── static_assets
        ├── epsg_3857                           <- EPSG:3857 projections under this folder.
        │     ├── council boundary              <- Council boundary polygons.
        │     │    ├── geojson                  <- Lewisham boundary as a geojson.
        │     │    └── shapefile                <- Lewisham boundary as a shapefile.
        │     │
        │     ├── msoa boundaries               <- MSOA boundary polygons.
        │     │    ├── geojson                  <- MSOA boundaries as a geojson.
        │     │    └── shapefile                <- MSOA boundaries as a shapefile.
        │     │
        │     ├── msoa 2011 boundaries          <- MSOA 2011 boundary polygons.
        │     │    ├── geojson                  <- MSOA 2011 boundaries as a geojson.
        │     │    └── shapefile                <- MSOA 2011 boundaries as a shapefile.
        │     │
        │     ├── lsoa boundaries               <- LSOA boundary polygons.
        │     │    ├── geojson                  <- LSOA boundaries as a geojson.
        │     │    └── shapefile                <- LSOA boundaries as a shapefile.
        │     │
        │     ├── lsoa 2011 boundaries          <- LSOA 2011 boundary polygons.
        │     │    ├── geojson                  <- LSOA 2011 boundaries as a geojson.
        │     │    └── shapefile                <- LSOA 2011 boundaries as a shapefile.
        │     │
        │     ├── oa boundaries                 <- OA boundary polygons.
        │     │    ├── geojson                  <- OA boundaries as a geojson.
        │     │    └── shapefile                <- OA boundaries as a shapefile.
        │     │
        │     ├── oa 2011 boundaries            <- OA 2011 boundary polygons.
        │     │    ├── geojson                  <- OA 2011boundaries as a geojson.
        │     │    └── shapefile                <- OA 2011 boundaries as a shapefile.
        │     │
        │     └── ward boundaries               <- Ward boundary polygons.
        │            ├── geojsons               <- Ward boundaries as geojsons.
        │            └── shapefiles             <- Ward boundaries as shapefiles.
        │
        ├── epsg_4326                           <- As above, but for EPSG:4326 projection.
        │   └──
        └── epsg_27700                          <- As above, but for EPSG:27700 projection.   
            └──
    


	
