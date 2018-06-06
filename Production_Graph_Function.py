#Function that takes production information from a state and the state's name,
#and outputs a graph of production 
from matplotlib import pyplot as plt

x_axis_ticks = ["07'", "08'", "09'", "10'", "11'", "12'", "13'", "14'", "15'", "16'", "17'"]
years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
texas_production = [391261, 406019, 399380, 426725, 529347, 723952, 924734, 1155449, 1258678, 1176041, 1282692]
louisiana_production = [76978,	72347,	68823, 67274,	68959,	70588,	71934,	68750,	62935,	56432,	50036]
north_dakota_production = [44788, 62348, 79339, 112530, 152398, 242330, 312350, 394655, 429497,	377968, 388305]
colorado_production = [26183, 29949, 30361, 32996, 39456,	49596,	66086,	95475,	122622, 115897, 128387]
def production_plot_maker(state_production, state_name):
    ax = plt.subplot()
    plt.plot(years, state_production) 
    plt.title(state_name)
    plt.xlabel("Year")
    plt.ylabel("1000 BBL Produced")
    plt.legend([state_name], loc = (0))
    ax.set_xticks(years)
    ax.set_xticklabels(x_axis_ticks)
    plt.show()

production_plot_maker(texas_production, "Texas")

production_plot_maker(louisiana_production, "Louisiana")


production_plot_maker(colorado_production, "Colorado")

