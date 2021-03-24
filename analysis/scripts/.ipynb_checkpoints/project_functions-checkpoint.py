import pandas as pd
import numpy as np

def load_and_process(path_to_csv):
    
    df = (
    	pd.read_csv(path_to_csv)
    	.loc[lambda x: x['STOLEN_VALUE']>1000]
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
    
    
    return df
