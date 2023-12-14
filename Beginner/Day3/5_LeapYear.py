
year = int(input('Enter a year: '))
# 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, and 2048

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")


if year%4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else: print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")