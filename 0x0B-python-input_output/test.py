#!/usr/bin/python3

with open("student.json", "r", encoding="utf-8")as f:
     j = f.read()
str1 = j.replace(" ", "")
str2 = str1.replace("{", "")
str3 = str2.replace("}", "")
li1 = str3.split(",")
li2 = []
for i in li1:
    li2.append(i.split(":"))
for j in li2:
    if j[0] == '"age"':
        j[1] = int(j[1])

print(li2)
