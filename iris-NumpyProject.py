import numpy as np

sepallength , sepalwidth , petallength = np.genfromtxt("iris.csv" , delimiter= "," , usecols= [0 , 1, 2] , dtype= None , skip_header= 1 , unpack= True)
print(sepallength)
print(sepalwidth)
print(petallength)

#Staticoperations
print("Mean of sepallength:" , np.mean(sepallength))
print("Meadian of sepallength:" , np.median(sepallength))
print("Standard deviation of sepallength:" , np.std(sepallength))
print("Maximum of seaplength:" , np.max(sepallength))
print("Minimum of sepallength:" , np.min(sepallength))
print("Average of sepallength:" , np.average(sepallength))
print("3 Percentile of sepallength:" , np.percentile(sepallength , 3))
print("75 Percentile of sepallength:" , np.percentile(sepallength , 75))
print("25 Percentile of sepallength:" , np.percentile(sepallength , 25))

#Mathematicaoperations
print("Square of sepallength:" , np.square(sepallength))
print("Square root of sepallength:" , np.sqrt(sepallength))
print("Absolute Value of sepallength:" , np.abs(sepallength))
print("Power of sepallength:" , np.power(sepallength , sepallength))
Addition = sepallength + sepalwidth
print("Addition of sepallength and sepalwidth" , Addition)
Substraction = sepallength - sepalwidth
print("Substraction of sepallength and sepalwidth" , Substraction )
Multiplication = sepallength * sepalwidth
print("Multiplication of sepallength and sepalwidth" , Multiplication)
Division = sepallength / sepalwidth
print("Division of sepallength and sepalwidth" , Division )

#TrigonometricFunctions
print("Sin:" , np.sin(petallength))
print("Cos:" , np.cos(petallength))
print("Tan:" , np.tan(petallength))
print("Exponential:" , np.exp(petallength))
print("Logarithm:" , np.log(petallength))
print("Logarithm10" , np.log10(petallength))

#HyperbolicFunctions
print("Sinh:" , np.sinh(petallength))
print("Cosh:" , np.cosh(petallength))
print("Tanh:" , np.tanh(petallength))

#InverseHyperbolicFunctions
print("Arcsinh:" , np.arcsinh(petallength))
print("Arccosh:" , np.arccosh(petallength))
print("Arctanh:" , np.arctanh(petallength))

#2Dimensionalarray
D2sepal = np.array([sepallength , sepalwidth])
print("2 Dimensional array:",D2sepal)
#Dimension
print("Dimension:" , D2sepal.ndim)
#Size
print("Size:" , D2sepal.size)
#Shape
print("Shape:" , D2sepal.shape)
#Dtype
print("Dtype:" , D2sepal.dtype)

#ArraySlicing
D2sepalslicing = D2sepal[ : 1 , : 5]
print("Array Slicing:" , D2sepalslicing)
D2sepalslicing2 = D2sepal[ : 1 , 4 : 15 : 4]
print("Array Slicing2:" , D2sepalslicing2)

#Indexing
D2ArrayOnlyItem = D2sepal[ 1 , 3]
print("Only 1 Item:" , D2ArrayOnlyItem)

#Iteration
for i in np.nditer(D2sepal) :
    print(i)

for index , i in np.ndenumerate(D2sepal) :
    print(index , i)

#Reshaping
D2sepalReshaping = np.reshape(D2sepal , (150 , 2))
print("Reshape:" , D2sepalReshaping)


