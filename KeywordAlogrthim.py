
mykeywords = open("Keywords.txt", "r")
Userinput = "RSA"
for line in mykeywords:
    templist = line.split(", ")
    for i in range(len(templist)):
        print("Word: ", templist[i])

        print(Userinput.find(templist[i]))
        if templist[i] in Userinput:
            index = templist[-1]

          
mykeywords.close()
print(index) 

myresponses = open("Answers.txt", "r")
temp = 0 
for line in myresponses:
    if temp == 0:
        if index == line:
            temp = 1
    elif temp == 1:
        answer = line
        break 
print(answer)
