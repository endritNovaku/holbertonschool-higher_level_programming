#!/usr/bin/python3
#remove c or C from a string
def no_c(my_string):
    new_list = []
    #turn the string to list and remove c characters
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_list.append(my_string[i])
    #convert the list back to a string and return the new_string
    new_string = ''.join(map(str, new_list))
    return new_string
