def NULL_not_found(object: any) -> int:
    x = 0
    if (object == None):
            print("Nothing:", object, type(object))
            x += 1
    if(type(object)):
        if (type(object) == float and object != object):
            print("Cheese:", object, type(object))
            x += 1
        if (type(object) == int and object == 0):
            print("Zero:", object, type(object))
            x += 1
        if (type(object) == str and object == ""):
            print("Empty:", object, type(object))
            x += 1
        if (type(object) == bool):
            print("Fake:", object, type(object))
            x += 1
        if (x == 0):
            print("Type not found")
            return 1
    return 0