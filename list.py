number = [3, 5, 8, 5, 0, 11]
number.append(10)           #adds 10 to last of a list and modifies it
number.insert(0, 10)        #adds 10 to first position in a list
number.remove(5)            #removes 5 from a list
number.pop()                #removes last value of a list
number.clear()              #empties the list
number.index(5)             #find the index of first occurence of 5 in the list
print(5 in number)          #checks if 5 is in list or not, boolean
print(number.count(5))      #checks nos of times 5 is in a list
number.sort()               #sorts list an moifies it as a new list
number.reverse()            #reverses the list
number_2 = number.copy()    #copies our list so that any changes made to list after this wont affect our real list


#Tupples
l = (1, 2, 3, 4)        #This is a tupple, it is a list that cannot be modified
