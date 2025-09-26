import numpy as np

Pregnancies , Glucose , Bloodpressure = np.genfromtxt("diabetes.csv" , delimiter= "," , usecols= [0,1,2] , unpack= True , dtype= None , skip_header= 1)
print(Pregnancies)
print(Glucose)
print(Bloodpressure)

#Static Operations 
print("Mean of Glucose:" , np.mean(Glucose))
print("Meadian of Glucose:" , np.median(Glucose))
print("Standard deviation of Glucose:" , np.std(Glucose))
print("Maximum of Glucose:" , np.max(Glucose))
print("Minimum of Glucose:" , np.min(Glucose))
print("Average of Glucose:" , np.average(Glucose))
print("3 Percentile of Glucose:" , np.percentile(Glucose, 3))
print("75 Percentile of Glucose:" , np.percentile(Glucose , 75))
print("25 Percentile of Glucose:" , np.percentile(Glucose, 25))

#Mathematical Operations
print("Square of Glucose:" , np.square(Glucose))
print("Square root of Glucose:" , np.sqrt(Glucose))
print("Absolute Value of Glucose:" , np.abs(Glucose))
print("Power of Glucose:" , np.power(Glucose , Glucose))
Addition = Glucose + Pregnancies
print("Addition of Glucose and Pregnancies" , Addition)
Substraction = Glucose - Pregnancies
print("Substraction of Glucose and Pregnancies" , Substraction )
Multiplication = Glucose * Pregnancies
print("Multiplication of Glucose and Pregnancies" , Multiplication)
Division = Glucose / Pregnancies
print("Division of Glucose and Pregnancies" , Division )

#Trigonometric Functions
print("Sin:" , np.sin(Bloodpressure))
print("Cos:" , np.cos(Bloodpressure))
print("Tan:" , np.tan(Bloodpressure))
print("Exponential:" , np.exp(Bloodpressure))
print("Logarithm:" , np.log(Bloodpressure))
print("Logarithm10" , np.log10(Bloodpressure))

#HyperbolicFunctions
print("Sinh:" , np.sinh(Bloodpressure))
print("Cosh:" , np.cosh(Bloodpressure))
print("Tanh:" , np.tanh(Bloodpressure))

#InverseHyperbolicFunctions
print("Arcsinh:" , np.arcsinh(Bloodpressure))
print("Arccosh:" , np.arccosh(Bloodpressure))

#2Dimensionalarray
D2glucose_Bp = np.array([Glucose , Bloodpressure])
print("2 Dimensional array:", D2glucose_Bp)
#Dimension
print("Dimension:" , D2glucose_Bp.ndim)
#Size
print("Size:" , D2glucose_Bp.size)
#Shape
print("Shape:" , D2glucose_Bp.shape)
#Dtype
print("Dtype:" , D2glucose_Bp.dtype)

#ArraySlicing
D2glucose_Bpslicing = D2glucose_Bp[ : 1 , : 5]
print("Array Slicing:" , D2glucose_Bpslicing)
D2glucose_Bpslicing2 = D2glucose_Bp[ : 1 , 4 : 15 : 4]
print("Array Slicing2:" , D2glucose_Bpslicing2)

#Indexing
D2ArrayOnlyItem = D2glucose_Bp[ 1 , 3]
print("Only 1 Item:" , D2ArrayOnlyItem)

#Iteration
for i in np.nditer(D2glucose_Bp) :
    print(i)

for index , i in np.ndenumerate(D2glucose_Bp) :
    print(index , i)

#Reshaping
D2sepalReshaping = np.reshape(D2glucose_Bp , (768 , 2))
print("Reshape:" , D2sepalReshaping)







