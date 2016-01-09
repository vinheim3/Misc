import sys

inputType = sys.argv[1]
if inputType == "cmd": string = sys.argv[2]
elif inputType == "file":
    myfile = open(sys.argv[2])
    string = myfile.read()
    myfile.close()
else: print "Only 'cmd' and 'file' valid"; sys.exit()

reg = [0 for i in range(30000)]
ptr = 0 #reg pointer
pc = 0 #string pointer
loopStk = []

#input in the form of an int, output in the ascii representation of an int
while pc < len(string):
    curSym = string[pc]
    
    if curSym == "+": reg[ptr] += 1
    
    elif curSym == "-": reg[ptr] -= 1
    
    elif curSym == ">":
        ptr += 1
        if ptr >= 30000:
            print "Over array bounds."
            sys.exit()
            
    elif curSym == "<":
        ptr -= 1
        if ptr < 0:
            print "Under array bounds."
            sys.exit()
            
    elif curSym == ".": sys.stdout.write(chr(reg[ptr]))
    
    elif curSym == ",":
        try:
            reg[ptr] = int(input())
        except:
            print "Invalid input."
            continue
        
    elif curSym == "[":
        if reg[ptr] == 0:
            loops = 1
            while 1:
                pc += 1
                if string[pc] == "[": loops += 1
                elif string[pc] == "]":
                    loops -= 1
                    if loops == 0: break
        else: loopStk.append(pc)
            
    elif curSym == "]":
        a = loopStk.pop()
        if reg[ptr] != 0:
            pc = a
            continue
        
    pc += 1
