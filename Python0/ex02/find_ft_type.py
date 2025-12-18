def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)

    if obj_type is list:
        print(f"List : {obj_type}")
    elif obj_type is tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type is set:
        print(f"Set : {obj_type}")
    elif obj_type is dict:
        print(f"Dict : {obj_type}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
