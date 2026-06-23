import numpy as np
import pandas as pd

# sns.set()

ds = pd.read_csv("carbon_emission_record.csv")
india = ds.where(ds['country']=='india')
indian_ds = india[['country','year','co2','co2_per_capita','cumulative_co2','share_global_co2','share_global_cumulative_co2','co2_growth_prct','consumption_co2','trade_co2','total_ghg']]

