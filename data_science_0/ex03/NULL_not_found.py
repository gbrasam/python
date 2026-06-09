def NULL_not_found(object: any) -> int:
    type_object = type(object)
    if object is None:
        print(f"Nothing: None {type_object}")
        return 0
    elif object != object:
        print(f"Cheese: nan {type_object}")
        return 0
    elif object == 0 and type_object is int:
        print(f"Zero: 0 {type_object}")
        return 0
    elif object == "":
        print(f"Empty: {type_object}")
        return 0
    elif object is False and type_object is bool:
        print(f"Fake: False {type_object}")
        return 0
    else:
        print("Type not Found")
        return 1
