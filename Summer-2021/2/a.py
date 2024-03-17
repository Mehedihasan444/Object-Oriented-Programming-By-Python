# name=input("Enter your name: ")
# father_name=input("Enter your father name: ")
# mother_name=input("Enter your mother name: ")
# phone_number=input("Enter your phone number: ")
# info=[]
# info.insert(0,name)
# info.insert(1,father_name)
# info.insert(2,mother_name)
# info.insert(3,phone_number)
# n_char=0;n_vow=0
# for i in info:
#     n_char += len(i)
#     for v in 'aeiou':
#      if v in i.lower():
#         n_vow += 1

# print(n_char)

# print(n_vow)
name = input("Enter your name: ")
father_name = input("Enter your father's name: ")
mother_name = input("Enter your mother's name: ")
phone_number = input("Enter your phone number: ")

info = [name, father_name, mother_name, phone_number]

n_char = 0
n_vow = 0

for i in info:
    n_char += len(i)
    for vowel in 'aeiou':
        if vowel in i.lower():
            n_vow += 1

print("Total number of characters:", n_char)
print("Total number of vowels:", n_vow)
