# Write a program to reverse the internal content of every second word in the given string

#User input
str=input("Enter the string: ")

#split the string
l=str.split()

#reverse every second word
l2=[]
index=0

while index<len(l):
    #skip even index word
    if index%2==0:
        l2.append(l[index])
    #reverse odd index word
    else:
        l2.append(l[index][::-1])

    index+=1


# print output
output=" ".join(l2)
print(output)
