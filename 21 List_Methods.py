numbers=[5,2,1,5,7,4]
numbers.append(20) # adds 20 at the end of the list
print(numbers)
numbers.insert(0,10) # adds 10 at index 0
print(numbers)
numbers.remove(5) # removes 5 from the list
print(numbers)
numbers.pop() # removes the last element from the list
print(numbers)
numbers.index(7) # returns the index of element 7
print(numbers.index(7))
print(50 in numbers) # checks if 50 is in the list, returns True/False
print(numbers.count(5)) # counts how many times 5 appears in the list
numbers.sort()
print(numbers)
numbers.reverse()  
print(numbers)
numbers.clear() # removes all elements from the list

print(numbers)
