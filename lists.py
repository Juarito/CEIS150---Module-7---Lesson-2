employee = ["Mary Smith", "John Samuels","Linda Johnson"] #create employee name list
jobDescription = ["Manager", "Assistant Manager","Driver"] #creat job description list

print("Employee Search ---")
print("Enter Position: ",end="")
for i in range(3): #display possible job descriptions
    print(jobDescription[i]+", ",end="")
print()
searchPosition = input("Which position are you looking for? ") #get position to search for

for i in range(3): #search list for job descprition
    if jobDescription[i] == searchPosition: # if found
        print("The job of"  + searchPosition +" is held by "+employee[i]) #display employee for that position

