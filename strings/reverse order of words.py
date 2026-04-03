# Write a program to reverse the order of words in the given string

## User input
str=input("Enter the string")

## split the string
l=str.split()  ## [Python,is,easy]

## reverse the list
rev_l=l[::-1]  ## [easy,is,Python]

## join the reversed list
output=" ".join(rev_l)
print(output)