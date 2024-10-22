# ----------global variable-------------
# name="aravinth"
# print(name)

# def globalfun():
#     print(name)
# globalfun()
# print(name)


# -----------local variable----------


# def localfun():
#     name="aravinth"
#     print(name)
# localfun()




# def greeting(*arg):              (non keyword arguments-no of arguments , input-tuple)
#     for i in arg:
#         print(i)
# greeting("all", "are", "best")

# def greeting(*arg):
#     for i in arg:
#         print(i)

# greeting("hello","welcome","to","home")




# def student(**stu):                            (keyword argument- no of argument,input-dictionary)
#     for i,j in stu.items():
#         print(i,j)
# student(name="aravinth",age="20",place="pondy")



# task:

# 1-sum of all arguments:

# def sum_arg(*arg):
#     sum=0
#     for i in arg:
#         sum+=i
#         print(sum)
# print(sum_arg(1,3,2,5))

# 2-multiply all arguments

# def multiply_arg(*arg):
#     multiply=1
#     for i in arg:
#         multiply*=i
#         print(multiply)
# print(multiply_arg(3,4))

# 3-concatenate all arguments:

# def concatenate(*arg):
#     for i in arg:
#         print(i,end=" ")
# print(concatenate("they","are","going","to","temple"))

# 4-print arguments and keywords:

# def arg_key(**arg):
#     for i,j in arg.items():
#         print(i,j)
# print(arg_key(name="aravinth",age="20",place="pondy"))