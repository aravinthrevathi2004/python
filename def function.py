# def function


# 1-calculate square:
# def square(x):
#     return x * x


# print(square(2))


# 2-calculate area of rectangle
# def rectangle(length, breath):
#     return length * breath


# print(rectangle(5, 3))

# 3-check even or odd


# def check_even_odd(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# print(even_odd(2))
# print(check_even_odd(6))
# print(check_even_odd(7))
# print(check_even_odd(8))
# print(check_even_odd(9))

# 4-calculate factorial

# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(3))

# 5-check prime number

# def prime(num):
#     if num%2==0 or num%3==0 or num%5==0:
#         print("not a prime number.")
#     else:
#         print("prime number.")
# print(prime(632))

# 6-reverse a string

# def reversestring(s):
#     return s[::-1]
# print(reversestring("pondicherry"))

# 7-count characters:

# def countchar(x):
#     return len(x)
# print(countchar("aravinth"))

# 8-sum of squares:

# def sum_squares(x,y,z):
#     return x**2+y**2+z**2
# print(sum_squares(2,3,4))

# 9-check palindrome:

# def palindrome(name):
#     return name==name[::-1]
# print(palindrome("12325"))

# 10-caculate fibonacci
# def fibonacci(n):
#     num1 = 0
#     num2 = 1
#     next_number = num2
#     count = 1
#     while count <= n:
#         print(next_number,end="")
#         count += 1
#         num1, num2 = num2, next_number
#         next_number = num1 + num2
#         print()
# print(fibonacci(5))

# 11-check armstrong number

# def armstrong(n):
#     sum=0
#     temp=n
#     while temp>0:
#         num=temp%10
#         sum=sum+temp**3
#         num=temp//10
#     if n==sum:
#         print("it is armstrong number.")
#     else:
#         print("not a armstrong number.")


# print(armstrong(153))

