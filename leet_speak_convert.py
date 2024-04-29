"""
Leet speak is a term for the style of typing that replaces letters with numbers or symbols that resemble them, e.g. leet becomes 1337. Speak might become 5p3@k. 
There is a variety of different character substitutions, but here is the translation table we will use for this assignment:

a -> @
A -> 4
B, b -> 8
E, e -> 3
I, i -> !
L, l -> 1
O, o -> 0
S, s -> 5

"""

s = "pizza" # -> 5p3@k

def convert(s):
    s_list = []
    for i in range(len(s)):
        s_list.append(s[i])

    for i in range(len(s_list)):
        if s_list[i] == "a":
            s_list[i] = "@"
        elif s_list[i] == "A":
            s_list[i] = "4"
        elif s_list[i] == "B" or s_list[i] == "b":
            s_list[i] = "8"
        elif s_list[i] == "E" or s_list[i] == "e":
            s_list[i] = "3"
        elif s_list[i] == "I" or s_list[i] == "i":
            s_list[i] = "!"
        elif s_list[i] == "L" or s_list[i] == "l":
            s_list[i] = "1"
        elif s_list[i] == "O" or s_list[i] == "o":
            s_list[i] = "0"
        elif s_list[i] == "S" or s_list[i] == "s":
            s_list[i] = "5"

    new_s = ""
    for letter in s_list:
        new_s += letter

    return(new_s)
convert(s)