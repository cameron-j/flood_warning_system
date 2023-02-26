import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
from matplotlib import dates as mp_dates

def plot_water_levels(station, dates, levels):
    """Plots the water level for a given station between the given dates, with given typical levels"""
    plt.title(station.name)
    plt.plot(dates, levels)
    plt.axhline(y=station.typical_range[0], linestyle="--", color="red")
    plt.axhline(y=station.typical_range[1], linestyle="--", color="red")
    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level data along with a polynomial fit of the data of order p"""
    plt.title(station.name)
    plt.plot(dates, levels, label="Data")
    poly, d0 = polyfit(dates, levels, p)
    date_nums = np.linspace(0, mp_dates.date2num(dates[-1]) - mp_dates.date2num(d0), len(dates))
    plt.plot(dates, poly(date_nums), label="Polynomial Fit")
    plt.axhline(y=station.typical_range[0], linestyle="--", color="red")
    plt.axhline(y=station.typical_range[1], linestyle="--", color="red")
    plt.tight_layout()
    plt.legend(loc="lower right")
    plt.show()
