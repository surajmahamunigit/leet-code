# write a program to merge characters of two strings by taking characters alternatively

#user input
s1=input("Enter a string")
s2=input("Enter another string")

#merge two strings
i,j=0,0
output=''

while i<len(s1) or j<len(s2):
    #check s1 --> index<length
    if i<len(s1):
        output=output+s1[i]
        i+=1

    #check s2 --> j<length
    if j<len(s2):
        output=output+s2[j]
        j+=1

#print output
print(output)