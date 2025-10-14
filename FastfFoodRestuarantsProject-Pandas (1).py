import pandas as pd

df = pd.read_csv("FastFoodRestaurants.csv" , delimiter=",")
print(df)
print("Datatype:" , df.dtypes)
print("Information:" , df.info())
print("Describe:" , df.describe())
print("First 3 rows:" , df.head(3))
print("Last 3 rows:" , df.tail(3))
print("Shape:" , df.shape)
#Print Column
print("Column:" , df["address"])
print("Two columns:" , df[["address" , "name"]])
#LOC
details1 = df.loc[1]
print("details1:" , details1)
details2 = df.loc[[3,5]]
print("Details2:" , details2)
details3 = df.loc[ 3 : 7]
print("Details3:" , details3)
details4 = df.loc[df["city"] == "Hamilton" ]
print("Details4:" , details4)
details5 = df.loc[ : 9 , "address"]
print("Details5:" , details5)
details6 = df.loc[ : 8 , ["name" , "address"]]
print("Details6:" , details6)
details7 = df.loc[ : 1 , "address" : "city"]
print("details7" , details7)
details8 = df.loc[ df["city"] == "Hamilton" , "address" : "city"]
print("details8:" , details8)
#index_col_LOc
df_index_col = pd.read_csv("FastFoodRestaurants.csv" , delimiter= "," , index_col= "address")
print(df_index_col)
record1 = df_index_col.loc["324 Main St"]
print("Record1:" , record1)
record2 = df_index_col.loc["324 Main St" : "139 Columbus Rd"]
print("Record2:" , record2)
record3 = df_index_col.loc["324 Main St" : "139 Columbus Rd", "city"]
print("Record3:" , record3)
record4 = df_index_col.loc["324 Main St" : "139 Columbus Rd", ["name" , "city"]]
print("Record4:" , record4)
record5 = df_index_col.loc["324 Main St" : "139 Columbus Rd" , "city" : "name"]
print("Record5:" , record5)
record6 = df_index_col.loc[df_index_col["city"] == "Hamilton"]
print("Record6:" , record6)
#Iloc
data1 = df_index_col.iloc[1]
print("data1:" , data1)
data2 = df_index_col.iloc[[1, 2, 3, 4]]
print("data2:" , data2)
data3 = df_index_col.iloc[ : , 2]
print("data3:" , data3)
data4 = df_index_col.iloc[ : 5 , [1,3,7]]
print("data4:" , data4)
data5 = df_index_col.iloc[ [1,3,4] , 4:8]
print("data5:" , data5)
#Row add
df.loc[len(df.index)] = {"address": "324 Main St",
    "city": "Massena",
    "country": "US",
    "keys": "us/ny/massena/324mainst/-1161002137",
    "latitude": 44.9213,
    "longitude": -74.89021,
    "name": "McDonald's",
    "postalCode": 13662,
    "province": "NY",
    "websites": "http://mcdonalds.com,http://www.mcdonalds.com/?cid=RF:YXT_FM:TP::Yext:Referral"}
print(df)
#Row delete
df.drop( 1 , axis= 0 , inplace= True)
df.drop( index =  5 , axis = 0, inplace= True)
df.drop( [ 4, 7] , axis= 0 , inplace= True)
print(df)
#Column drop
df.drop( "city" , axis= 1 , inplace= True)
print(df)
#Rename column
df.rename(columns= {"Address" : "Location"} , inplace= True)
df.rename(mapper= {"Name" : "Namechanged"} , axis= 1 , inplace= True)
print(df)
#Index rename 
df.rename(index = { 0 : 6} , inplace= True)
df.rename(mapper= { 5  : 19} , axis= 0 , inplace= True)
print(df)
#Querylikesql
Newdf = df.query("country == 'US' or latitude > 44.9213")
print(len(Newdf))
#Sorting
a = df.sort_values( by= "longitude")
print("a:" , a)
b = df.sort_values( by= ["longitude" , "latitude"] )
print("b:" , b)
print(df.to_string())
#Groupby
c = df.groupby("keys")  ["latitude"].sum()
print("c:" , c)
#MissingValues
d = df.dropna()
print("d:" , d)
df.fillna( 1 , inplace= True)
print(df)
#array
data = [ 1, 2, 3]
print("array:" , pd.array(data))





