import pandas as pd

df = pd.read_csv("Startups in 2021 end.csv" , delimiter= "," , parse_dates= [2] , date_format= {"Date Joined" : "%m-%d-%y"} )
print(df)
print("Dtype:" , df.dtypes)
print("Info" , df.info())
print("Describe:" , df.describe())
print("First 3 rows:" , df.head(3))
print("Last 3 rows:" , df.tail(3))
print("Shape:" , df.shape)
#Print column
column = df["City"]
print("Column:" , column)
column2 = df[["City" , "Date Joined"]]
print("Column2:" , column2)
#Loc
a = df.loc[1]
print("a:" , a)
b = df.loc[ 3: 5]
print("b:" , b)
c = df.loc[df["Country"] == "China"]
print("c:" , c)
d = df.loc[ :7 , ["Country" , "City"]]
print("d:" , d)
e = df.loc[ : 7 , "Country" : "City"]
print("e:" , e)
f = df.loc[df["Country"] == "China" , "City" : "Select Investors"]
print("f:" , f)
#index_col
df_index_col = pd.read_csv("Startups in 2021 end.csv" , delimiter= "," , parse_dates= [2] , date_format= {"Date Joined" : "%m-%d-%y"} , index_col="Company" )
print(df_index_col)
a = df_index_col.loc["Bytedance"]
print("a:" , a)
b = df_index_col.loc["Bytedance" : "BYJU's"]
print("b:" , b)
c = df_index_col.loc[df_index_col["Country"] == "China"]
print("c:" , c)
#iloc
a = df_index_col.iloc[0]
print("a:" , a)
b = df_index_col.iloc[[ 1, 2, 3]]
print("b:" , b)
c = df_index_col.iloc[ : , [1,3]]
print("c:" , c)
d = df_index_col.iloc[ : , 3 : 5]
print("d:" , d)
#Dataframe manipulation
df.loc[len(df.index)] = {
    "Company": "Bytedance",
    "Valuation ($B)": "$140",
    "Date Joined": "4/7/2017",
    "Country": "China",
    "City": "Beijing",
    "Industry": "Artificial intelligence",
    "Select Investors": "Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group"
}
print(df)
df.drop(1 , axis= 0 , inplace= True)
df.drop(index= 3 , axis= 0 , inplace= True)
df.drop([2,4] , axis= 0 , inplace= True)
print(df)
df.drop("City" , axis= 1 , inplace= True )
print(df)
df.rename(columns= {"Country" : "State"} , inplace= True)
df.rename(mapper= {"Date Joined" : "Date"} , axis= 1 , inplace= True)
print(df)
df.rename(index= {3 : 7 , 2: 10} , inplace= True)
df.rename(mapper= {4:5} , axis= 1 , inplace= True)
print(df)
newdf = df.query("Company == 'SpaceX' or 'Date Joined' < '4/7/2017'"  )
print("newdf:" , newdf)
print(len(newdf))
a = df.sort_values(by= "Company")
print("a:" , a)
b = df.sort_values(by= ["Company" , "Industry"])
print("b:" , b)
print("Full dataframe:" , df.to_string())
c = df.groupby("Company") ["Industry"].sum()
print("c:" , c)
df.dropna()
df.fillna(1, inplace= True)
print(df)
data = [1,2,3]
pd.array(data)
print(data)



