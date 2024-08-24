#Write a program with use of defination in python.
def my_fun():
    print("My name is Laxman learning python and FastAPI")
my_fun()

# Write a python program with use def key.

def my_fun_details(fname,lname):
    print(fname + " " + lname)


my_fun_details("Kadhambala","Laxman")
my_fun_details("Kadhambala","Suma")
my_fun_details("Kadhambala","Kavya")
my_fun_details("Kadhambala","Nihal") 

# Write a python program with use def key.
print("##"*20)
def my_fun_details(fname):
    print(fname +" " + "Laxman")
    
my_fun_details("Kadhambala")
my_fun_details("Suma")

#Arbitrary Keyword Arguments, **kwargs

def my_new_function(**kid):
    print("His name is "+ kid["lname"])
    
my_new_function(fname = "Nemalapuri" , lname = "Sathish")

print("/"*100)

#Passing a List as an Argument

def my_function_new(food):
    for i in food:
        print(i)
    
fruits = ["Apple","Orange","Grapes"]
grosers = ["Atta","Maida","Rice"]
my_function_new(fruits)
my_function_new(grosers)

print("@"*20)
#Adding two numbers

def add(x,y):
    return x + y

result = add(25,65)

print("Adding two number result:",result)

print("$"*25)

#Return value.
def my_funtion(x):
    return 5 * x

print("Result:",my_funtion(3))


