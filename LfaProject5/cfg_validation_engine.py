from sys import argv
f = open(argv[1], "r")
variables = []
terminals = []
productions = []
starts=[]
ok = 1
final = 0
for s in f:
    # print(s)
    if s[0] == "#":
        pass
    elif s == "Variables:\n":
        for variable in f:
            if variable[0]=="#":
                pass
            else:
                if variable == "End\n":
                    break
                variable.strip()
                variables.append(variable[0])
    elif s == "Terminals:\n":
        for terminal in f:
            if terminal[0] == "#":
                pass
            else:
                if terminal == "End\n":
                    break
                terminal.strip()
                terminals.append(terminal[0])
    elif s == "Productions:\n":
        for line in f:
            if line[0]=="#":
                pass
            else:
                if line == "End\n":
                    break
                production = [x for x in line.strip().split("-")]
                prod=[]
                print(production[0])
                if production[0] not in variables:
                    ok=0
                    break
                prod.append(production[0])
                prod2=[]
                rez=[x for x in production[1].strip().split(" ")]
                for cv in rez:
                    if cv in terminals or cv in variables:
                        prod2.append(cv)
                    else:
                        ok=0
                        break
                if ok==1:
                    nr=0
                    for x in prod2:
                        if x in terminals:
                            nr+=1
                    if nr==len(prod2):
                        final=1
                    prod.append(prod2)
                    productions.append(prod)
        if ok==0:
            break
    elif s == "StartVariable:\n":
        for start in f:
            if start[0] == "#":
                pass
            else:
                if start == "End":
                    break
                start.strip()
                starts.append(start[0])
        if len(starts)>1:
            ok=0
            break
        if starts[0]!=productions[0][0][0]:
            ok=0
            break

f.close()
"""
print(variables)
print(terminals)
print(productions)
print(starts)
"""

if ok == 1 and final == 1:
    print("CFG valid")
else:
    print("CFG invalid")