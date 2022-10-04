beseda=input("Type a string\n")
array_even_characters=[]
array_odd_characters=[]
for char in beseda:
    if (ord(char)%2==0): #if char ascii value division remainder by 2 is 0,append it to following array
        array_even_characters.append(char)

    else:
        array_odd_characters.append(char)

print("Even characters are: ",array_even_characters)
print("Odd characters are: ",array_odd_characters)