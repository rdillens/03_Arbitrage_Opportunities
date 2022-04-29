import matplotlib.pyplot as plt

plot_height = 3
plot_width = 12

# def main_plotter(x1, y1, x2, y2, date_picker_slider, range_slider, date_slicer, bitstamp_checkbox, coinbase_checkbox, scale):
#     """
#     A helper function to make a graph.
#     """
#     fig, ax = plt.subplots(figsize=(16,5))
#     ax.axis(
#         xmin=x1[date_slicer[0]],
#         xmax=x1[date_slicer[1]],
#         ymin=range_slider[0], 
#         ymax=range_slider[1],
#         )
#     # date_picker.min = date_slicer[0]
#     # date_picker.max = date_slicer[1]
#     if bitstamp_checkbox is True:
#         ax.plot(x1, y1, label="Bitstamp")

#     if coinbase_checkbox is True:
#         ax.plot(x2, y2, label="Coinbase")
#     ax.set_xlabel("Date/Time")
#     ax.set_ylabel("Close Price")

#     if bitstamp_checkbox or coinbase_checkbox:
#         ax.legend()
#     ax.set_title("Arbitrage")

#     ax.vlines(x1[date_picker_slider-1], scale[0], scale[1], colors="Red")
#     # date_picked.value = f"{x1[date_picker_slider-1]}"

def main_plotter(
    df, 
    # date_picker_slider, 
    range_slider, 
    date_slicer, 
    bitstamp_checkbox, 
    coinbase_checkbox, 
    # scale
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
    # date_picker.min = date_slicer[0]
    # date_picker.max = date_slicer[1]
    if bitstamp_checkbox is True:
        ax.plot(df.index, df['Bitstamp'], label="Bitstamp")

    if coinbase_checkbox is True:
        ax.plot(df.index, df['Coinbase'], label="Coinbase")
    ax.set_xlabel("Date/Time")
    ax.set_ylabel("Close Price")

    if bitstamp_checkbox or coinbase_checkbox:
        ax.legend()
    ax.set_title("Arbitrage")

    # ax.vlines(df.index[date_picker_slider-1], scale[0], scale[1], colors="Red")
    # date_picked.value = f"{df.index[date_picker_slider-1]}"

# def day_plotter(x1, y1, x2, y2, date_picker):
#     fig, ax = plt.subplots(figsize=(8,4))
#     ax.axis(
#         xmin=x1[date_picker-720],
#         xmax=x1[date_picker+720],
#         ymin=.9*min(y1[date_picker-720:date_picker+720]), 
#         ymax=1.1*max(y1[date_picker-720:date_picker+720]), 
#         )
#     ax.plot(x1, y1, label="Bitstamp")
#     ax.plot(x2, y2, label="Coinbase")
#     ax.set_xlabel("Date/Time")
#     ax.set_ylabel("Close Price")
#     ax.legend()
#     ax.set_title("Arbitrage")

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
