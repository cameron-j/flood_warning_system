import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def plot_water_levels(station, dates, levels):
    """Plots the water level for a given station between the given dates, with given typical levels"""
    dates, measure_levels = fetch_measure_levels(station, dt=dates[1] - dates[0])
    plt.plot(dates, measure_levels)
    plt.axhline(y=levels[0], linestyle="--", color="red")
    plt.axhline(y=levels[1], linestyle="--", color="red")
    plt.tight_layout()
    plt.show()
