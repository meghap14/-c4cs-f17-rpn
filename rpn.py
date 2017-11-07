#!/usr/bin/env python3
import operator
import readline
import sys
#from colors import *


#sys.stdout.write(GREEN)

ops = {
    "+" : operator.add, 
    "-" : operator.sub,
    "^" : operator.pow,
   # "/" : operator.div,
    "*" : operator.mul
}

def calculate(arg):
    stack = list()
    for token in arg.split():
       try:
            stack.append(int(token))
       except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1, arg2)
            result2 = function(arg2, arg1)
            stack.append(result)
            print(result2)
    print("\033[1;33;44m The answer is: ", stack)
    print("\033[1;37;40m")
    return stack.pop()
    pass

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ =='__main__': # Note: that's "underscore underscore n a m e ..."
    main()
    
    #c4cs-f17-rpn
