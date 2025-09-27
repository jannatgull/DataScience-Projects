import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("tested.csv" , delimiter= "," , dtype= None , index_col= "PassengerId")
print(df)
print(df.dtypes)

dffilter = df.head(40)
dffilter100 = df.head(100)

#Histplot
graph = sns.displot(data= dffilter , x = 'Age' , hue= 'Survived' , kind= "hist")
graph.figure.suptitle("sns.displot(data= dffilter , x = 'Age' , hue= 'Survived' , kind= 'hist')")
plt.show()
read = input("Wait for me...")
graph = sns.histplot(data= dffilter , x = 'Fare' , hue= 'Sex' , multiple= "stack" )
graph.figure.suptitle("sns.histplot(data= dffilter , x = 'Fare' , hue= 'Sex' , multiple= 'stack' )")
plt.show()
read = input("Wait for me...")

#KDEplot
graph = sns.kdeplot(data= dffilter , x = 'Age' , hue= 'Survived' , multiple= "stack")
graph.figure.suptitle("sns.kdeplot(data= dffilter , x = 'Age' , hue= 'Survived' , multiple= 'stack')")
plt.show()
read = input("Wait for me...")

#Scatterplot
graph = sns.scatterplot(data= dffilter , x = 'Age' , y = 'Fare' , hue= 'Pclass' )
graph.figure.suptitle("sns.scatterplot(data= dffilter , x = 'Age' , y = 'Fare' hue= 'Pclass')")
plt.show()
read = input("Wait for me...")

#Barplot
graph = sns.barplot(data= dffilter , x = 'Embarked' , y = 'Age' , hue= 'Survived' )
graph.figure.suptitle("sns.barplot(data= dffilter , x = 'Embarked' , y = 'Age' , hue= 'Survived' )")
plt.show()
read = input("Wait for me...")

#Catplot
graph = sns.catplot(data= dffilter , x = 'Embarked' , y = 'Age' , hue= 'Survived' )
graph.figure.suptitle("sns.catplot(data= dffilter , x = 'Embarked' , y = 'Age' , hue= 'Survived' )")
plt.show()
read = input("Wait for me...")

#Pivot-Reshape
glue = dffilter.pivot(columns= "Age" , values= "Survived")
graph = sns.heatmap(glue)
graph.figure.suptitle("Heatmap")
plt.show()
read = input("Wait for me....")




