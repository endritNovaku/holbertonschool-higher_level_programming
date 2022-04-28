#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    operator = ['+', '-', '*', '/']
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    op1 = int(argv[1])
    op2 = argv[2]
    op3 = int(argv[3])
    if op2 == "+":
        print(op1, op2, op3, "=", add(op1, op3))
    if op2 == "-":
        print(op1, op2, op3, "=", sub(op1, op3))
    if op2 == "*":
        print(op1, op2, op3, "=", mul(op1, op3))
    if op2 == "/":
        print(op1, op2, op3, "=", div(op1, op3))
