#!/usr/bin/python3
def no_c(mystr):
    my_list = [letter for letter in mystr if (letter.lower() != "c")]
    return ("".join(my_list))
