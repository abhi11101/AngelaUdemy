totalNum = int(input("Enter total Num\n"))
data =[]
for i in range(0,totalNum):
    data.append(int(input("Enter Number ")))

print(data)

max = data[0]

for i in data:
    if max < i:
        max = i

print(f"Max Number is {max}")