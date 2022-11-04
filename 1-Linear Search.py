def LinearSearch(myList,key):
    found = -1
    for i in range(0,len(myList)):
        if myList[i] == key:
            found = i
    return found

myList = []
n = int(input("Enter number of elements in the List:\n"))
for j in range(0,n):
    element = int(input("Input elements: \n"))
    myList.append(element)
print("Your list is "+str(myList))

key = int(input("Enter the value of the element you'd like to search for\n"))
result = LinearSearch(myList,key)

if result < 0:
    print("Element has not been found")
else:
    print(str(key)+" has been found in the "+str(result+1)+"th position")