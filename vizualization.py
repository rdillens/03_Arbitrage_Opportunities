import matplotlib.pyplot as plt

plot_height = 4
plot_width = 20

def main_plotter(
    df, 
    range_slider, 
    date_slicer, 
    bitstamp_checkbox, 
    coinbase_checkbox, 
    ):

    """
    A helper function to make a graph.
    """
    fig, ax = plt.subplots(figsize=(plot_width, plot_height))
    ax.axis(
        xmin=df.index[date_slicer[0]],
        xmax=df.index[date_slicer[1]],
        ymin=range_slider[0], 
        ymax=range_slider[1],
        )
    if bitstamp_checkbox is True:
        ax.plot(df.index, df['Bitstamp'], label="Bitstamp")

    if coinbase_checkbox is True:
        ax.plot(df.index, df['Coinbase'], label="Coinbase")
    ax.set_xlabel("Date/Time")
    ax.set_ylabel("Close Price")

    if bitstamp_checkbox or coinbase_checkbox:
        ax.legend()
    ax.set_title("Arbitrage")

def day_plotter(df, date_picker):
    fig, ax = plt.subplots(figsize=(int(round(plot_width/2, 0)), plot_height-1))
    ax.axis(
        xmin=df.index[date_picker-720],
        xmax=df.index[date_picker+720],
        ymin=.9*min(df['Bitstamp'][date_picker-720:date_picker+720]), 
        ymax=1.1*max(df['Bitstamp'][date_picker-720:date_picker+720]), 
        )
    ax.plot(df.index, df['Bitstamp'], label="Bitstamp")
    ax.plot(df.index, df['Coinbase'], label="Coinbase")
    ax.set_xlabel("Date/Time")
    ax.set_ylabel("Close Price")
    ax.legend()
    ax.set_title("Arbitrage")

def arbitrage_summary(arbitrage_spread):
    fig, ax = plt.subplots(figsize=(int(round(plot_width/2, 0)), plot_height-1))
    ax.boxplot(arbitrage_spread)
    ax.set_title("Arbitrage Summary")
