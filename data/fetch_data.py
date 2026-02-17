from ucimlrepo import fetch_ucirepo 
import matplotlib.pyplot as plt
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
x = mushroom.data.features 
y = mushroom.data.targets 
  
# metadata 
print(mushroom.metadata) 
  
# variable information 
print(mushroom.variables) 

plt.figure()
plt.scatter("poisonous", "veil-type")
plt.show()
plt.savefig('chart_1.png')