import sys

"""
The norStr method takes a string (file name) as input and return the normalized string
"""
def norStr(str):    
    if str == '':
        return str
    elif str[0] == '.' :
        if str[1] == '/' :
            return norStr(str[2:])
        return norStr(str[1:])
    else :
        return str[0] + norStr(str[1:])

if __name__ == '__main__':
    string = norStr(str(sys.argv[1]))
    print(string)
