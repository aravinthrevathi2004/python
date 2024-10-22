# dictionaries:
# >> it is orderd,changable,and do bot allowed duplicate values.
# >> it is declared by cursive bracket{}.

# mydict={"name":"aravimth","age":"20","place":"pondy"}
# print(type(mydict))
# mydict=dict(name="aravimth",age="20",place="pondy")
# print(type(mydict))

# mydict={"name":"aravimth","age":"20","place":"pondy","place":"villianur"}
# # print(len(mydict))
# print(mydict[3])
# print(mydict)

# mydict={"name":"aravinth","age":"20","place":"pondy"}-----------------access
# print(mydict["age"])
# print(mydict.get("name"))
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# mydict={"name":"aravinth","age":"20","place":"pondy"}
# mydict["place"]="villianur"
# mydict.update({"name":"tharun"})
# mydict.pop("age")
# mydict.popitem()
# del mydict["age"]
# print(mydict)

# mydict={"name":"aravinth","age":"20","place":"pondy"}
# for i in mydict:
#     print(i)

# for i in mydict:
#     print(mydict[i])

# for i,j in mydict.items():
#     print(i,j)

# mydict.setdefault("areaa","villianur")
# print(mydict)

# mydict.copy()
# print(mydict)

# ----------nested dictionaries-----------

# student={
#     "student 1":{
#         "name":"tharun",
#         "age":"15",
#         "place":"pondy"
#     },
#     "student 2":{
#         "name":"arun",
#         "age":"16",
#         "place":"pondy"
#     },
#     "student 3":{
#         "name":"kavi",
#         "age":"17",
#         "place":"pondy"
#     },
# }
# print(student)
# print(student["student 1"])
# print(student["student 2"])
# print(student["student 3"])

# for i,j in student.items():
#     print(i)
#     for k in j:
#         print(k,j[k])


# student1={
#     "name":"tharun",
#     "age":"15",
#     "place":"pondy"
# }
# student2={
#     "name":"aravinth",
#     "age":"20",
#     "place":"villianur"
# }
# student3={
#     "name":"arun",
#     "age":"18",
#     "place":"pondy"
# }

# student={
#     "student1":student1,
#     "student2":student2,
#     "student3":student3
# }
# # print(student)
# for i,j in student.items():
#     print(i)
#     for n in j:
#         print(n,j[n])