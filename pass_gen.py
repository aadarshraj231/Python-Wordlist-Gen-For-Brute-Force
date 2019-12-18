import os
os.path.abspath(__file__)
import sys
import random
from utilitybelt import change_charset

origspace="abcdefghijklmnopqrstuvwxyz"
keyspace="abcd3fgh1jklmnopqr57uvwxyz"

pass_len=int(input("Enter Password Length : "))
too_pass=int(input("How Many Combinations : "))

first_name=input("Enter Your name : ")
first_name=change_charset(first_name,origspace,keyspace)
last_name=input("Enter you last name : ")
age=int(input("Enter your age : "))
dob=int(input("Enter your DOB: "))
pet_name=input("Enter you pet name : ")
surname=input("Enter your surname : ")
surname=change_charset(surname,origspace,keyspace)


all_1=first_name + last_name
all_2=first_name + surname
all_3=first_name + str(dob) + pet_name
all_4=first_name + str(age)
all_5=surname + first_name



for p in range(too_pass):
    pass_long=""
    for i in range(pass_len):
        pass_long+=random.choice(all_1)
    print(pass_long)

for p in range(too_pass):
    pass_long=""
    for i in range(pass_len):
        pass_long+=random.choice(all_2)
    print(pass_long)

for p in range(too_pass):
    pass_long=""
    for i in range(pass_len):
        pass_long+=random.choice(all_3)
    print(pass_long)


for p in range(too_pass):
    pass_long=""
    for i in range(pass_len):
        pass_long+=random.choice(all_4)
    print(pass_long)

for p in range(too_pass):
    pass_long=""
    for i in range(pass_len):
        pass_long+=random.choice(all_5)
    print(pass_long)



print("Thank You")



