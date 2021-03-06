#The purpose of this exercise is to demonstrate how I solved a problem
#After graphing industries vs stock price for companies in the S&P 500, I wanted to subcategorize the industries by price ranges
#In this excersize, I split up the data into groups, I add information to identify the data groups, and then I recombine the groups.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("constituents-financials_csv.csv")

Sectors = ["Information Technology","Utilities", "Industrials", "Energy" , "Real Estate",
  "Consumer Staples",   "Telecommunication Services", "Materials", "Financials", 
  "Consumer Staples", "Consumer Discretionary"]


#Here's how I seperated the groups. I had to use .loc to permenatly make changes to the dataframe; without it, pandas would 
#make a copy and the program wouldn't function.
less_than_50 = df.loc[df['Price'] < 50]
between_50_and_100 = df.loc[(df['Price'] >=50) & (df['Price'] < 100)]
between_100_and_500 = df.loc[(df.Price >= 100) & (df.Price < 500)]
greater_than_500 = df.loc[df.Price > 500]

#Here's where I added a characteristic to help me distinguish these groups. I knew I wanted to use the "hue" function in seaborn, 
#so this seemed like the best way to let me use that function appropriately.
less_than_50.loc[:,"Price_Range"] = "Less than 50" 
between_50_and_100.loc[:,"Price_Range"] = "Between 50 and 100"
between_100_and_500.loc[:,"Price_Range"]  = "Between 100 and 500"
greater_than_500.loc[:,"Price_Range"]  = "Greater than 500"

#Here's where I recombine the dataframes.
frames = [less_than_50, between_50_and_100, between_100_and_500, greater_than_500]
result = pd.concat(frames)

#Here's where I plot my figure and adjust the styling 
fig = plt.figure(figsize = (30,20))
ax = sns.barplot(data = result, x = "Sector", y = "Price", estimator = len, hue = "Price_Range")
plt.ylabel("Number of Companies", fontsize = 35)
ax.set_xticklabels(Sectors, rotation = 30, fontsize = 20)
plt.title("S&P 500 Companies by Sector, Price per Share Range, and Quantity", fontsize = 40)

plt.savefig("Price_range.png")



       
