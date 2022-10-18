import math
number=7536
results=[]
int_size=0
size_of_digits=0
calculation=0

size_of_digits=math.log10(number)
int_size=int(size_of_digits) #in this case the result should be 3

for i in range(int_size+1) : #we need to do this so it ranges to the full size of our number which is 4
    calculation=number%10
    number=number/10
    number=int(number)
    results.append(calculation)
    print(calculation,end=" ")
print(results)
