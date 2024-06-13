# %%
import requests

# import geopandas as gpd
import pandas as pd
import seaborn as sns
import json

# from shapely.geometr*y import Polygon, MultiPolygon, shape
# from geopandas.tools import sjoin

# %%

# Haetaan tiedot API:lta

params_postcodes = {
    "SERVICE": "WFS",
    "VERSION": "1.0.0",
    "REQUEST": "GetFeature",
    "TYPENAME": "postialue:pno_2023",
    "OUTPUTFORMAT": "json",
}

postal_codes = requests.get(
    url="http://geo.stat.fi/geoserver/postialue/wfs", params=params_postcodes
)

response = postal_codes.json()

print(response["features"])

postal_codes_df = pd.DataFrame()

for feature in response["features"]:
    postal_codes_df = postal_codes_df.append(
        {
            "postal_code": feature["properties"]["posti_alue"],
            "name": feature["properties"]["nimi"],
            "geometry": feature["geometry"],
        },
        ignore_index=True,
    )

# %%

print(postal_codes_df.head(10))
postal_codes_df
# print(postal_codes_df.loc[3]["geometry"])

# Alla oleva funktio on turha
# def convert_coordinates(geometry_dict):
#     if geometry_dict['type'] == 'Polygon':
#         return Polygon(*geometry_dict['coordinates'])
#     elif geometry_dict['type'] == 'MultiPolygon':
#         return MultiPolygon([Polygon(*coords) for coords in geometry_dict['coordinates']])
#     else:
#         return None


# %%

# Muutetaan GeoDataFrameksi

gdf = gpd.GeoDataFrame(postal_codes_df)

# gdf["geometry"] = gdf["geometry"].apply(convert_coordinates)
gdf["geometry"] = gdf["geometry"].apply(shape)

gdf = gdf.set_crs("EPSG:3067")

gdf = gdf.to_crs("EPSG:4326")

gdf.head()


# %%
