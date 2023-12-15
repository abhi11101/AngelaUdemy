programming_dictionary = {
    "Key1": "Data1",
    "Key2": "Data2",
    "Key3": "Data3"
}

print(programming_dictionary)

programming_dictionary["Key4"] = "Data4"
print(programming_dictionary)
print(programming_dictionary["Key2"])

for i in programming_dictionary:
    print(i)
    print(programming_dictionary[i])
