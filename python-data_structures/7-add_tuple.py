#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    tuple_a = tuple_a + (0, 0)  # make sure it has 2 elements
    tuple_b = tuple_b + (0, 0)
    
	  # add element 0 of a and b, and element 1 of a and b
    tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (tuple)
