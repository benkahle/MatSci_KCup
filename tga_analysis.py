import matplotlib.pyplot as pp
import pandas
import math
import sys
print sys.argv[1]
dataframe = pandas.read_table(sys.argv[1], sep=',')
print(dataframe)