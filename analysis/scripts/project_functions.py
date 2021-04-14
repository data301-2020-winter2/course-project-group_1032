import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy import distance

def load_and_process(path_to_csv):
    
    df = (
    	pd.read_csv(path_to_csv)
    	.loc[lambda x: x['STOLEN_VALUE']>1000]
        .loc[lambda x: x['STOLEN_VALUE']<1000000]
        .drop(['ORI', 'PUB_AGENCY_NAME', 'PUB_AGENCY_UNIT', 'AGENCY_TYPE_NAME', 'STATE_ABBR', 'POPULATION_GROUP_CODE', 'OFFENSE_CODE', 'VICTIM_TYPE_CODE', 'LOCATION_CODE', 'WEAPON_CODE', 'PROP_DESC_ID', 'PROP_DESC_CODE'], axis=1)
   		.sort_values("DATA_YEAR", ascending = True)
   		.rename(columns={
   			"COUNTY_NAME" : "County_Name",
   			"POPULATION_GROUP_DESC": "Population_Description", 
   			"REGION_NAME" : "Region_Name",
   			"DATA_YEAR" : "Year",
   			"STATE_NAME" : "State",
   			"DIVISION_NAME" : "Division",
   			"COUNTY_NAME" : "County",
   			"REGION_NAME" : "Region",
   			"OFFENSE_NAME" : "Offense",
   			"OFFENDER_RACE" : "Offender_Race",
   			"OFFENDER_ETHNICITY" : "Offender_Ethnicity",
   			"OFFENDER_AGE" : "Offender_Age",
   			"OFFENDER_SEX" : "Offender_Sex",
   			"VICTIM_TYPE_NAME" : "Victim_Type",
   			"LOCATION_NAME" : "Location",
   			"WEAPON_NAME" : "Weapon",
   			"PROP_DESC_NAME" : "Property_Type",
   			"STOLEN_VALUE" : "Stolen_Value",
   			"RECOVERED_VALUE" : "Recovered_Value",
   			"RECOVERED_FLAG" : "Recovered?",
   			"DATE_RECOVERED" : "Recovery_Date"
		})
    )
    df["Latitude"] = np.nan
    df["Longitude"] = np.nan
    
    geolocator = Nominatim(user_agent="chatbot")
    coordDict = {}
    for index, row in df.iterrows():
        if row["State"] in coordDict:
            df.at[index, "Latitude"] = coordDict[row["State"]][0]
            df.at[index, "Longitude"] = coordDict[row["State"]][1]
        else:
            location = geolocator.geocode(row["State"])
            df.at[index, "Latitude"] = location.latitude
            df.at[index, "Longitude"] = location.longitude
            coordDict[row["State"]] = (location.latitude, location.longitude)

    return df
