import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Load in data from .csv files only using the 10 most recent years of data, 120 for monthly 40 for quarterly
    federal_funds_df = pd.read_csv("data/FEDFUNDS.csv").tail(120)
    CPI_df = pd.read_csv("data/CPIAUCSL.csv").tail(120)
    unemployment_df = pd.read_csv("data/UNRATE.csv").tail(120)
    real_GDP_df = pd.read_csv("data/GDPC1.csv").tail(40)

    # Initialize the plot figure
    plt.figure(figsize=(4, 1))
    plt.suptitle("U.S. Economic Indicators")
    
    # Effective Federal Funds Rate Plot
    plt.subplot(141)
    plt.plot(federal_funds_df.DATE, federal_funds_df.FEDFUNDS, label="Federal Funds Rate")
    plt.legend(loc='best')

    # Consumer Price Index Plot
    plt.subplot(142)
    plt.plot(CPI_df.DATE, CPI_df.CPIAUCSL, label="Consumer Price Index")
    plt.legend(loc='best')

    # Civilian Unemployment Rate Plot
    plt.subplot(143)
    plt.plot(unemployment_df.DATE, unemployment_df.UNRATE, label="Unemployment Rate")
    plt.legend(loc='best')

    # Real Gross Domestic Product Plot
    plt.subplot(144)
    plt.plot(real_GDP_df.DATE, real_GDP_df.GDPC1, label="Real GDP")
    plt.legend(loc='best')
    
    # Show plots fullscreen
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()