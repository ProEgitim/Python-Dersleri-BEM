import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/nabru/Documents/Github/Python-Dersleri-BEM/Ogrenciler/Varol/corona/covid_19_data.csv")
print(df)

df=df.drop("SNo",axis=1)

tr=df[df["Country/Region"]=="Turkey"]

plt.plot(tr.Deaths,tr.Recovered,color="red",label="Türkiye'de ölen/kurtulan hasta sayısı")
plt.xlabel("Ölüm Sayısı")
plt.ylabel("Kurtulan Hasta Sayısı")
plt.title("Türkeye Corona virüs analizi")
plt.legend()

plt.show()