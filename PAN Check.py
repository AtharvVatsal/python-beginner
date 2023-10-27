def pan():
    no  = input("Enter PAN Numner: \n")
    if len(no)!=10:
        return('Invalid PAN')
    else:
        if no[0:5].isalpha() and no[5:9].isdigit() and no[-1].isalpha():
            return("Valid PAN")
        else:
            return("Invalid PAN")
print(pan())