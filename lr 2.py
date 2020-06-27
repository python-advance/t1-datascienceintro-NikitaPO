import pandas  
import matplotlib.pyplot as plt
import numpy as np 

data = pandas.read_csv('train.csv', index_col="PassengerId")

prices = data.sort_values('Fare')
prices = prices["Fare"].value_counts()
##prices = data['Fare']
#prices = prices.sort_values()
count = prices.tolist()
print(count[0])
#prices = prices.keys().sort_values()

#print(len(prices))

x = np.linspace( 0, count[0],  len(count))
y = prices.keys()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xticks(np.arange(0, max(count)+5, 5.0))
plt.yticks(np.arange(0, max(prices.keys()+50), 50.0))
ax.set_xlabel('Число пассажиров купивших билеты за эту стоимость')
ax.set_ylabel('Стоимость билетов')
ax.scatter(x, y, color = 'black', s = 2)
fig.savefig('graph.png')
