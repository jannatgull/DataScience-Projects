import pandas as pd 

df = pd.read_csv("diabetes.csv" , delimiter= "," , dtype= None)
print(df)

#dtype
print("dtype:" , df.dtypes)
#info
print("Information:" , df.info())
#head
print("First 30 rows:" , df.head(30))
#tail
print("Last 30 rows:" , df.tail(30))
#describe
print("Static operations:" , df.describe())
#shape
print("Shape:" , df.shape)

#Column
Glucosecolumn = df["Glucose"]
print("Glucose Column:" , Glucosecolumn)
Glucose_BP = df[["Glucose" , "BloodPressure"]]
print("Glucose_BP Column:" , Glucose_BP)

#Loc
thirdrow1= df.loc[2]
print("Third row:" , thirdrow1)
thirdrow2 = df.loc[2 : 7]
print("Third to sixth row:" , thirdrow2)
thirdrow3 = df.loc[df ["Glucose"] == "3"]
print("Conditional selection of rows:" , thirdrow3)
thirdrow4 = df.loc[ : 1 , "Glucose"]
print("Single column:" , thirdrow4)
thirdrow5 = df.loc[ : 1 , ["Glucose" , "BloodPressure"]]
print("2 Columns:" , thirdrow5)
thirdrow6 = df.loc[ df["Glucose"] == "3" , "BloodPressure" : "Insulin"]
print("Combined row and column selection:" , thirdrow6)

#Loc with index_col
dfindex_col = pd.read_csv("diabetes.csv" , delimiter= "," , dtype= None , index_col= "Pregnancies")
print(dfindex_col)

thirdrow1= dfindex_col.loc[1]
print("Third row:" , thirdrow1)
thirdrow2 = dfindex_col.loc[[6 , 1]]
print("Third to sixth row:" , thirdrow2)
thirdrow3 = dfindex_col.loc[dfindex_col ["Glucose"] == "3"]
print("Conditional selection of rows:" , thirdrow3)
thirdrow4 = dfindex_col.loc[ 10 , "Glucose"]
print("Single column:" , thirdrow4)
thirdrow5 = dfindex_col.loc[ 7, ["Glucose" , "BloodPressure"]]
print("2 Columns:" , thirdrow5)
thirdrow6 = dfindex_col.loc[ dfindex_col["Glucose"] == "3" , "BloodPressure" : "Insulin"]
print("Combined row and column selection:" , thirdrow6)

#Iloc
thirdrow1 = dfindex_col.iloc[2]
print("Third row:" , thirdrow1)
thirdrow2 = dfindex_col.iloc[[1,2,3,4]]
print("Multiple rows:" , thirdrow2)
thirdrow3 = dfindex_col.iloc[ 1 : 8]
print("Slicing:" , thirdrow3)
thirdrow4 = dfindex_col.iloc[ : , [1,3]]
print("Selective columns:" , thirdrow4)
thirdrow5 = dfindex_col.iloc[ [ 1,2,3] , 1: 9]
print("Selective rows and columns:" , thirdrow5)

#Dataframe manipulation
#Row add
df.loc[len(df.index)] = [1, 7, 9, 5, 4 ,3 , 8, 4 ,9]
print(df)
#Row drop
df.drop(1 , axis= 0 , inplace= True)
df.drop( index = [ 2, 3] , axis= 0 , inplace= True)
df.drop( 5 , axis= 0 , inplace= True)
print(df)
#Column drop
df.drop("Insulin" , axis= 1 , inplace= True)
print(df)
#Rename column
df.rename(columns= {"BloodPressure" : "BP"} , inplace= True)
df.rename(mapper= {"Age" : "Lifespan"} , axis= 1 , inplace= True)
print(df)
#Index rename
df.rename(index= { 0 : 7} , inplace= True)
df.rename(mapper= { 2: 20 , 3 : 8} , axis= 0 , inplace= True)
print(df)
#Query 
query = df.query("Glucose == '3' or BMI > 28.1")
print(query)
print(len(query))
#Sorting
sorted_df = df.sort_values(by= "Glucose")
sorted_df = df.sort_values(by= "BMI")
print(df)
print(df.to_string)
#Grouping
grouped = df.groupby("Glucose") ["BMI"].sum()
print(df)
#Missing value
df_cleaned = df.dropna()
print(df_cleaned)
df.fillna( 0 , inplace= True)
print(df)









