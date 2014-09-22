import matplotlib.pyplot as pp
import pandas
import math
import sys

dataframe = pandas.io.parsers.read_csv(sys.argv[1], sep="\t")
print(dataframe)