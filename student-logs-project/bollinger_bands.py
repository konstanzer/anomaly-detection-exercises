import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def compute_pct_b(pages, span, weight):
    """
    Compute anomalies based on percentage-b
    1 is on upper band, -1 is on lower band 
    """
    midband = pages.ewm(span=span).mean()
    stdev = pages.ewm(span=span).std()
    ub = midband + stdev*weight
    lb = midband - stdev*weight
    bb = pd.concat([ub, lb], axis=1)
    my_df = pd.concat([pages, midband, bb], axis=1)
    my_df.columns = ['pages', 'midband', 'ub', 'lb']
    my_df['pct_b'] = (my_df['pages'] - my_df['lb'])/(my_df['ub'] - my_df['lb'])
    
    return my_df


def plt_bands(my_df):
    """
    Plot Bollinger bands
    """
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(my_df.index, my_df.pages, label='Number of Pages')
    ax.plot(my_df.index, my_df.midband, label = 'EMA/midband')
    ax.plot(my_df.index, my_df.ub, label = 'Upper Band')
    ax.plot(my_df.index, my_df.lb, label = 'Lower Band')
    ax.legend(loc='best')
    ax.set_ylabel('Number of Pages')
    plt.show()

            
def find_anomalies(pages, span, weight):
    """
    Dataframe of days where percent-b is above 1 (top band)
    """
    my_df = compute_pct_b(pages, span, weight)
    plt_bands(my_df)
            
    return my_df[my_df.pct_b>1]
