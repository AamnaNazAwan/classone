                   #TUPLE
numbers = (1,2,3,4,5)
print(numbers)

              #TUPLE OPERATIONS
#TUPLE CONCATENATION
my_tuple_1 = (1,2,3)
my_tuple_2 = (4,5,6)
combined_tuple = my_tuple_1 +my_tuple_2
print(combined_tuple)

#ACCESSING ELEMENTS
print(my_tuple_1[0])

#REPEATITION
repeated_tuple = my_tuple_1*2
print(repeated_tuple)

#SLICING THE TUPLE
sliced_tuple = combined_tuple[1:4]
print(sliced_tuple)

#COUNT THE VALUES IN TUPLE
tuple_one = (1,2,3,4,3,2)
print(sliced_tuple)
count = repeated_tuple.count(3)
print(count)

#CREATING A TUPLE
person = ("Alison", 30, "Engineer")

#ACCESSING ELEMENTS
name = person[0]
age = person[1]
profession = person[2]

#CONCATENATION
person_with_address = person + ("Newyork",)

#REPEATITION
double_person = person * 2

#SLICING
slice_of_person = person[1:3]

#USING TUPLE METHODS
occurances_of_30 = person.count(30)
index_of_engineer = person.index("Engineer")

#PRINTING RESULTS
print(name)
print(age)
print(profession)
print(person_with_address)
print(double_person)
print(slice_of_person)
print(occurances_of_30)
print(index_of_engineer)


