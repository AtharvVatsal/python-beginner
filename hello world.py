name = input("Enter Your name -> ")
gender = input("Whats Your Gender (M) or (F) -> ").upper()
if len(name) <= 6:
    print("A SHORT NAME")
else:
    print("A >6 Letters NAME")
if gender == 'M':
    print(f"Hello Mr. {name}")
elif gender == 'F':
    print(f"Hello Ms/Mrs. {name} ")
else:
    print("There are only Two Genders")
print("THANK YOU!")