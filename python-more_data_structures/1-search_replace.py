#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    # empty list
    for element in my_list:
        # looking for search, and replacing with replace
        if element == search:
            new_list.append(replace)
    # otherwise just append the element
        else:
            new_list.append(element)
    return (new_list)
