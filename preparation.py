import logging
import fire

import collection

def clean_data(dataframe):
    dataframe.dropna(inplace=True)
    
    # Use the str.replace function to remove the dollar sign, $
    # regex=False set to remove Future Warning message
    dataframe['Close'] = dataframe['Close'].str.replace('$', '', regex=False)
    logging.debug(dataframe.head())
 
    # Convert the Close data type to a float
    dataframe['Close'] = dataframe['Close'].astype('float')
    logging.debug(dataframe.dtypes) 

    # Review the data for duplicate values, and drop them if necessary
    # Use a conditional (if statement) to determine if the number of duplicated values is non-zero.
    if dataframe.duplicated().sum() != 0:
        logging.debug(dataframe.duplicated())
        print("Duplicate values deleted.")
        dataframe.drop_duplicates(inplace=True)
    else:
        print("No duplicate values found.")
    return

def run():
    collection.run()

if __name__ == "__main__":
        logging.basicConfig(
        # filename='debug.log', 
        level=logging.DEBUG)
        fire.Fire(run)
