import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("hepatitis.csv")
data=pd.DataFrame(data.head())
print(data)

x = data['state_name']
y = data['incidence_per_capita']

plt.title("Incidence of Hepatitis per state")
plt.bar(x,y,width=0.8)
plt.xlabel("State")
plt.ylabel("Incidence per capital")
plt.show()
