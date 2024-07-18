                    #SETS
my_sets = {1,2,3,4}
print(my_sets)

another_set = set([1,2,3])
print(another_set)

#ADDINNG AND REMOVING IN SET
my_sets.add(4)

my_sets.remove(2)

my_sets.discard(1)

print(my_sets)

#CREATING SETS
set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8}

#ADDING ELEMENTS
set_1.add(6)
print(set_1)

#REMOVING ELEMENTS
set_1.remove(2)
print(set_1)

                    #SET OPERATIONS
#UNION
union = set_1|set_2
print("union",union)

#INTERSECTION
intersection = set_1 & set_2
print("intersection",intersection)

#DIFFERENCES
difference = set_1 - set_2
print("diffeerence",difference)

#SYMMETRIC DIFFERENCE
symmetric_difference = set_1 ^ set_2
print("symmetric difference",symmetric_difference)

#METHODS
is_member = 3 in set_1
print(is_member)

set_length = len(set_1)
print(set_length)

set_1.clear()
print(set_1)


