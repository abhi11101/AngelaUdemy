import random

names = ["Micheal","Jim", "Pam","Kevin", "Dwight"]

chosen = random.choice(names)

print(f"{chosen} will pay the bill")



names = input("Give me names with comma-separated\n")

names = names.split(',')
print(names)

randomName = random.randint(0,len(names)-1)
print(f"{names[randomName]} will pay the bill")
