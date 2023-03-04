from sys import argv
f = open(argv[1], "r")
letters = []
states = []
transitions = []
existaS = 0
input=argv[2]# cuv de input care incepe si se termina cu _ pe langa cuv efectiv : ex _abbaa*abbaa_
cuv=[]
for i in input:
    cuv.append(i)
ok = 1
for s in f:
    if s[0] == "#":
        pass
    elif s == "Sigma:\n":
        for letter in f:
            if letter[0] == "#":
                pass
            else:
                if letter == "End\n":
                    break
                letter.strip()
                letters.append(letter[0])
    elif s == "States:\n":
        for line in f:
            if line[0] == "#":
                pass
            else:
                if line == "End\n":
                    break
                state = [x for x in line.strip().split(",")]
                if len(state[len(state)-1])>1:
                    state[len(state) - 1]=state[len(state)-1][0]
                if len(state) == 2:
                    if state[1] == 'S':
                        if existaS == 0:
                            existaS = 1
                            start = state[0]
                        else:
                            ok = 0
                            break
                if len(state) == 3:
                    if state[1] == 'S' or state[2] == 'S':
                        if existaS == 0:
                            existaS = 1
                            start = state[0]
                        else:
                            ok = 0
                            break
                states.append(state[0])   # doar liteara ca S tinem minte separat
    elif s == "Transitions:\n":
        for line in f:
            if line[0] == "#":
                pass
            else:
                if line == "End":
                    break
                transition = [x for x in line.strip().split(",")]
                if transition[0] not in states:
                    ok=0
                    break
                if transition[2] not in states:
                    ok=0
                    break
                cv = [x for x in transition[1].strip().split(" ")]
                if cv[0] not in letters and cv[0] != '_' and cv[0] != 'x':
                    ok=0
                    break
                transition[1] = cv
                transitions.append(transition)

f.close()
"""
print(letters)
print(states)
print(transitions)
"""
ok = 0
i = 1
s_curent=start
while i<len(cuv) and s_curent!='A' and s_curent!='R':
    letter=cuv[i]
    for j in range(len(transitions)):
        if transitions[j][0] == s_curent and transitions[j][1][0] == letter:
            s_curent = transitions[j][2]
            if transitions[j][1][1]=='x':
                cuv[i]='x'
                if transitions[j][1][2]=='r':
                    i+=1
                else:
                    i-=1
            else:
                if transitions[j][1][1]=='r':
                    i+=1
                else:
                    i-=1
            break

if s_curent == 'A':
    print("acceptat")
else:
    print("neacceptat")