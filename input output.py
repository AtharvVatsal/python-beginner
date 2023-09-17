name = input("Enter your name ")
birth = int(input("Enter your Birth Year "))
age = 2023 - birth
sex = input("Gender ")
print(f""" Biodata>>>
      Name: {name}
      DOB: {birth}
      Age: {age}
      Gender: {sex}""")        #Concatenated Strings