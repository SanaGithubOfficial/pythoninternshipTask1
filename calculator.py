#!/usr/bin/env python3
"""
CLI Calculator App - Developed by Sana 
Elevate Labs Internship Task

An advanced Python command-line calculator that supports:
- Multiple operations
- Error handling
- Colored output
- Automatic logging
"""

import argparse
import math
import datetime
from colorama import Fore, Style

# ---------- Functions for Operations ----------
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "Error! Division by zero." if b == 0 else a / b
def mod(a, b): return a % b
def power(a, b): return math.pow(a, b)

# ---------- Logging Function ----------
def log_operation(operation, a, b, result):
    with open("calc_log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} | {operation}({a}, {b}) = {result}\n")

# ---------- Main Program ----------
def main():
    parser = argparse.ArgumentParser(
        description="🧮 Command-line Calculator supporting multiple operations."
    )
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div", "mod", "pow"],
        help="Choose operation: add, sub, mul, div, mod, pow"
    )
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed output")

    args = parser.parse_args()

    # Operation mapping
    operations = {
        "add": ("Addition", add),
        "sub": ("Subtraction", sub),
        "mul": ("Multiplication", mul),
        "div": ("Division", div),
        "mod": ("Modulus", mod),
        "pow": ("Power", power)
    }

    op_name, func = operations[args.operation]
    result = func(args.num1, args.num2)

    # Log operation
    log_operation(args.operation, args.num1, args.num2, result)

    # Output formatting
    print(Fore.CYAN + f"\n🧮 Operation: {op_name}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Input: {args.num1}, {args.num2}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Result: {result}" + Style.RESET_ALL)

    if args.verbose:
        print(Fore.MAGENTA + "✅ Operation successfully logged to calc_log.txt" + Style.RESET_ALL)

if _name_ == "_main_":
    main()


