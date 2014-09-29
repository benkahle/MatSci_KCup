import matplotlib.pyplot as pp
import pandas
import math
import sys

maxWeightFilterHold = 19.64691
maxWeightCasingHold = 5.15985
maxWeightEkoHold = 37.15359


dFCasingHold = pandas.read_table('casing_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dFCasingSlowRamp = pandas.read_table('casing_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dFFilterHold =pandas.read_table('plastic_filter_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dfFilterSlowRamp = pandas.read_table('plastic_filter_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dfEkoHold = pandas.read_table('ekocup_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dfEkoSlowRamp = pandas.read_table('ekocup_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])




dFFilterHold['Weight'] = dFFilterHold['Weight']/maxWeightFilterHold
dFCasingHold['Weight'] = dFCasingHold['Weight']/maxWeightCasingHold
dfEkoHold['Weight'] = dfEkoHold['Weight']/maxWeightEkoHold


pp.plot(dFCasingHold['Time'][0:500],dFCasingHold['Weight'][0:500], 'r')
#pp.plot(dFFilterHold['Time'][367:],dFFilterHold['Weight'][367:])
pp.plot(dfEkoHold['Time'][0:500],dfEkoHold['Weight'][0:500])
pp.show()
print(dataframe)