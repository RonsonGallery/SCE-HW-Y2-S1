import string

def evenFactorial(n):
    if(n<=0): #checks if at the end of the number
        return 1
    if(n%2==0):
        return n*evenFactorail(n-1) #if number is even multiplies by that number
    return evenFactorial(n-1)
def printBin(n):
   if n > 1:
       convertToBinary(n//2) 
   print(n % 2,end = '')
def bracketsCheck(String):
    global numP
    numP = 0
    if len(String)==0: return numP==0
    if numP < 0: return False
    if String[0] == "(":
        numP += 1
        return balanced_str(String[1:])
    elif String[0] == ")":
        numP -= 1
        return balanced_str(String[1:])
    return balanced_str(String[1:])

def interceptPoint(m1,n1,m2,n2):
    if(m1 == m2): #checks if the two lines are paralel
        return 'None'
    y = int((n1-n2)/(m1-m2)) # gets y 
    x = int((y - n1)/m1) # gets x
    return tuple(x,y)

def parseStr(a):
    i=0
    flag = 1
    intNumber = int(0)
    if(a[i] == '-'):
        i=1
        flag = -1
    x = int(len(a))
    for j in range(i,x):
        if((int(ord(a[j]) - ord('0')) > 9) | ((int(ord(a[j]) - ord('0'))) < 0)): #checks if the input is valid
            print("There was a letter in the input returning 0")
            return 0
        intNumber += int(ord(a[j]) - ord('0')) #does conversion from Char to Int
        if(j<x-1): #makes sure dont multiply too many times
            intNumber *=10

    intNumber*=flag
    print("The Number after the conversion into Integer is:"+ str(intNumber))
    return intNumber  
def smallHash(arr):
    length = len(arr)
    f0 = arr[0] #recives the first parameter at the
    fnb = f0
    for i in range(1,length): 
        fn = ((31*fnb)^arr[i]) & 0xff #converts to hash with the requested function
        fnb = fn #contains value of pervious variable

    return fn
def factorSum(n):
    for i in range (2,n+1):
        if(n % i != 0):
                isPrime = 1 #flag to see if number is prime or not 
        for j in range (2,i):
            if(i % j == 0 & i!=j):
                isPrime = 0 #if the number is not prime flags it as 0
                break
        if(isPrime == 1):
            sum += i #Acummolates sum of all Prime numbers that fit the bill
    return sum

# Access to the function's plus testing
Number = input("Enter a number")
Number = parseStr(Number)
x = int(input("Enter the ammount of numbers would you like to enter"))
Arr = []
print("Enter Numbers with enters every number")
for i in range(0,x):
    Arr.append(int(input()))
print(smallHash(Arr))
m1 = input("Enter Recuired Angle")
m2 = input("Enter Recuired Angle")
n1 = input("Enter Recuired n1")
n2 = input("Enter Recuired n2")
print(interceptPoint(m1,n1,m2,n2))

x = int(input("Enter a number to do an even factorial for:"))
print(evenFactorial(x))

x = int(input("Enter number to convert to binary"))
print(printBin(x))