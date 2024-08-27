import math

pi = -3.14

x ,y,z = 10,20,30
print(round(pi))
print(math.sqrt(25))
print(math.ceil(pi))
print(abs(pi))
print(pow(42,2))
print("Maximum value of x,y,z = ",max(x,y,z))
print("Minimum value of x,y,z = ",min(x,y,z))

#Write a python program sting slicing.

name = "This is india"

first_name = name[0:-1]
print(first_name)

import random

aa = random.randint(1,6)

print(aa)

import numpy as np

new_arr = np.array([[1,2,3],[4,5,6]])
print(new_arr)
print("Result: ",new_arr[1,2])

arr = np.zeros(5)
print(arr)

app = np.zeros((4,5))
print(app)

aaa = np.ones(6)
print(aaa)

abb = np.ones((7,8))
print(abb)

#Write a numpy python program 
first_fill_array = np.empty(10,dtype=int)
first_fill_array.fill(12)
print(first_fill_array)

#Write a numpy python program 
first_full_array = np.full(5,10)
print(first_full_array)

#Write a numpy python program 

second_full_array = np.full((4,5),8)
print(second_full_array)