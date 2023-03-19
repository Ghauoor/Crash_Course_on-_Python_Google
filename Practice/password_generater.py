import random

lower = "abcdefghijklmnopqrstuvxyz"
uper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
NUMBER = "0123456789"
Symbol = "[]{}#()*;._-"

all = lower + uper + NUMBER + Symbol

length = 9
password = "".join(random.sample(all, 9))

print(" The Password You Generate is  ", password)
