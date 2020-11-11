import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pagedfs.txt', parse_dates=True,index_col=['date'])

# Clean data
a=round(len(df)*2.5/100)
b=(df.drop(df.value[:a].index)) 
b=(df.drop(df.value[-a:].index))


def draw_line_plot():
  fig,ax = plt.subplots(figsize=(10,5))
  ax.plot(b.index,b['value'])
  plt.title('Daily freeCodeCamp Forum Page dfs 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page views')
    





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df.reset_index(inplace=True)

    # Draw bar plot
    df_bar = df.groupby([df['date'].dt.year.rename('Years'),
               df['date'].dt.month.rename('Months')]).agg('mean')['value'].unstack()
    fig, ax = plt.subplots(figsize=(12,8))
    df_bar.plot(kind='bar', ax=ax)




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(10,5))

    plt.ylim(10000,180000)
    plt.title("Year-Wise Box Plot (Trend)")
    plt.xlabel('Year')
    plt.ylabel('Page dfs')

    sns.boxplot(x='year',y='value', data=df_box, ax=ax[0])
    plt.ylim(10000,180000)
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel('Month')
    plt.ylabel('Page dfs')
    sns.boxplot(x='month',y='value', data=df_box, ax=ax[1])    





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
