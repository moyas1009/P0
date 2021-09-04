input = open('Test.txt','r')
content = input.read()
#print(content.split('\n'))
input.close()
flagCorrect = False
variables = {}
lpcount = 0
rpcount = 0
lbcount = 0
rbcount = 0
tocount = 0
endcount = 0
outcount = 0
for i in content.split('\n'):
    if '(' in i:
        lpcount = lpcount +1
        #print(i)
    if ')' in i:
        rpcount = rpcount +1
        #print(i)
    if '[' in i:
        lbcount = lbcount +1
        #print(i)
    if ']' in i:
        rbcount = rbcount +1
        #print(i)
    if 'TO' in i:
        tocount = tocount +1
        #print(i)
    if 'END' in i:
        endcount = endcount +1
        #print(i)
    if 'END' in i:
        outcount = outcount +1
        #print(i)

if (lbcount != rbcount):
    print("You are missing a bracket!")
if (lpcount != rpcount):
    print("You are missing a parenthesis!")
if (tocount != endcount or tocount != outcount):
    print("You are missing an end!")

tokens = content.split('\n')

instructions = {
    "MOVE": [1, "number"],
    "RIGHT": [1, "number"],
    "LEFT": [1, "number"],
    "ROTATE": [1, "number"],
    "LOOK": [1, "N.O.S.E"],
    "DROP": [1, "number"],
    "FREE": [1, "number"],
    "PICK": [1, "number"],
    "POP": [1, "number"],
    "DEFINE": [2, "string", "number"],  
}

for i in tokens:
    for j in instructions:
        if j in i:
            ia = i[i.find(j):]
            #print(instructions[j][0])
            args = i[(i.find(j) + len(j)+1):]
            #print(args)
            argss = args.split(" ")
            #print(argss)
            if len(argss) < instructions[j][0]:
                print("You are missing an argument for a function")
                break
            currentinst = 1
            for arg in range(instructions[j][0]):
                if instructions[j][currentinst] == "number":
                    try:
                        res = isinstance(int(argss[arg]), int)
                    except:
                        print("Wrong data type(number)")
                        break
                    if not res:
                        print("Wrong data type(number)")
                        print(argss)
                        break
                if instructions[j][currentinst] == "N.O.S.E":
                    if argss[arg] != "N" or argss[arg] != "O" or argss[arg] != "S" or argss[arg] != "E" :
                        print("Only N,O,S,E are admitted")
                        break
                if instructions[j][currentinst] == "string":
                    res = isinstance(argss[arg], str)
                    if not res:
                        print("Wrong data type(str)")
                        print(arg)
                        print(argss)
                        break
                if j == "DEFINE":
                    variables[argss[0]] = argss[1]
                currentinst = currentinst + 1



            



