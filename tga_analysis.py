import matplotlib.pyplot as pp
import pandas
import math
import sys

maxWeightFilterHold = 19.64691
maxWeightCasingHold = 5.15985
maxWeightCasingHold = 9.727528
maxWeightEkoHold = 37.19263  #37.15359
# maxWeightEkoHold = 45.21924



dFCasingHold = pandas.read_table('casing_hold2.csv', sep=',', names=['Time', 'Temp', 'Weight'])
#dFCasingSlowRamp = pandas.read_table('casing_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dFFilterHold =pandas.read_table('plastic_filter_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
#dfFilterSlowRamp = pandas.read_table('plastic_filter_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])
dfEkoHold = pandas.read_table('ekocup_hold.csv', sep=',', names=['Time', 'Temp', 'Weight'])
#dfEkoSlowRamp = pandas.read_table('ekocup_slowRamp.csv', sep=',', names=['Time', 'Temp', 'Weight'])




dFFilterHold['Weight'] = dFFilterHold['Weight']/maxWeightFilterHold
dFCasingHold['Weight'] = dFCasingHold['Weight']/maxWeightCasingHold
dfEkoHold['Weight'] = dfEkoHold['Weight']/maxWeightEkoHold



pp.plot(dFCasingHold['Time'],dFCasingHold['Weight']*100, 'r')
pp.plot(dfEkoHold['Time'],dfEkoHold['Weight']*100, 'g')
pp.title('Mass lost while holding at 89 degrees Celcius')
pp.legend(['Casing','EkoCup'])
pp.xlabel('Time (minutes)')
pp.ylabel('Percent Mass')
pp.show()


pp.figure()
pp.clf()
pp.plot(dFCasingHold['Time'][0:300],dFCasingHold['Weight'][0:300]*100, 'r')
#pp.plot(dFFilterHold['Time'][367:],dFFilterHold['Weight'][367:])
pp.plot(dfEkoHold['Time'][0:300],dfEkoHold['Weight'][0:300]*100, 'g')

pp.title('Mass lost while holding at 89 degrees Celcius')
pp.legend(['Casing','EkoCup'])
pp.xlabel('Time (minutes)')
pp.ylabel('Percent Mass')
pp.show()