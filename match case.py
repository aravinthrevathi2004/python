# 1-check a day as weekday or weekend

# week=input("enter the day:")
# match week:
#     case "monday"| "tuesday"|"wednesday"|"thursday"|"friday":
#         print("the day is a weekday.")
#     case "saturday"|"sunday":
#         print("the day is weekend.")
#     case _:
#         print("enter the day.")


# 2- print a no of days in a month


# name=input("enter the month:")
# match name:
#     case "january"|"march"|"may"|"july"|"august"|"october"|"december":
#         print("31 days in a month.")
#     case "april"|"june"|"septemper"|"october"|"november":
#         print("30 days in a month.") 
#     case "february":
#         print("28 days in a month.")
#     case _:
#         print("enter the month.")   


# 3-print a entered input is vowel or constants



# name=input("enter the letter:")
# match name.lower():
#     case "a"|"e"|"i"|"o"|"u":
#         print("it is vowel.")
#     case "b"|"c"|"d"|"f"|"g"|"h"|"j"|"k"|"l"|"m"|"n"|"p"|"q"|"r"|"s"|"t"|"v"|"w"|"x"|"y"|"z":
#         print("it is constants.")
#     case _:
#         print("please entered the letters.")


# 4-grade by percentage


# grade=input("enter the mark:")
# match grade:
#     case grade if grade>=90 and grade<=100:
#         print("the grade is A")
#     case grade if grade>=70 and grade<90:
#         print("the grade is B")
#     case grade if grade>=50 and grade<70:
#         print("the grade is C")
#     case _:
#         print("the result is fail")


# 5-season based on month name


# name=input("enthe the month:")
# match name:
#     case "january" | "february" | "december":
#         print("the season is winter.")
#     case "march" | "april" | "may":
#         print("the season is spring.")
#     case "june" | "july" | "august":
#         print("the season is summer.")
#     case "septemper" | "october" | "november":
#         print("the season is fall or autumn.")
#     case _:
#         print("enter the month.")


# 6-positive or negative


# num=int(input("enter the number:"))
# match num:
#     case num if num>0:
#         print("the number is positive.")
#     case num if num<0:
#         print("the number is negative.")
#     case _:
#         print ("it is zero.")

# 7-range of number


# num=int(input("enter the number:"))
# match num:
#     case num if num>0 and num<10:
#         print("the number is lies between 0-10.")
#     case num if num>11 and num<20:
#         print("the numer is lies between 11-20.")
#     case num if num>21 and num<30:
#         print("the number lise between 21-30.")
#     case num if num >31 and num<40:
#         print("the number is lies between 31-40.")
#     case num if num>41 and num<50:
#         print ("the number is lies between 41-50.")
#     case _:
#         print("enter th correct number.")