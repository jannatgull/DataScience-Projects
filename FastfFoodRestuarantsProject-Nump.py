import numpy as np

latitude, longitude = np.genfromtxt("FastFoodRestaurants.csv" , delimiter="," , usecols= [4,5] , unpack= True, skip_header= 1 , invalid_raise= False , dtype= float)
print(latitude)
print(longitude)
latitude = latitude[~np.isnan(latitude)]
longitude = longitude[~np.isnan(longitude)]
#Static operations
print("Mean:" , np.mean(latitude))
print("Median:" , np.median(latitude))
print("std:" , np.std(latitude))
print("Max:" , np.max(latitude))
print("Min:" , np.min(latitude))
print("Percentile 75:" , np.percentile(latitude , 75))
print("Percentile 25:" , np.percentile(latitude , 25))
print("Percentile 3:" , np.percentile(latitude , 3))
#Mathematical operations
print("Square:" , np.square(latitude))
print("Sqrt:" , np.sqrt(latitude))
print("Absolute value:" , np.abs(latitude))
print("Power:" , np.power(latitude , latitude))
n = min(len(latitude) , len(longitude))
latitude = latitude[ :n]
longitude = longitude[ : n]
addition = latitude + longitude
print("Addition:" , addition)
subtraction = latitude - longitude
print("Subtraction:" , subtraction)
multiplication = latitude * longitude
print("Multiplication:" , multiplication)
division = latitude / longitude
print("Division:" , division)
#Trigonometric function
latitudepi = (latitude / np.pi) + 1 
print("Latitude:" , latitudepi)
print("Sin:" , np.sin(latitude))
print("Cos:" , np.cos(latitude))
print("Tan:" , np.tan(latitude))
print("Exponential:" , np.exp(latitude))
print("Logarithm:" , np.log(latitude))
print("Logarithm10:" , np.log10(latitude))
#Hyperbolic functions
print("Sinh:" , np.sinh(latitude))
print("Cosh:" , np.cosh(latitude))
print("Tanh:" , np.tanh(latitude))
#Inverse Hyperbolic functions
print("Arcsinh:" , np.arcsinh(latitude))
print("Arccos:" , np.arccosh(latitude))
print("Arctanh:" , np.arctanh(latitude))
#2-Dimensional array
Dimensionalarray2 = np.array([latitude , longitude])
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
Reshape = np.reshape(Dimensionalarray2 , (9906 , 2))
print("Reshape:" , Reshape)
