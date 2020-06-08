a = input()
list_a = list(a)

#this prints a list of strings
#print(list_a)

for i in range(0, len(list_a)):
    list_a[i] = int(list_a[i])

#this prints a list of ints
#print(list_a)

list_b = []
i = 0
j = 0
for name in list_a:
    list_b.append(list_a[i] + j)
    j += list_a[i]
    i += 1

print(list_b)
