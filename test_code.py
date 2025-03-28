import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np 


# Read data from file
df = pd.read_csv("epa-sea-level.csv")
# print(df)

# Create scatter plot
year = df['Year']
sea_level = df['CSIRO Adjusted Sea Level']

# Create second line of best fit
sea_level_2000 = pd.concat([year , sea_level], axis = 1)    # sea_level_2000.set_index('Year', inplace = True)

    # Create second line of best fit
df_2000 = df[df['Year'] >= 2000]

lineB = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
xB = np.arange(2000,2050,1)
yB = xB*lineB.slope + lineB.intercept



    # year_2000 = sea_level_2000['Year']
    # year_2000 = year_2000[120:]
    # print(year_2000)
    # sealevel_2000 = sea_level_2000['CSIRO Adjusted Sea Level']

sealevel_2000 = sea_level_2000[120:]
year_2000 = sealevel_2000['Year']
sealevel2000_ = sealevel_2000['CSIRO Adjusted Sea Level']

slope, intercept, r_value, p_value, std_err = linregress(year_2000, sealevel2000_)

sealevelpred_2000 = slope * year_2000 + intercept

plt.plot(year_2000, sealevelpred_2000, color = 'orange', label = 'Predictive Regression Line')

