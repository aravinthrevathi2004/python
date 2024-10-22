# list:
# >> multiple items store in  single variable
# >> ordered , changable, allow duplicate values




# name=["apple","orange","tree",1,2,5,7,"true","false"]
# print(type(mylist))

# name=list(("apple","orange","tree",1,2,5,7,"true"))
# print(type(name))
# print(len(name))           ------lenth
# print(name[2])             ------index

# mylist=["apple","orange","tree",1,2,5,7,"true","false"]

# print(mylist[1:5])        ------postive index
# print(mylist[4:])
# print(mylist[:4])
# print(mylist[-7:-4])       -------negative index
# print("aravinth" in mylist)   


# mylist[4]="bee"
# print(mylist)

# mylist.insert(5,"python")        -------insert 
# print(mylist)
 
# mylist.append("python")          --------append
# print(mylist)

# mylist=["apple","orange","tree",1,2,5,7,"true","false"]
# new=(1,3,5,7)
# mylist.extend(new)              -----------extend
# print(mylist)

# mylist.remove("tree")         -----------------remove
# print(mylist)

# mylist.pop()
# print(mylist)                  ----------------pop(delete)

# del mylist()
# print(mylist)                   ----------------del(delete all input with syntax error)

# mylist.clear()
# print(mylist)                 --------------clear(clear all input without error)

# loop

# mylist=["apple","orange","tree",1,2,5,7,"true","false"]

# for i in mylist:
#     print(i)

# for i in range(len(mylist)):
#     print(mylist[i])

# num=[4,6,2,-1,5,-4,9,-4,0]
# num.sort()                   -------------ascending
# print(num)
 
# num.sort(reverse=True)
# print(num)                   --------------descending

# mylist=["apple","orange","tree",1,2,5,7,"true","false"]
 
# mylist.copy()               --------------copy
# print(mylist)

# mylist=["apple","orange","tree",1,2,5,7,"true","false"]
# new=[1,3,5,7]

# res=mylist+new
# print(res)
# res=[]
# for i in new:
#     res.append(i)
#     print(i)

# task:

# task:

# 1-in a list of array store even or odd numbers in new list and print

# mylist=[1,2,3,4,5,6,7,8,9]
# even_number=[]
# odd_number=[]
# for i in mylist:
#     if i%2==0:
#         even_number.append(i)
#     elif i%2!=0:
#         odd_number.append(i)
# print(odd_number,"odd number")
# print(even_number,"even number")

# 2-print sum of list

# mylist=[1,2,3,4,5]
# sum=0
# for i in mylist:
#          sum=sum+i
#          print(sum)
        
# 3-product of list when zero in list it cant product that number

# mylist=[1,2,3,0,4,5,8]
# product=1
# for i in mylist:
#     if i==0:
#         continue
#     else:
#         product*=i
# print(product)

# 4-find duplicate element in a array and print in new array

# name=["apple","orange","graphs","apple","banana"]
# new=[]
# for i in name:
#     if name.count(i)>1:
#         new.append(i)
# print(new)


# 5-largest and smallest number in a list

# mylist=[2,3,6,4,8,4,3]







# 6-reverse a list

# mylist=[2,3,6,4,8,4,3]
# mylist.sort(reverse=True)
# print(mylist)