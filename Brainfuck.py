import sys

def Brainfuck(string, inType, outType):
    cells = 30000
    reg = [0 for i in range(cells)]
    ptr = 0 #reg pointer
    pc = 0 #string pointer
    loopStk = []

    while pc < len(string):
        curSym = string[pc]
        
        if curSym == "+":
            reg[ptr] += 1
            if reg[ptr] > 255:
                print "Cell value over 255."
                sys.exit()
        
        elif curSym == "-":
            reg[ptr] -= 1
            if reg[ptr] < 0:
                print "Cell value under 0."
                sys.exit()
        
        elif curSym == ">":
            ptr += 1
            if ptr >= cells:
                print "Over array bounds."
                sys.exit()
                
        elif curSym == "<":
            ptr -= 1
            if ptr < 0:
                print "Under array bounds."
                sys.exit()
                
        elif curSym == ".":
            if outType == "c": sys.stdout.write(chr(reg[ptr]))
            elif outType == "i": print "{} ".format(reg[ptr])
        
        elif curSym == ",":
            try:
                if inType == "c": reg[ptr] = ord(raw_input())
                elif inType == "i": reg[ptr] = int(raw_input())
            except:
                print "Invalid input."
                continue
            
        elif curSym == "[":
            if reg[ptr] == 0:
                loops = 1
                while loops != 0:
                    pc += 1
                    if string[pc] == "[": loops += 1
                    elif string[pc] == "]": loops -= 1
            else: loopStk.append(pc)
                
        elif curSym == "]":
            if reg[ptr] != 0: pc = loopStk[-1]
            else: loopStk.pop()
            
        pc += 1

if __name__ == "__main__":
    inputType = sys.argv[1]
    if inputType == "cmd": string = sys.argv[2]
    elif inputType == "file":
        myfile = open(sys.argv[2])
        string = myfile.read()
        myfile.close()
    else: print "Only 'cmd' and 'file' valid"; sys.exit()
    inType, outType = sys.argv[3]

    Brainfuck(string, inType, outType)
