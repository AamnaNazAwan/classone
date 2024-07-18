print("hello world")
                           #LISTS
numbers = [1,2,3,4,5]

#ACCESSING ELEMENTS
print(numbers[0])
print(numbers[1])

#MODIFYING NUMBERS
numbers[0] = 10
print(numbers)

#ADDING ELEMENTS
numbers.append(6)
print(numbers)

#ADDING ELEMENTS BY INDEX
numbers.insert(2,9)
print(numbers)

#ADDING MORE THAN ONE VALUES
numbers.extend([1,2,3,4,5])
print(numbers)

#REMOVING ELEMENTS
numbers.remove(3)
print(numbers)

#REMOVING BY INDEX
del numbers[1]
print(numbers)

#SORTING THE NUMBERS IN LIST(ASSENDING ORDER)
numbers.sort()
print(numbers)

#REVERSING THE NUMBERS IN LIST(DESENDING ORDER)
numbers.reverse()
print(numbers)

#SLICING THE LIST
print(numbers[1:7])

print(numbers)