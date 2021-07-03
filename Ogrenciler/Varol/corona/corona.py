import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("C:/Users/nabru/Documents/Github/Python-Dersleri-BEM/Ogrenciler/Varol/corona/covid_19_data.csv")


print(df)
df=df.drop("SNo",axis=1)
tr=df[df["Country/Region"]=="Turkey"]


# plt.plot(tr.Deaths,tr.Recovered,color="red",label="Türkiye'de ölen/kurtulan hasta sayısı")

# plt.scatter(tr.Deaths,tr.Recovered,color="red",label="Türkiye'de ölen/kurtulan hasta sayısı")

# plt.hist(tr.Deaths,tr.Recovered,color="red",label="Türkiye'de ölen/kurtulan hasta sayısı")


# plt.xlabel("Ölüm Sayısı")
# plt.ylabel("Kurtulan Hasta Sayısı")
# plt.title("Türkeye Corona virüs analizi")
# plt.legend()



s=np.array([1,2,3,4,5,6,7,8,9])
k=s**2
plt.bar(s,k)
plt.xlabel("Sayı değeri")
plt.ylabel("sayının karesi")
plt.title("sayıların karesini alma")

plt.show()