# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(flights,range=(0,365),bins=365)
plt.title("Daily Flight Count")
plt.xlabel("Days")
plt.ylabel("Count")

plt.subplot(212)
plt.hist(in_bloom,range=(0,365),bins=365)
plt.title("Daily Blooming Flowers")
plt.xlabel("Days")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
