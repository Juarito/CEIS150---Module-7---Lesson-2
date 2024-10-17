#create personnel dictionary (key: value)
personnel = {
    "Manager": "Mary Smith",
    "Assistant Manager": "John Samuels",
    "Driver": "Linda Johnson"
 }

print("Employee Search ---")
print("Enter Position: ",end="")
for p in personnel: #display possible job descriptions
    print(p + ", ",end="")
print()

searchPosition = input("Which position are you looking for? ") #get position to search for
print("The job of " + searchPosition + " is held by " + personnel[searchPosition]) #display matching employee