# 1-square all numbers in list

# mylist=[2,3,4,5,6]
# def square(n):
#     return n**2
# result=map(square,mylist)
# print(list(result))

# 2-convert all string in a list to uppercase:

# name="pondicherry"
# def string(n):
#     return n.upper()
# res=map(string,name)
# print(list(res))

# 3-add 10 to each number in a list

# mylisyt=[2,3,4,5,6,7]
# def add(n):
#     return n+10
# res=map(add,mylisyt)
# print(list(res))

# 4-double each number in a list

# mylisyt = [2, 3, 4, 5, 6, 7]
# def double(n):
#     return n+n
# res=map(double,mylisyt)
# print(list(res))

# 5-capitalize the first letter 0f each string ina list

# name=["wellcome","to","pondicherry"]
# def string(n):
#     return (n.capitalize())
# res=map(string,name)
# print(list(res))

# 6-filter out even numbers from a list

# mylist=[2,3,4,5,6,7,8,9,10]
# def even_number(n):
#     return n%2==0
# res=filter(even_number,mylist)
# print(list(res))

# 7-filter out words shorter then 4 characters
# name=["apple","home","orange","come","what"]
# def short(n):
#     return len(n)<=4
# res=filter(short,name)
# print(list(res))

# 8-filter out numbers that greater then 10:

# mylist=[4,12,5,31,6,3,4,543,66,3322]
# def greater(n):
#     return n>10
# res=filter(greater ,mylist)
# print(list(res))

# 9-filter out strings containninga the letter "a":

# name = ["apple", "home", "orange", "come", "what"]
# def letter(n):
#     return "a" in n
# res=filter(letter,name)
# print(list(res))

# 10-filter out number that are not diviible by 3:

# mylist=[2,3,5,6,8,9,11,15,19]
# def number(n):
#     return n%3!=0
# res=filter(number,mylist)
# print(list(res))

# 11-filter out negative number from a list:

# mylist = [2,3,-5,6,8,-9,11,-15,-19]
# def number(n):
#     return n<0
# res=filter(number,mylist)
# print(list(res))


# 12-filter out number that are not diviible by 3:

# mylist=[2,3,5,6,8,9,11,15,19]
# def number(n):
#     return n%3!=0
# res=filter(number,mylist)
# print(list(res))

# 13-find the product of all number in a list
# import functools
# mylisyt = [2, 3, 4, 5, 6, 7]
# def number(x,y):
#     return x*y
# res=functools.reduce(number,mylisyt)
# print(res)

# 14-concatenate a list of strings

# name = ["wellcome", "to", "pondicherry"]
# import functools
# def concate(x,y):
#     return x+" "+y
# res=functools.reduce(concate,name)
# print(res)

# 15-find the maximum number in a list

# import functools
# mylist = [2, 3, 4, 5, 6, 7]
# def number(a,b):
#     # return (a.max())
#     if a>b:
#        return a
#     elif b>a:
#        return b
# res=functools.reduce(number,mylist)
# print(res)

# 16-compute the sum of square of number in a list
# import functools
# mylist = [2, 3, 4, 5]
# def sum(a,b):
#     return a+b**2
# res=functools.reduce(sum,mylist)
# # res=map(sum,mylist)
# print(res)

# 17-compute the factorial of a number using reduce
# import functools
# n=5
# factorial=1
# def number(n):
#     return n*factorial(n-1)
# res=functools.reduce(number,n)
# print(res)