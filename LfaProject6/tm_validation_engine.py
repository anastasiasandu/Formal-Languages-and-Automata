from sys import argv
f = open(argv[1], "r")
letters = []
states = []
transitions = []
existaS = 0
# abbaa*abbaa # cuv de input
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

if 'A' not in states or 'R' not in states:
    ok = 0
"""
print(letters)
print(states)
print(transitions)
"""
if ok == 1 and existaS==1:
    print("TM valid")
else:
    print("TM invalid")
