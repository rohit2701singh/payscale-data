number = int(input("how many star: "))

# method 1
number_list = []
for i in range(1, number+1):
    number_list.append(i)
print(number_list)

for i in number_list[::-1]:
    print("*" * i)
    if i == 1:
        for num in number_list[1:]:
            print("*" * num)

# method 2
for i in range(number, 0, -1):
    print("*"*i)
    if i == 1:
        for num in range(2, number+1):
            print("*" * num)
