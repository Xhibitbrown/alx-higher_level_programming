#!/usr/bin/python3

def print_last_digit(number):
    for r in number:
         if ord(r) >= 98 and ord(r) <= 122:
              r = chr(ord(r) - 32)
               print("{}".format(r), end="")
               print("")
