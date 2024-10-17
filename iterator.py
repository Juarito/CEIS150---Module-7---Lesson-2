#create a list
shoppingList =["milk","bread","eggs","cheese"]

#create iterator from list
shoppingIterator = iter(shoppingList)

#display list using the next() function
print("Display using iterator with next() function: ---")
for i in range(4):
    print(next(shoppingIterator))