#copyright@2019
#Dont Redistribute without Cedits
#--------------intro
#means commenting code
"""
multiline commenting
"""
print("hello Geek")
print("i'm "prasoon"")#error
print("i\'m \"prasoon\"" )#escape character 
print("""\
      hello:
          user defined look
          """)
print("c:\number\me")
print("c:\\number\\me")

#you can use either ' or "  to denote a string 

#to check which type
type(2)
type(3.2)
type('abc')
type(True)

#--------------variable
a=2
b=2.4
c="word"
sum=a+b
print(a)
print(b)
print(c)
print(a+b)
print(sum)

2**5 #exponent means 2*2*2*2*2

# order of execution () ** * / % + -
# for clear screen 
"""import os 
clear = lamda:os.system('cls')
clear()
"""
#--------------string handling 
p="prasoon"
print(p)
print(len(p))
print("con"+"catination")
a ="w"
b="ord"
print(a+b)
print("L"+b)
print("2"+b[1:])

#--------------logic operator and conditional statement <,>,<=,>=,!=,==
print(5<8)
print(5==11)
print(5==5)
print(8!=12)
print("abc"=="abc")
a=True
b=False
print(not a)
print(a and b)
print(a or b)
#-------------- Branching in Python
a = 40
b = 300
if b > a:
  print("b is greater than a")
#--
a = 4
b = 4
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#--
a = 400
b = 100
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#-------------- loop in python
#(while)
count = 0
while (count < 3):     
    count = count + 1
    print("Hello Geek") 
count = 0
#--

while (count < 3):     
    count = count + 1
    print("Hello Geek") 
else: 
    print("your In Else Block")
#--
for i in range(0,10):
    print(i)
#--
for i in range(0,10,2):
    print(i)
    
#"This Is List Iteration 
l = ["your","will","be","a","machine"," learning","expert","soon"] 
for i in l: 
    print(i)

#This IsTuple Iteration 
t = ("your","will","be","a","machine"," learning","expert","soon") 
for i in t: 
    print(i) 
#String Iteration  
s = "machinelearning"
for i in s : 
    print(i) 
#-------------- function
"""syntax
def functionname( parameters ):
   "function_docstring"
   body of function
   return [expression]"""

def greeting(name):
	print("Hello, " + name + ". Good morning!")
 # function calling 
greeting("prasoon")
