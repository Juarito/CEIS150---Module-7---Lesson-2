class fibonacci:
    def __init__(self): #constructor method initializes values
        self.a=0
        self.b=1
    def __iter__(self): #iterator returns self 
        return self
    def __next__(self): #next method returns next fibonacci number 
        self.fib=self.a+self.b #next Fibonucci number is the sum of the two previous numbers 
        self.a=self.b #we then move b to a 
        self.b=self.fib #and we move fib to b 
        return self.fib #return the new Fibonacci number 

f = fibonacci() #create a new fibonacci object 
print("The Fibonacci Sequence ---") 
print(next(f)) #call the next () method to display the next number 
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))