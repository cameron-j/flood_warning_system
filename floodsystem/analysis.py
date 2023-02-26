import numpy as np
from matplotlib.dates import date2num
from floodsystem.datafetcher import fetch_measure_levels
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    """Fits the data to a polynomial of order p"""
    d0 = dates[0]
    date_ax = [date2num(date) for date in dates]
    date_ax -= date2num(d0)
    return np.poly1d(np.polyfit(date_ax, levels, p)), d0
