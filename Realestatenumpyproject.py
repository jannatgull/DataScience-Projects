import numpy as np

status , price , bath , bed = np.genfromtxt("RealEstate-USA (2).csv" , delimiter= "," , usecols= (1,2,3,4) , unpack= True , dtype= None , skip_header= 1)
print(status)
print(price)
print(bath)
print(bed)

print("Mean:" , np.mean(price))
print("Median:" , np.median(price))
print("Std:" , np.std(price))
print("Min:" , np.min(price))
print("Max:" , np.max(price))
print("Percentile 75:" , np.percentile(price , 75))
print("Percentile 25:" , np.percentile(price , 25))
print("Percentile 3:" , np.percentile(price , 3))
print("Two arrays:" , np.mean(price) , np.mean(bath))

print("Square:" , np.square(price))
print("Squareroot:" , np.sqrt(price))
print("Absolute value:" , np.abs(price))
print("Power:" , np.power(price , price))

print("Sin:" , np.sin(price))
print("Cos:" , np.cos(price))
print("Tan:" , np.tan(price))
print("Log:" , np.log(price))
print("Log10:" , np.log10(price))

print("Sinh:" , np.sinh(price))
print("Cosh:" , np.cosh(price))
print("Tanh:" , np.tanh(price))

print("Arcsin:" , np.arcsin(price))
print("Arccos:" , np.arccos(price))
print("Arctan:" , np.arctan(price))

Dimensionalarray = np.array([price , bath])
print("Dimensional array:" , Dimensionalarray)
print("Dimension:" , Dimensionalarray.ndim)
print("Size:" , Dimensionalarray.size)
print("Shape:" , Dimensionalarray.shape)
print("Dtype:" , Dimensionalarray.dtype)

Arrayslicing = Dimensionalarray[ 0 : 2 , 3 : 9]
print("Arrayslicing:" , Arrayslicing)
Arrayslicing2 = Dimensionalarray[ : 1 , 5 : 20 : 6]
print("Arrayslicing2:" , Arrayslicing2)

Onlyoneitem = Arrayslicing2[ 0 , 2]
print("Onlyoneitem:" , Onlyoneitem)

for i in np.nditer(price) :
    print(i)

for index , i in np.ndenumerate(price) :
    print(index , i)

Reshaping = np.reshape(Arrayslicing2 , ( 3, 1))
print("Reshaping:" , Reshaping)
 