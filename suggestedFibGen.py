def fibonacci():
    a = 1  # initialize the first number
    b = 2  # initialize the second number
    while True:  # create an infinite loop to generate Fibonacci numbers
        yield a  # return the number and pause the function
        fib = a + b  # calculate the next Fibonacci number
        a = b  # move 'b' to 'a'
        b = fib  # move the new Fibonacci number to 'b'

print("The Fibonacci Sequence ---")
for f in fibonacci():  # call the fibonacci() generator in a loop
    if f > 50:  # break out of the loop if the number is > 50
        break
    print(f)  # print the number generated
