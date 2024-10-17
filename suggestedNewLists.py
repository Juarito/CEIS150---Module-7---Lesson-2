employee = ["Mary Smith", "John Samuels", "Linda Johnson"]  # create employee name list
jobDescription = ["Manager", "Assistant Manager", "Driver"]  # create job description list

print("Employee Search ---")
print("Enter Position:", end=" ")  # corrected syntax for end

for i in range(3):  # display possible job descriptions
    if i < 2:
        print(jobDescription[i] + ",", end=" ")  # print each job with a comma
    else:
        print(jobDescription[i])  # no comma for the last item

searchPosition = input("Which position are you looking for? ")  # get position to search for

found = False  # flag to track if position is found

for i in range(3):  # search list for job description
    if jobDescription[i] == searchPosition:  # if found
        print("The job of " + searchPosition + " is held by " + employee[i])  # display employee for that position
        found = True

if not found:  # if the position was not found
    print("No employee found for that position.")
