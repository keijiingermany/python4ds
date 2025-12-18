def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            label = "Nothing: None"
        elif isinstance(object, float) and object != object:
            label = "Cheese: nan"
        elif type(object) is int and object == 0:
            label = f"Zero: {object}"
        elif type(object) is str and object == '':
            label = "Empty:"
        elif type(object) is bool and object is False:
            label = "Fake: False"
        else:
            print("Type not Found")
            return 1
        print(label, type(object))
        return 0
    except Exception:
        print("Type not Found")
        return 1
