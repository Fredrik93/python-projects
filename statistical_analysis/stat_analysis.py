# https://medium.com/@hackdeploy/python-t-test-a-friendly-guide-e38ea041481c

# Chose independent t-test, have to check for normal distribution first though, before i can tell that this is viable.
# comparing average of two independent unrelated groups.

import matplotlib.pyplot as plt
import seaborn as sns
import random

random.seed(20)  # for results to be created
N = 50
a = [random.gauss(55, 20) for x in range(N)]

b = [random.gauss(50, 15)for x in range(N)]

sns.kdeplot(a, shade=True)
sns.kdeplot(b, shade=True)
plt.title("Independent sample t-test WORKING :) ")


plt.show()
