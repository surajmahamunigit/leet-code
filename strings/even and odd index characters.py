# print characters present at even and odd index separately for the given string

###### option 1  ######

#User input
str=input("Enter the given string: ")

#even index characters
print("Printing even index characters: ")
i=0

while i<len(str):
    print(str[i])
    i=i+2

#odd index characters
print("Printing odd index characters: ")
i=1

while i<len(str):
    print(str[i])
    i=i+2


##########  Option 2  ############

print("Printing even index characters: ",str[::2])
print("Printing odd index characters: ",str[1::2])

