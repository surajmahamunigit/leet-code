#write a program to remove duplicates in the string

#input: AABCCCSS
#output: ABCS

#user input
str1=input("Enter the string to remove duplicates: ")


########################## Using not in ########################

## logic 1:

output=""

for ch in str1:

    #if ch is not in output, add it
    if ch not in output:
        output+=ch

print("Output using not in logic 1: ",output)


### logic 2:

#core logic
l=[]

#go over each character in the string
for ch in str1:

    #if ch is not in list, add it.
    if ch not in l:
        l.append(ch)

#print output
output="".join(l)
print("Output using not in logic 2: ",output)


######################## using set  ############

#core logic

#convert string into set
s1=set(str1)    #set doesnt allow any duplicates but order of characters will be random

#output
output="".join(s1)
print("Output using set data-structure: ",output)
