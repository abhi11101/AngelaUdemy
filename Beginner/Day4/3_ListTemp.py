
listOfStates = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA"]
print(listOfStates[0:])
print(listOfStates)
print(listOfStates[1])
print(listOfStates[-1])
print(listOfStates[2])
print(listOfStates[-2])

listOfStates.insert(1,"New")

print(listOfStates)
value = listOfStates.pop()
print(value)
print(listOfStates)

listOfStates.append("Last")
print(listOfStates)

listOfStates.extend(["NewLast", "Last2"])
print(listOfStates)

listOfStates.remove("CO")
print(listOfStates)
