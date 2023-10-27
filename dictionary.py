value = {
    "Name": "Atharv Vatsal", 
    "Age": "18", 
    "is_legal": True
}
print(value["Name"])
print(value["Age"])
print(value.get("birthdate", "Not Given"))      #dic.get() does not give a error like dic[] if given value is not in a dictionary