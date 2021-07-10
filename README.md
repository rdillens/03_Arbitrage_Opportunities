# Arbitrage_Opportunities
Analyze Bitcoin historical data from Bitstamp and Coinbase to find potential arbitrage opportunities.

---
## Technologies
Code is written using Python version 3.7 and runs a Jupyter Lab notebook. The following libraries are required to run the app:
 ```python
import pandas as pd
from pathlib import Path

%matplotlib inline
```

---
## Installation Guide
Using the command prompt, navigate to an empty folder where you would like to install the files and type the command:
```
git clone https://github.com/rdillens/03_Arbitrage_Opportunities.git
```
Then, to run the app type:
```
cd 03_Arbitrage_Opportunities
jupyter lab
```
**Note: You must install Jupyter Lab in your Conda environment in order to run this program.**

See the [Jupyter Lab Installation Guide](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) for more information.

---
## Examples
 ![cumsum](/Images/cumsum.png)
---
## Usage
This program anaylzes historical data for Bitcoin trading prices from January 01, 2018 to March 31, 2018 on two trading platforms, Bitstamp and Coinbase. The program will determine the value of any arbitrage opportunities that exist on three different dates chosen from the dataset. The data is analyzed and graphed to show the prices and also plot the cumulative sum of arbitrage profits is plotted.
---
## Contributors
Starter code was given in the Module 3 Challenge in the Rice FinTech Bootcamp and all modifications were made by Remy Dillenseger. 

---
## License
This project is not licensed for use by anyone other than the author, Remy Dillenseger, and the faculty/staff of Rice FinTech Bootcamp for the purpose of the course.