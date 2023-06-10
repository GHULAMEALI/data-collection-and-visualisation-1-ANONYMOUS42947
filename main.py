import matplotlib.pyplot as plt
import numpy as np
import pandas

#enter a file path according your os
# store the data of PMPL asia 2022 in data variable
data = pandas.read_csv("/home/anonymous/DATA/IDE files/github/1/in.csv",header=None)

# store team name in x variable
x=data[0]
# store team kills in y variable
y=data[1]

# show the data in graph form
plt.plot(x, y)
plt.show()