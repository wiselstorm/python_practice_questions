a=[] #data where to store the numbers
i=0 #counter of current number
current=0 #current for-generated number
previous=0 #previous for-generated number
next=0 #next for-generated number
sum=0 #sum of current and previous number, which is our desired output.first we must declare sum to be 0
for i in range(0,10): #iteration through the numbers
    a.append(i) #adds number to array so we can do maths with it
    current=a[i]
    l = len(a) #calculates lenght of our array
    previous=a[(i+l-1)%l]
    next=a[(i+1)%l]
    sum=current+previous
    print("Current number: ",i,"Previous number: ",previous,"Sum:  ",sum)


