import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  sea=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  plt.scatter(sea['Year'],sea['CSIRO Adjusted Sea Level'],color='red')
  plt.xlabel('Year')
  plt.ylabel('CSIRO Adjusted Sea Level')
  plt.title("Year vs CSIRO Adjusted Sea Level")

    # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = stats.linregress(sea['Year'], sea['CSIRO Adjusted Sea Level'])
  plt.scatter(sea['Year'],sea['CSIRO Adjusted Sea Level'],color='red',label='data')

  newyear1=np.arange(1880,2050,1)
  fit1=np.polyfit(sea['Year'],sea['CSIRO Adjusted Sea Level'],1)
  v1=np.polyval(fit1,newyear1)
  plt.plot(newyear1,v1,color='black',label='best fit')
  plt.xlabel('Year')
  plt.ylabel('CSIRO Adjusted Sea Level')
  plt.title("Year vs CSIRO Adjusted Sea Level with best fit line")
  plt.legend()
    # Create second line of best fit
  x=sea.loc[sea['Year']>=2000,'Year']
  y=sea.loc[sea['Year']>=2000,'CSIRO Adjusted Sea Level']
  plt.scatter(sea['Year'],sea['CSIRO Adjusted Sea Level'],color='red',label='data')
  newyear1=np.arange(1880,2050,1)
  fit1=np.polyfit(sea['Year'],sea['CSIRO Adjusted Sea Level'],1)
  v1=np.polyval(fit1,newyear1)
  plt.plot(newyear1,v1,color='black',label='best fit')
  newyear=np.arange(2000,2050,1)
  fit=np.polyfit(x,y,1)
  v=np.polyval(fit,newyear)
  plt.plot(newyear,v,label='best fit 2')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title("Rise in Sea Level")
  plt.legend()  


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()