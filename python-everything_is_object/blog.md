
# Python: Everything is object!

## Introduction
####     Eveything in python is an object. An object is an instance of a class. It holds the data and functions. Objects are either mutable or immutable.
    Example of an object.
    class Taco:
        meat = ""
    taco = Taco()
    taco.meat = "Asada"
#### We have class Taco that defines the structure of the object. And then create an object taco with the attribute meat. And add a value to meat called Asada. The object is an instance of the class.

## ID and Type
#### All objects in Python have a unique ID and a type. ID is the memory address, and type is the objects class.
    class Taco:
        meat = ""
    taco1 = Taco()
    taco2 = Taco()

    even though they are both referencing Taco(), they will both have a different unique id.

## Mutable Objects
#### Mutable objects can be changed after they have been created.
    taco = [1, 2, 3]
    taco.append(4)
    print(f"after appending: {taco}")

    output: after appending: [1, 2, 3, 4]

## Immutable Objects
#### Immutable objects can't be changed after they are created.
    Here are some immutable objects in Python: Integers, Floats, Strings, Tuples...
#### Immutable objects help with memory usage, and can help with unexpected errors since they can't be changed and will remain consistent.

## Why does it matter how differently Python treats mutable and immutable objects?
    Using the correct choice can help with memory management, performance, thread safety, debugging, and code reliability.

## How arguments are passed to functions,and what does that imply for mutable and immutable objects?
#### Function arguments are passed by object reference. Depending on whether they are mutable or immutable.
    If you are modifying a list, it will modify that list since its mutable. But if you modify a tuple, it wil create a new object containg that change.
