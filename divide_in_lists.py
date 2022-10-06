l=[]
results=[]
maximum_input=int(input("Vnesi stevilo vnosov"))
divide=False
for i in range (0,maximum_input):

    l.append(int(input("Enter a number")))
    if l[i]%5!=0: #if an element is not divisible by 5 divide becomes false
        divide=False


    else: #initiate when element is divisible by 5 divide becomes true
        divide=True
        results.append(l[i])#appending our results into a list
    print(divide)

print (results)