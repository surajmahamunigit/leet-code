# Write a program to reverse internal content of each word in given string

# User input
str=input("Enter the string: ")

# split it
l=str.split()

l2=[]

# reverse each word
for word in l:
    l2.append(word[::-1])

# join the list
output=" ".join(l2)
print(output)
