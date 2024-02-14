# Create an Empty Dictionary
my_dict = {}

#use prompt to get user input to ask for the user's name and age and assign it to the dictionary
my_dict['name'] = input("What is your name? ")
my_dict['age'] = input("What is your age? ")

# Print the dictionary
print(my_dict)

#use prompt to get user input to ask for the user's favorite color and food and assign it to the dictionary
my_dict['favorite_color'] = input("What is your favorite color? ")
my_dict['favorite_food'] = input("What is your favorite food? ")

#use update to change the value of the key 'age' to age +1 in multiple steps 
my_dict['age'] = int(my_dict['age']) + 1
my_dict.update({'age': my_dict['age']})

#get the value of the key 'age' and assign it to a variable
new_age = my_dict['age']
#increment the value of the variable by 1
new_age += 1
#update the value of the key 'age' with the new value of the variable
my_dict['age'] = new_age
#Remove name by key and return its value into a variable
name = my_dict.pop('name')
#make new dictionary with the key from name variable and a nested dictionary holding the rest of the attributes
new_dict = {name: my_dict}
#Print the new dictionary
print(new_dict)

#print the keys of the new dictionary
print(new_dict.keys())
#print the values of the new dictionary
print(new_dict.values())
#print the items of the new dictionary
print(new_dict.items())
#print the length of the new dictionary
print(len(new_dict))
#check if users name exists in the new dictionary
exists = name in my_dict
print(f"{name} exists:", exists)






