import numpy as np

company , valuation , datetime, City = np.genfromtxt("Startups in 2021 end.csv" , delimiter= "," , unpack= True  , usecols= [0, 1,2,3] , invalid_raise= False, dtype= None, skip_header= 1)
print(company)
print(valuation)
print(datetime)
print(City)
datetime= np.char.replace(datetime, "$", "")
datetime = np.char.replace(datetime, ",", "")
datetime = datetime[datetime != ""]   
datetime = datetime.astype(float)
print("Mean:" , np.mean(datetime))
print("Median:" , np.median(datetime))
print("std:" , np.std(datetime))
print("Max:" , np.max(datetime))
print("Min:" , np.min(datetime))
print("Percentile 75:" , np.percentile(datetime , 75))
print("Percentile 25:" , np.percentile( datetime, 25))
print("Percentile 3:" , np.percentile( datetime, 3))
#Mathematical operations
print("Square:" , np.square(datetime))
print("Sqrt:" , np.sqrt(datetime))
print("Absolute value:" , np.abs(datetime))
print("Power:" , np.power(datetime , datetime))
add = company + datetime
print("Add:" , add)
sub = company - datetime
print("Sub:" , sub)
multiply = company * datetime
print("Multiply:" , multiply)
division = company / datetime
print("Division:" , division)
#Trigonometric functions
companypi = (company / np.pi) + 1 
print("companypi:" , companypi)
print("Sin:" , np.sin(company))
print("Cos:" , np.cos(company))
print("Tan:" , np.tan(company))
print("Exponential:" , np.exp(company))
print("Logarithm:" , np.log(company))
print("Logarithm10:" , np.log10(company))
#Hyperbolic functions
print("Sinh:" , np.sinh(company))
print("Cosh:" , np.cosh(company))
print("Tanh:" , np.tanh(company))
#Inverse Hyperbolic functions
print("Arcsinh:" , np.arcsinh(company))
print("Arccos:" , np.arccosh(company))
print("Arctanh:" , np.arctanh(company))
#2-Dimensional array
Dimensionalarray2 = np.array([company , datetime])
print("2dimensionalarray:" , Dimensionalarray2)
print("Dimension:" , Dimensionalarray2.ndim)
print("Size:" , Dimensionalarray2.size)
print("Shape:" , Dimensionalarray2.shape)
print("Dtype:" , Dimensionalarray2.dtype)
#ArraySlicing
Arrayslicing = Dimensionalarray2[ : 1 , : 5]
print("Arrayslicing:" , Arrayslicing)
Arrayslicing2 = Dimensionalarray2[ : 1, 4 : 15 : 4]
print("Arrayslicing2:" , Arrayslicing2)
#Indexing
Dimensionalarrayindexing = Dimensionalarray2[ 0, 5]
print("Indexing:" , Dimensionalarrayindexing)
#Nditer
for i in np.nditer(Dimensionalarray2) :
    print(i)
for index , i in np.ndenumerate(Dimensionalarray2) :
    print(index , i)
#Reshape
Reshape = np.reshape(Dimensionalarray2 , (936, 2))
print("Reshape:" , Reshape)
