import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("covid_19_clean_complete.csv" , delimiter= "," , dtype= None)
print(df)
dffilter = df.head(40)
dffilter100 = df.head(100)

#Histplot
graph = sns.displot(data= dffilter100 , x = 'Confirmed' , hue= 'WHO Region' , kind= "hist")
graph.figure.suptitle("sns.displot(data= dffilter100 , x = 'Confirmed' , hue= 'WHO Region' , kind= 'hist')")
plt.show()
read = input("Wait for me...")
graph = sns.histplot(data= dffilter , x = 'Deaths' , hue= 'WHO Region' , multiple= "stack" )
graph.figure.suptitle("sns.histplot(data= dffilter , x = 'Deaths' , hue= 'WHO Region' , multiple= 'stack' )")
plt.show()
read = input("Wait for me...")

#Scatterplot
graph = sns.scatterplot(data= dffilter , x = 'Confirmed' , y = 'Deaths' , hue= 'Country/Region' )
graph.figure.suptitle("sns.scatterplot(data= dffilter , x = 'Confirmed' , y = 'Deaths' , hue= 'Country' )")
plt.show()
read = input("Wait for me...")

#Barplot
graph = sns.barplot(data= dffilter , x = 'Date' , y = 'Active' , hue= 'WHO Region' )
graph.figure.suptitle("sns.barplot(data= dffilter , x = 'Region' , y = 'Active' , hue= 'WHO Region' )")
plt.show()
read = input("Wait for me...")

#Catplot
graph = sns.catplot(data= dffilter , x = 'Date' , y = 'Confirmed' , hue= 'Country/Region' )
graph.figure.suptitle("sns.catplot(data= dffilter , x = 'WHO Region' , y = 'Confirmed' , hue= 'Country' )")
plt.show()
read = input("Wait for me...")

#Pivot-Reshape
g = dffilter.pivot(columns= "Date" , values= "Active")
graph = sns.heatmap(g)
graph.figure.suptitle("Heatmap")
plt.show()
read = input("Wait for me....")