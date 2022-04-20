import pandas as pd
from pathlib import Path

import logging
import fire

# Read in the CSV file called "bitstamp.csv" using the Path module. 
# The CSV file is located in the Resources folder.
# Set the index to the column "Date"
# Set the parse_dates and infer_datetime_format parameters

class Data_Container:
    def __init__(self, csvpath=None):
        self.df = None
        self.sliced = None
        self.csvpath = csvpath

        if self.csvpath is not None:
            self.init_data_container()
    
    def init_data_container(self, csvpath=None):
        if csvpath is None:
            csvpath = self.csvpath
        self.df = self.read_csv(csvpath)
        self.clean_data()
        self.slice_data()

    def read_csv(self, csvpath):
        # Set the index to the column "Timestamp"
        # Set the parse_dates and infer_datetime_format parameters
        return pd.read_csv(csvpath, index_col="Timestamp", parse_dates=True, infer_datetime_format=True)

    def clean_data(self):
        self.df.dropna(inplace=True)
        self.df['Close'] = self.df['Close'].str.replace('$', '', regex=False).astype('float')
        logging.debug(self.df.head())
        # Use a conditional (if statement) to determine if the number of duplicated values is non-zero.
        if self.df.duplicated().sum() != 0:
            logging.debug(self.df.duplicated())
            logging.info("Duplicate values deleted.")
            self.df.drop_duplicates(inplace=True)
        else:
            logging.info("No duplicate values found.")

    def slice_data(self):
        # Use loc or iloc to select `Timestamp (the index)` and `Close` from bitstamp DataFrame
        self.sliced = self.df.loc[:, 'Close']

        # Review the first five rows of the DataFrame
        logging.debug(self.sliced.head())


def run():
    bitstamp = Data_Container()
    bitstamp.df = bitstamp.read_csv(Path("Resources/bitstamp.csv"))
    # Use the head function to confirm that the data was imported properly.
    logging.debug(bitstamp.df.head())

    coinbase = Data_Container()
    coinbase.df =  coinbase.read_csv(Path("Resources/coinbase.csv"))
    # Use the head function to confirm that the data was imported properly.
    logging.debug(coinbase.csv.head())

    bitstamp.clean_data()
    coinbase.clean_data()

    # bitstamp_sliced = bitstamp.slice_data()
    # coinbase_sliced = coinbase.slice_data()

    return

if __name__ == "__main__":
        logging.basicConfig(
        # filename='debug.log', 
        level=logging.DEBUG)
        fire.Fire(run)
