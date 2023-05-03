####break
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']
for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] == 'Guru':
        print('Found the name Guru')
        break
        print('After break statement')
print('Loop is Terminated')
print()

for i in range(4):
    for j in range(4):
        if j==2:
            break
        print("The number is ",i,j);


####continue
n=100
for i in range(n):
    if i>20 and i<50:
        continue
    print(i)

###pass
print()
n=100
for i in range(n):
    if i>20 and i<50:
        pass
    print(i)

print()
for i in range(10):
    if i == 7:
        pass
    print("The Number is :" , i)