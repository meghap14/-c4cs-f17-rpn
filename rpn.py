#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        if token =='+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg1 + arg2
            stack.append(result)
        elif token == '-':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 - arg2
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()
    pass

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ =='__main__': # Note: that's "underscore underscore n a m e ..."
    main()
