x = lambda a :  a+15

print("Result:",x(15))

print("------------------------------")

def my_function():
    print("Hello World!!")
    
my_function()

print("------------------------------")

def new_function(fname,):
    print(fname + " " + "Kumar")
    
new_function("Mohan")

print("------------------------------")


x = lambda a , b , c :a+b+c
print("Result: ",x(5,5,5))

print("------------------------------")

a = 5
print(a)
print(type(a))
aa = str(a)
print(aa)
print(type(aa))

my_list = [1,2,3,4]
print(type(my_list))
print(my_list)
my_tup = (1,1,2,2,3,3)
print(my_tup)
mm = list(my_tup)
print(mm)
mm[0] = 6
print(mm)
my_tup = tuple(mm)
print(my_tup)

