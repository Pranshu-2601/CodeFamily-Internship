#1 lowercase letter into Uppercase letter and vice versa

s = input("Enter a string:")
new_str = ""
for i in range(len(s)):
    if len(s) < 1000:
        if s[i].isupper():
            new_str += s[i].lower()
        elif s[i].islower():
            new_str += s[i].upper()
        else:
            new_str += s[i]
    else:
        print("String Length not valid")
print(new_str)


#2 capitalise first two character of the string

s = input("Enter a string:")
lst = [word[0].upper() + word[1].upper() + word[2:] for word in s.split()]
s = " ".join(lst)
print("The Capitalized String is:", s)


#3 Print the given names in a specific format in descending order

import pprint
test_dict = {}
size = int(input("Enter the number of elements: "))

for i in range(size):
    dict_name = input("Enter the name : ")

    test_dict[dict_name] = {}
    Age = input("Enter Age: ")
    city = input("Enter city: ")
    sex = input("Enter sex: ")
    test_dict[dict_name]["Age"] = Age
    test_dict[dict_name]["City"] = city
    test_dict[dict_name]["Sex"] = sex
print("Sorted data:")
pprint.pprint(sorted(test_dict.items(), key=lambda x: x[1]['Age'], reverse=True))







