"""a='name'
b="divya"
c=a+b
print(c)   """

"""str="python"
print(str[1:5])
print(str[0:6])
print(str[0:5])
print(str[:5])
print(str[:])
print(str[0:3:5])
print(len(str))   """

"""set={1,2,3,4}
for x in set:
    print(x,end=" ")

def findSum(a,b):         # function definition
    result =a+b
    return result

x=5
y=7
z=findSum(x,y)            # function call
print(z) 

def my_function(fname,lname):
    print(f"first name is {fname} and last name is {lname}")
my_function(lname="Singh",fname="Divya")  """

"""def sum_num(num1,*num):
    result = num1
    for i in num:
        result +=i
    return result
r=sum_num(10,20,30)
print(f"sun of num is: ",(r))

r=sum_num(10,20,30,40,50)
print(f"sun of num is: ",(r))

result=lambda num1,num2,num3: num1+num2+num3
print(result(10,20,30))
print(result(1,5,6))   """

"""nums=[1,2,3,4,5,6,7,8,9,10]
def is_even(n):
    if n%2==0:
        return True

even_nums=filter(is_even,nums)

even_nums_list=list(even_nums)

print(even_nums_list)   

age=[5,18,23,25,74,85,12,65]
adults=list(filter(lambda x: x>18,age))
print(adults)    

from functools import reduce
num_list=[20,12,52,22,72,19,7]
min=reduce(lambda x,y:x if x<y else y,num_list)
total_sum=reduce(lambda x,y:x+y,num_list)
print(min)
print(total_sum) 

def generate_report(name,marks,subject="Python"):
    average=sum(marks)/len(marks)
    grade="A"if average>=90 else "B"if average>=75 else "C"
    print(f"{name}'s {subject} bReport\nMarks: {marks}\nAverage: {average}\nGrade:{grade}\n")
generate_report("Divya",[95,94,90]) """

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print("fact=",fact(5))