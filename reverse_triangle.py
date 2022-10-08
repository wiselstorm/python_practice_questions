rows=6
i=0 #i is a number for rows
r=0 #variable that calculates the amount of spaces
j=0 #number for columns
while i<rows:
    i=i+1
    r=rows-i
    while r>0:
        r = r - 1
        print('  ', end="") # prevent the default \n


        j=i
    while j>0:
        j = j - 1
        print("*",end=" ") # add a space after each *

    print() # print new line