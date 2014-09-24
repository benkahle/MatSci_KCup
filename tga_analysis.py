import matplotlib.pyplot as pp
import pandas
import math
import sys

maxWeightFilterHold = 19.64691
maxWeightCasingHold = 5.15985


dFCasingHold = pandas.read_table('casing_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dFCasingSlowRamp = pandas.read_table('casing_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dFFilterHold =pandas.read_table('plastic_filter_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dfFilterSlowRamp = pandas.read_table('plastic_filter_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])

dFFilterHold['Weight'] = dFFilterHold['Weight']/maxWeightFilterHold
dFCasingHold['Weight'] = dFCasingHold['Weight']/maxWeightCasingHold
pp.plot(dFCasingHold['Time'][940:],dFCasingHold['Weight'][940:], 'r')
pp.plot(dFFilterHold['Time'][367:],dFFilterHold['Weight'][367:])
pp.show()
print(dataframe)