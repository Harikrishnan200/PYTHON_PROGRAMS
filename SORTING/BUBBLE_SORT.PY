list = []
num = int(input("Enter the number of elements:"))
print("Enter  the numbers one by one:")
for i in range(num):
    list.append(int(input()))

print("unsorted list:",list)

for i in range(len(list)-1,0, -1):
    for j in range(i):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]

print("sorted list:",list)