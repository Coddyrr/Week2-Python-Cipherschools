# pratice for loop
# ask user name and count each character
# "Surjeet Singh" 
# S: 2
#u: 1
#r: 1
#j: 1
#e: 2
#t: 1
# : 1
#i: 1
#n: 1
#g: 1
#h: 1
name = input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]