#!/usr/bin/python3

def print_last_digit(number):
    for c in number:
         if ord(c) >= 97 and ord(c) <= 122:
              c = chr(ord(c) - 32)
               print("{}".format(c), end="")
               print("")
