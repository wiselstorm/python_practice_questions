list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
list3=[]

for x in list1:
    if x%2!=0:
        list3.append(x)

for y in list2:
    if y%2==0:
        list3.append(y)


print(list3)