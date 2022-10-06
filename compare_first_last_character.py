import numpy as np #imported library for math with arrays
tab_a=np.array([10,20,30,40,10]) #creation of array
boolean_value=False #boolean value to determine status of variable(true/false)
first_var=tab_a[0] #gets the first element of array which is 10
last_var= tab_a[len(tab_a)-1]   #gets the last character of the program by substracting -1 from array
print(first_var)
print(last_var)
if first_var==last_var: #if first element in list is equal to last print true
    boolean_value=True
    print("True")

else: #print false
    boolean_value=false
    print("False")

