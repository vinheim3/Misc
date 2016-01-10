import sys

def Ook(string, inType, outType):
    from Brainfuck import Brainfuck
    
    mapp = {
        ".?": ">",
        "?.": "<",
        "..": "+",
        "!!": "-",
        "!.": ".",
        ".!": ",",
        "!?": "[",
        "?!": "]"
    }

    commands = string.split()
    newStr = ""
        
    for i in range(0, len(commands), 2):
        left, right = commands[i:i+1+1]
        newStr += mapp[left[3]+right[3]]

    Brainfuck(newStr, inType, outType)

if __name__ == "__main__":
    inputType = sys.argv[1]
    if inputType == "cmd": string = sys.argv[2]
    elif inputType == "file":
        myfile = open(sys.argv[2])
        string = myfile.read()
        myfile.close()
    else: print "Only 'cmd' and 'file' valid"; sys.exit()
    inType, outType = sys.argv[3]

    Ook(string, inType, outType)
