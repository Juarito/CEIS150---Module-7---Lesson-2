def fibonacci():
    a=0 #initialize first two numbers
    b=1
    while True: #create an infinite loop to generate Fibonacci numbers
      fib=a+b #generate next Fibonacci number
      yield fib #return the number and pause the function
      a=b #when function resumes, it starts here
      a=fib

print("The Fibonacci Sequence ---")
for f in fibonacci(): #call the fibonacci() generator in a loop
   if f > 50: #break out the loop if the number is > 50
       break
   print(f) #print the number generated