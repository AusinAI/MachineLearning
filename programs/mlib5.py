import matplotlib.pyplot as plt
import numpy as np

y = np.array([10,20,30,40,50])
myLabels = ["Apple","Bananas","Cherries","Grapes","Orange"]

plt.pie(y, labels = myLabels, startangle = 90)
plt.show()

