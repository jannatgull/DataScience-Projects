import pandas as pd 

df = pd.read_csv("RealEstate-USA (2).csv" , delimiter= "," , parse_dates=[11] , date_format= {"prev_sold_date" : "%d-%m-%y"})
print(df)

print("Datatypes:" , df.dtypes)
print("Info:" , df.info())
print("Head:" , df.head(3))
print("Tail:" , df.tail(3))
print("Describe:" , df.describe())
print("Shape:" , df.shape)

print("Column:" , df["bed"])
print("2Columns:" , df[["bed" , "bath"]])

#LOC
a = df.loc[1]
print("a:" , a)
b = df.loc[[1 , 3]]
print("b:" , b)
c = df.loc[ : 6 , "bed"]
print("c:" , c)
d = df.loc[ : 6 , ["bed" , "bath"]]
print("d:" , d)
e = df.loc[ : 8 , "bath" : "city"]
print("e:" , e)
f = df.loc[df["city"] == "Juana Diaz"]
print("f:" , f)
g = df.loc[df["city"] == "Juana Diaz" , "bath" : "city"]
print("g:" , g)
#indexcolloc
df_index_col = pd.read_csv("RealEstate-USA (2).csv" , delimiter= "," , parse_dates= [11] , date_format={"prev_sol_date" : "%d-%m-%y"} , index_col= "brokered_by" )
print(df_index_col)
a = df_index_col.loc[103378]
print("a:" , a)
b = df_index_col.loc[[52707 , 31239]]
print("b:" , b)
d = df_index_col.loc[  34632 , "status"]
print("d:" , d)
e = df_index_col.loc[df_index_col["bed"] == 6.0]
print("e:" , e)
f = df_index_col.loc[df_index_col["bed"] == 6.0 , "price" : "bath" ]
print("f:" , f)
#iloc
a = df_index_col.iloc[1]
print("a:" , a)
b = df_index_col.iloc[ [1,2,3]]
print("b:" , b)
c = df_index_col.iloc[ : 5]
print("c:" , c)
d = df_index_col.iloc[ : , [ 1, 2, 3]]
print("d:" , d)
e = df_index_col.iloc[ : , 2: 9]
print("e:" , e)
#Row add
df.loc[len(df.index)] = ["Gateawayproperties", "for_sale", 250000, 3, 2, 0.25, "123 Main St", "Houston", "TX", 77001, 1800, "2018-06-15"]
print(df)
#Row delete
df.drop( 1 , axis = 0 , inplace= True)
df.drop( index= 3 , axis = 0 , inplace= True)
df.drop([ 4,5] , axis = 0 , inplace= True )
print(df)
#Column delete
df.drop("price" , axis = 1, inplace= True)
print(df)
#Rename column
df.rename( columns= {"price" : "qeemat"} , inplace= True)
print("REname column:" , df)
df.rename(mapper= {"status" : "renamedstatus"} , axis= 1 , inplace= True)
print("RENAMED COLUMN:" , df)
#Index rename
df.rename( index= { 0:7} , inplace= True)
print("Index:" , df)
df.rename( mapper= { 6 : 2 , 8 : 100} , axis= 0 , inplace= True)
print("Index2:" , df)
#Sorting
a = df.sort_values( by= "bath")
print("a:" , a)
b = df.sort_values( by= ["bath" , "bed"] )
print("b:" , b)
#Fulldataframe
print(df.to_string)
#missingvalues
a = df.dropna()
print("Dropa:" , a)
df.fillna( 1, inplace= True)
print(df)
#query


