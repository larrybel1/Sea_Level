import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np 

def draw_plot():
    ## Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # print(df)

    ## Create scatter plot
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
    fig = plt.scatter(x = year, y = sea_level)   #, hue = df_bar['month'], color = 'rainbow')#, label = "Bar")#, = months)

    ## Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)
    sea_level_pred = slope * year + intercept
    plt.plot(year, sea_level_pred, color = "red", label = "Regression Line")

    ## Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    year_2000 = df_2000['Year']
    year_2050 = np.arange(2000, 2050, 1)
    sea_level_2050 = df_2000['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(year_2000, sea_level_2050)
    sea_level_2050_ = slope * year_2050 + intercept
    plt.plot(year_2050, sea_level_2050_, color = 'black', label = 'Predicted Sea Level')

    ## Add labels and title
    plt.legend()
    plt.xlabel("Years")
    plt.ylabel("Sea Level (Inches)")
    plt.title("Rise in Sea Levels")
    plt.show()

    
    # # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig('sea_level_plot.png')
    # return plt.gca()

    # Lets see if making a git pull works tomorrow!
    # Made some updated and opened a new py file!

draw_plot()