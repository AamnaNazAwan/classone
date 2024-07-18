                  #DICTIONARY
#CREATING DICTIONARY USING CURLY BRACKETS
my_dict = {'name':'Alison', 'age': 30, 'proffession':'Engineer'}
print(my_dict)

#CREATING DICTIONARY USING dict() CONSTRUCTOR
another_dict = dict(name = "bob",age = 25,proffesssion = "Doctor")
print(another_dict)

#ACCESSING VALUES
name = my_dict["name"]
age = my_dict["age"]
print(name)
print(age)

#ADDING A NEW KEY VALUES
my_dict["city"] = "Newyork"
print(my_dict)

#UPDATING AN EXISTING VALUE
my_dict["age"] = 31
print(my_dict)

#REMOVING A KEY-VALUE PAIR USING del
del my_dict["proffession"]
print(my_dict)

#REMOVING A KEY-VALUE PAIR USING POP()
age = my_dict.pop("age")
print(my_dict)
print(age)

my_dict = {"name":"Alice", "age":30, "proffession": "Engineer"}

#KEYS() METHOD RETURNS A VIEW OBJECT THAT DISPLAYS A LIST OF ALL KEYS IN THE DICTIONARY
keys = my_dict.keys()
print(keys)

#VALUES() METHOD RETURNS A VIEW OBJECT THAT DISPLAYS A LIST OF ALL KEYS IN THE DICTIONARY
values = my_dict.values()
print(values)

#ITEMS() METHOD RETURNS A VIEW OBJECT THAT DISPLAYS A LIST OF ALL KEYS IN THE DICTIONARY
items = my_dict.items()
print(items)

#GETS() METHOD RETURNS THE VALUE FOR THE SPECIFIED KEY IF KEY IS IN THE DICTIONARY
name = my_dict.get("name")
print(name)

#UPATE() METHOD UPDATES THE DICTIONARY WITH ELEMENTS FROM ANOTHER DICTIONARY OBJECTS
my_dict.update({"age": 31, "city": "Newyork"})
print(my_dict)

#CLEAR () METHOD REMOVES ALL ITEMS FROM THE DICTIONARY
my_dict.clear()
print(my_dict)