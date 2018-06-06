#Plotting production information from severl different states from 2008 - 2017
source: https://www.eia.gov/dnav/pet/pet_crd_crpdn_adc_mbbl_a.htm

from matplotlib import pyplot as plt

x_axis_ticks = ["07'", "08'", "09'", "10'", "11'", "12'", "13'", "14'", "15'", "16'", "17'"]

texas_production = [391261, 406019, 399380, 426725, 529347, 723952, 924734, 1155449, 1258678, 1176041, 1282692]
louisiana_production = [76978,	72347,	68823, 67274,	68959,	70588,	71934,	68750,	62935,	56432,	50036]
north_dakota_production = [44788, 62348, 79339, 112530, 152398, 242330, 312350, 394655, 429497,	377968, 388305]
colorado_production = [26183, 29949, 30361, 32996, 39456,	49596,	66086,	95475,	122622, 115897, 128387]
year1 = list(range(len(texas_production)))


f = plt.figure(figsize = (7.5,3.5))
ax = plt.subplot(2,2,1) 
plt.plot(year1, texas_production)
plt.title("Texas Production")
plt.xlabel("Year")
plt.ylabel("1000 BBL Produced")
plt.legend(["Texas"], loc = (0))
ax.set_xticks(year1)
ax.set_xticklabels(x_axis_ticks)

ax = plt.subplot(2,2,2)
plt.plot(year1, louisiana_production)
plt.title("Louisiana Production")
plt.xlabel("Year")
plt.ylabel("1000 BBL Produced")
plt.legend(["Louisiana"], loc = (0))
ax.set_xticks(year1)
ax.set_xticklabels(x_axis_ticks)

ax = plt.subplot(2,2,3)
plt.plot(year1, north_dakota_production)
plt.title("North Dakota Production")
plt.xlabel("Year")
plt.ylabel("1000 BBL Produced")
plt.legend(["North Dakota"], loc = (0))
ax.set_xticks(year1)
ax.set_xticklabels(x_axis_ticks)

ax = plt.subplot(2,2,4)
plt.plot(year1, colorado_production)
plt.title("Colorado Production")
plt.xlabel("Year")
plt.ylabel("1000 BBL Produced")
plt.legend(["Colorado"], loc = (0))
ax.set_xticks(year1)
ax.set_xticklabels(x_axis_ticks)

plt.subplots_adjust(wspace=.4)
plt.subplots_adjust(hspace=.8)

plt.show()

f.savefig("ProducionPlots.pdf")



